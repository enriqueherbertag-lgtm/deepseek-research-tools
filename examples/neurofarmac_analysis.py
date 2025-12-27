"""
Example: Applying DeepSeek tools to NeuroFarmac research.
"""

from deepseek_tools.paper_analyzer import PaperAnalyzer

def analyze_neurofarmac_concept():
    """Demonstrate how DeepSeek tools help NeuroFarmac research."""
    
    # Simulated NeuroFarmac concept paper text
    neurofarmac_text = """
    NeuroFarmac: An Integrated Brain-on-a-Chip Platform for Neuropharmacology
    
    ABSTRACT: We present NeuroFarmac, a novel platform integrating brain organoids, 
    functional blood-brain barrier, and microelectrode arrays for real-time drug assessment.
    
    INTRODUCTION: Current drug screening lacks physiological relevance. NeuroFarmac 
    addresses this by creating a biomimetic neural environment.
    
    METHODS: The platform combines three layers: vascular interface with BBB cells, 
    3D human brain organoids, and high-density MEA for electrophysiological monitoring.
    
    RESULTS: Preliminary data shows reproducible neural network activity and 
    measurable drug responses at physiologically relevant concentrations.
    
    DISCUSSION: This platform bridges the gap between simple 2D assays and 
    complex animal models, enabling more predictive neuropharmacology.
    """
    
    analyzer = PaperAnalyzer()
    
    # Save text to temporary file for analysis
    with open("temp_neurofarmac.txt", "w") as f:
        f.write(neurofarmac_text)
    
    # Analyze the concept
    results = analyzer.analyze("temp_neurofarmac.txt")
    
    print("=" * 60)
    print("NEUROFARMAC CONCEPT ANALYSIS")
    print("=" * 60)
    
    print("\n STRUCTURAL ANALYSIS:")
    for section, content in results["structure"].items():
        if content:
            print(f"  • {section.upper()}: {content[:100]}...")
    
    print("\n KEY INSIGHTS:")
    for contribution in results["insights"]["key_contributions"]:
        print(f"  ✓ {contribution}")
    
    print("\n RESEARCH IMPLICATIONS:")
    print("  1. Enables real-time neuropharmacological assessment")
    print("  2. Bridges organoid technology with pharmaceutical needs")
    print("  3. Provides quantitative metrics beyond cell viability")
    
    print("\n HOW DEEPSEEK TOOLS HELP:")
    print("  • Rapid literature review for platform validation")
    print("  • Hypothesis generation for experimental design")
    print("  • Comparative analysis with existing methods")
    
    # Cleanup
    import os
    if os.path.exists("temp_neurofarmac.txt"):
        os.remove("temp_neurofarmac.txt")

if __name__ == "__main__":
    analyze_neurofarmac_concept()
