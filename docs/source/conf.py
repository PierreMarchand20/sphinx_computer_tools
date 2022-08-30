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


# -- Project information -----------------------------------------------------

project = 'ComputerTools'
copyright = '2022, Pierre Marchand'
author = 'Pierre Marchand'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.asciinema',
    'sphinxcontrib.rsvgconverter',
    'sphinx_copybutton',
    'sphinx_contributors'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Numbering figures
numfig = True
numfig_secnum_depth = 2

# Smart quotes
smartquotes = True

#
rst_epilog = """
.. _VS Code: https://code.visualstudio.com
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

html_title = "Computer tools"

html_theme_options = {
    "source_repository": "https://github.com/PierreMarchand20/computer_tools/",
    "source_branch": "main",
    "source_directory": "docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "css/custom.css"
]

sphinxcontrib_asciinema_defaults = {
    # 'theme': 'solarized-dark',
    'preload': 1,
    # 'font-family': "monospace, 'MesloLGS NF'",
    # 'font-size': '25',
    # 'path': '_static/asciicast/'
}

# -- Options for LaTeC output -------------------------------------------------
latex_engine = 'lualatex'
latex_elements = {
    'tableofcontents': r"",
    'preamble': r'''
\expandafter\def\expandafter\LaTeX\expandafter{\expandafter\text\expandafter{\LaTeX}}

''',
    # https://tex.stackexchange.com/questions/572212/substituting-fonts-for-emojis-in-lualatex
    # Reset defaults plus fallback for emojis
    'fontpkg': r'''
\directlua{luaotfload.add_fallback
   ("emojifallback",
    {
        "NotoColorEmoji:mode=harf;",
        "TwemojiMozilla:mode=harf;"
    }
   )}
\setmainfont{FreeSerif}[
  Extension      = .otf ,
  UprightFont    = *,
  BoldFont       = *Bold,
  ItalicFont     = *Italic,
  BoldItalicFont = *BoldItalic,
  RawFeature={fallback=emojifallback}
]
\setsansfont{FreeSerif}
\setmonofont{FreeMono}
'''
}
