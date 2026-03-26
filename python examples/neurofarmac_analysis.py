from deepseek_tools import PaperAnalyzer

# Inicializar (usar variable de entorno DEEPSEEK_API_KEY)
analyzer = PaperAnalyzer()

# Analizar paper
results = analyzer.analyze("path/to/paper.pdf")

# Resultados
print(f"Contribuciones clave: {results['insights']['key_contributions']}")
print(f"Metodología: {results['insights']['methodology']}")
print(f"Limitaciones: {results['insights']['limitations']}")
