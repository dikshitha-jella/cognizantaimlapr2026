# Configuration file for the Sphinx documentation builder.

import os
import sys

project = 'Banking Management System'
copyright = '2026, Dikshitha'
author = 'Dikshitha'
release = '1.0.0'

# Add the source path
sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']

# Napoleon settings for Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_members = False
napoleon_include_special_members = True

# Autodoc settings
autodoc_typehints = 'description'
autodoc_member_order = 'bysource'
