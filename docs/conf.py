# -- Project information -----------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = 'Drawing Generator'
copyright = '2023, hydroft1'
author = 'hydroft1'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.napoleon"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
