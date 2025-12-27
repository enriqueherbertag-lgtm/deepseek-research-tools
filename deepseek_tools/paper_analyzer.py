"""
DeepSeek Paper Analyzer
Simple but effective tool for academic paper analysis.
"""

import json
from typing import Dict, List
import pymupdf  # For PDF extraction

class PaperAnalyzer:
    """Analyze academic papers using DeepSeek API."""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com"
        
    def extract_text(self, pdf_path: str) -> str:
        """Extract text from PDF file."""
        try:
            doc = pymupdf.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            return text[:5000]  # Limit for demo
        except Exception as e:
            return f"Error extracting text: {str(e)}"
    
    def analyze_structure(self, text: str) -> Dict:
        """Basic structural analysis of paper."""
        sections = {
            "abstract": self._find_section(text, ["abstract", "summary"]),
            "introduction": self._find_section(text, ["introduction"]),
            "methods": self._find_section(text, ["methods", "methodology"]),
            "results": self._find_section(text, ["results", "findings"]),
            "discussion": self._find_section(text, ["discussion", "conclusion"])
        }
        return sections
    
    def _find_section(self, text: str, keywords: List[str]) -> str:
        """Find section by keywords."""
        text_lower = text.lower()
        for kw in keywords:
            idx = text_lower.find(kw)
            if idx != -1:
                # Return next 500 chars after keyword
                return text[idx:idx+500]
        return ""
    
    def generate_insights(self, text: str) -> Dict:
        """Generate research insights from paper text."""
        insights = {
            "key_contributions": [],
            "methodological_approach": "",
            "potential_limitations": [],
            "future_directions": []
        }
        
        # Simple rule-based extraction (would use DeepSeek API in production)
        if "organoid" in text.lower():
            insights["key_contributions"].append("Uses brain organoid technology")
        if "microelectrode" in text.lower() or "MEA" in text.upper():
            insights["key_contributions"].append("Employs microelectrode array recording")
        
        return insights
    
    def analyze(self, pdf_path: str) -> Dict:
        """Main analysis pipeline."""
        text = self.extract_text(pdf_path)
        structure = self.analyze_structure(text)
        insights = self.generate_insights(text)
        
        return {
            "paper_text_sample": text[:1000],
            "structure": structure,
            "insights": insights,
            "word_count": len(text.split()),
            "section_count": len([v for v in structure.values() if v])
        }

def main():
    """Demo function."""
    analyzer = PaperAnalyzer()
    print("DeepSeek Paper Analyzer - Ready")
    print("Use: analyzer = PaperAnalyzer()")
    print("results = analyzer.analyze('path/to/paper.pdf')")

if __name__ == "__main__":
    main()
