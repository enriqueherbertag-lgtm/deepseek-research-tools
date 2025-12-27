# Research Workflow with DeepSeek Tools

## Phase 1: Literature Review
```python
from deepseek_tools import PaperAnalyzer

# Batch analyze relevant papers
analyzer = PaperAnalyzer()
papers = ["paper1.pdf", "paper2.pdf", "paper3.pdf"]
insights = [analyzer.analyze(p) for p in papers]
