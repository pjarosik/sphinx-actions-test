# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime

html_theme = 'sphinx_rtd_theme'
html_logo = "https://us4us.eu/wp-content/uploads/2018/10/us4us-logo-white.png"

current_year = datetime.now().year

# -- Project information -----------------------------------------------------

project = 'Us4R/Us4R-lite User Manual'
copyright = f"{current_year}, us4us Ltd"
author = 'us4us Ltd'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinxcontrib.jquery"
]

html_theme_options = {
    'logo_only': True,
    # Set the name of the project to appear in the sidebar
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

latex_documents = [('index', 'user_manual.tex', project, author, 'manual')]

