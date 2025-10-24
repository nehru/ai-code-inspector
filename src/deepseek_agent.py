"""
DeepSeek-R1 agent using Ollama for local inference.
"""
import json
from typing import Dict, Any
import ollama
import yaml


class DeepSeekAgent:
    """Wrapper for DeepSeek-R1 model via Ollama."""
    
    def __init__(self, config_path: str = "config.yaml"):
        """Initialize the agent with configuration."""
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        self.model_name = config['model']['name']
        self.temperature = config['model']['temperature']
        self.max_tokens = config['model']['max_tokens']
        
    def query(self, prompt: str, parse_json: bool = True) -> Dict[str, Any]:
        """
        Send a query to DeepSeek-R1 and get response.
        
        Args:
            prompt: The input prompt
            parse_json: Whether to parse response as JSON
            
        Returns:
            Response as dictionary or raw text
        """
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                options={
                    'temperature': self.temperature,
                    'num_predict': self.max_tokens,
                }
            )
            
            content = response['message']['content']
            
            if parse_json:
                # Try to extract JSON from markdown code blocks
                if '```json' in content:
                    content = content.split('```json')[1].split('```')[0].strip()
                elif '```' in content:
                    content = content.split('```')[1].split('```')[0].strip()
                
                return json.loads(content)
            
            return {"response": content}
            
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON parsing error: {e}")
            print(f"Raw response: {content[:200]}...")
            return {"error": "json_parse_error", "raw_response": content}
        
        except Exception as e:
            print(f"❌ Error querying model: {e}")
            return {"error": str(e)}
    
    def detect_bugs(self, code: str, language: str, prompt_template: str) -> Dict:
        """Detect bugs in code using specialized prompt."""
        prompt = prompt_template.format(code=code, language=language)
        return self.query(prompt, parse_json=True)
    
    def suggest_optimizations(self, code: str, language: str, prompt_template: str) -> Dict:
        """Suggest optimizations using specialized prompt."""
        prompt = prompt_template.format(code=code, language=language)
        return self.query(prompt, parse_json=True)
    
    def generate_summary(self, bug_count: int, opt_count: int, prompt_template: str) -> str:
        """Generate executive summary."""
        prompt = prompt_template.format(bug_count=bug_count, opt_count=opt_count)
        result = self.query(prompt, parse_json=False)
        return result.get('response', 'No summary generated')
