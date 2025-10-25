#  Quick Start Guide

Get the AI Code Reviewer running in 5 minutes!

## Step 1: Install Ollama

```bash
# Linux/macOS
curl -fsSL https://ollama.com/install.sh | sh

# Or download from: https://ollama.com/download
```

## Step 2: Pull DeepSeek-R1 Model

```bash
ollama pull deepseek-r1:latest
```

This will download the model (~3-4GB). Verify it works:
```bash
ollama list
```

## Step 3: Install Python Dependencies

```bash
cd ai-code-reviewer
pip install -r requirements.txt
```

## Step 4: Run Your First Review

```bash
python examples/review.py test_samples/buggy_code.py
```

Expected output:
```
 Starting code review for: test_samples/buggy_code.py
============================================================
 Parsing code...
 Parsed python file: 67 lines
 Detecting bugs...
 Found 5 bugs (confidence >= 0.7)
 Analyzing optimizations...
 Found 4 optimization opportunities
 Generating report...
 Report generated: 5 bugs, 4 optimizations
============================================================
 Review complete!

 CODE REVIEW SUMMARY
============================================================
File: buggy_code.py
Language: python
Lines: 67
Overall Severity: HIGH
------------------------------------------------------------
 Bugs Found: 5
   - Critical: 1
   - High: 3
   - Medium: 1
   - Low: 0
 Optimizations: 4
============================================================

 Reports saved:
   - JSON: outputs/review_20250124_143022.json
   - Markdown: outputs/review_20250124_143022.md
```

## Step 5: Review Your Own Code

```bash
python examples/review.py path/to/your/code.py
```

Supported file types: `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c`, `.go`, `.rb`, `.php`

##  Check Your Reports

- **JSON Report**: `outputs/review_TIMESTAMP.json`
- **Markdown Report**: `outputs/review_TIMESTAMP.md`

##  Customize Settings

Edit `config.yaml` to adjust:
- Model temperature
- Confidence thresholds
- Output formats
- Review categories

##  Troubleshooting

### "Ollama connection refused"
```bash
# Start Ollama service
ollama serve
```

### "Model not found"
```bash
# Re-pull the model
ollama pull deepseek-r1:latest
```

### "Out of VRAM"
- DeepSeek-R1 requires ~8GB VRAM
- Close other GPU applications
- Try smaller model: `ollama pull deepseek-r1:7b`

##  Next Steps

1. Review multiple files in your project
2. Integrate into CI/CD pipeline
3. Customize prompts in `src/prompts.py`
4. Add new programming languages

---

**Ready to find bugs? Start reviewing! **
