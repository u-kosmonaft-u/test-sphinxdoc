# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Document example"
copyright = "2023, u-kosmonaft-u"
author = "u-kosmonaft-u"

version = "0.0.1"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_multiversion",
]

templates_path = ["_templates"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_sidebars = {"**": ["versioning.html"]}
html_js_files = ["js/jquery-3.6.3.min.js"]
html_show_sphinx = False
html_show_sourcelink = False
html_theme_options = {"display_version": True, "style_nav_header_background": "#0d284f"}
