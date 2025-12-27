# DeepSeek Research Tools

Practical AI tools for scientific research using DeepSeek models.

## Quick Start

```bash

# Clone repository
git clone https://github.com/enriqueherbertag-lgtm/deepseek-research-tools
cd deepseek-research-tools

# Install as package
pip install -e .

# Or install dependencies manually
pip install -r requirements.txt


# Run paper analyzer example
python examples/neurofarmac_analysis.py



## Available Tools


## 1. Paper Analyzer

Extract key insights from academic papers using DeepSeek API.


```python


from deepseek_tools import PaperAnalyzer

analyzer = PaperAnalyzer(api_key="your_api_key")
results = analyzer.analyze("path/to/paper.pdf")

print(f"Key contributions: {results['insights']['key_contributions']}")



## 2. Research Workflow Automation

Tools to accelerate literature review and hypothesis generation.


## Example: NeuroFarmac Research

See how these tools assist in computational neuropharmacology research:

- NeuroFarmac Analysis Example (examples/neurofarmac_analysis.py)

- Research Workflow (examples/research_workflow.md)


Installation


From source:

```bash


git clone https://github.com/enriqueherbertag-lgtm/deepseek-research-tools
cd deepseek-research-tools
pip install -e .



## Documentation

Examples (examples/)

Research Workflow (examples/research_workflow.md)

## Author

Enrique Aguayo - NeuroAI Researcher
GitHub: enriqueherbertag-lgtm
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825

## Acknowledgments

DeepSeek team for their open research approach

Neuropharmacology research community

Open-source scientific tools ecosystem
