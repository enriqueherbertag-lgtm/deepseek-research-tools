from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deepseek-research-tools",
    version="0.1.0",
    author="Enrique Aguayo",
    author_email="eaguayo@migst.cl",
    description="AI tools for scientific research using DeepSeek",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enriqueherbertag-lgtm/deepseek-research-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
)
