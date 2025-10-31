# Configuration file for Sphinx documentation builder.

project = 'Heavens Above'
copyright = '2025, Nabeeha Islam'
author = 'Nabeeha Islam'
release = '1.0'

extensions = [
    'myst_parser',  # Allows Markdown support
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
