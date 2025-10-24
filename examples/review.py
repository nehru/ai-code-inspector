"""
Main CLI script for running code reviews.

Usage:
    python examples/review.py <file_path>
    
Example:
    python examples/review.py test_samples/buggy_code.py
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.workflow import run_review
from src.report_generator import (
    save_json_report,
    save_markdown_report,
    print_report_summary
)


def main():
    """Main entry point for CLI."""
    
    # Check arguments
    if len(sys.argv) < 2:
        print("❌ Usage: python examples/review.py <file_path>")
        print("Example: python examples/review.py test_samples/buggy_code.py")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Verify file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    try:
        # Run the review workflow
        report = run_review(file_path)
        
        if not report:
            print("❌ Review failed to generate report")
            sys.exit(1)
        
        # Print summary to console
        print_report_summary(report)
        
        # Save reports
        json_path = save_json_report(report)
        md_path = save_markdown_report(report)
        
        print(f"💾 Reports saved:")
        print(f"   - JSON: {json_path}")
        print(f"   - Markdown: {md_path}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Review interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error during review: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
