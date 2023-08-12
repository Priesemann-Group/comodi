#!/usr/bin/env python
#
# comodi documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = "1.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
"sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
#    "m2r",
    "myst_parser",
    "nbsphinx"
]



# Mock imports
autodoc_mock_imports = [
    "numpy",
    "matplotlib",
    "matplotlib.pyplot",
    "mpl_toolkits",
    "scipy",
    "pymc",
    "pytensor",
    "pandas",
    "filelock",
    "arviz",
    "optax",
    "jax",
    "jax.numpy",
    "diffrax",
    "pytensor",
]

nbsphinx_allow_errors = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Compartmental Models Inference Toolbox"
copyright = "2023, Jonas Dehning"
author = "Jonas Dehning"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = "0.1.0"
# The full version, including alpha/beta/rc tags.
release = "0.1.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

html_show_sourcelink = False


# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

html_theme_options = {
    "collapse_navigation": False,
    "display_version": False,
    "navigation_depth": 4,
    "sticky_navigation": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# Napoleon settings
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
napoleon_use_ivar = True  # True enables links for attribute types
napoleon_use_param = True  # True enables links for parameter types
napoleon_use_rtype = False


#html_logo = "./images/logo.png"
#html_theme_options = {
#    'logo_only': False,
#}


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "comodidoc"


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    #
    # "papersize": "letterpaper",

    # The font size ("10pt", "11pt" or "12pt").
    #
    # "pointsize": "10pt",

    # Additional stuff for the LaTeX preamble.
    #
    # "preamble": "",

    # Latex figure (float) alignment
    #
    # "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, "comodi.tex",
     "Compartmental Models Inference Toolbox Documentation",
     "Jonas Dehning", "manual"),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "comodi",
     "Compartmental Models Inference Toolbox Documentation",
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "comodi",
     "Compartmental Models Inference Toolbox Documentation",
     author,
     "comodi",
     "One line description of project.",
     "Miscellaneous"),
]


# -- Options for intersphinx -------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://docs.scipy.org/doc/numpy", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "pymc": ("https://www.pymc.io/projects/docs/en/stable", None),
    "pytensor": ("https://pytensor.readthedocs.io/en/latest/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "arviz": ("https://python.arviz.org/en/stable/", None),
    "jax": ("https://jax.readthedocs.io/en/latest/", None),
    "diffrax": ("https://docs.kidger.site/diffrax/", None),
    "optax": ("https://optax.readthedocs.io/en/latest/", None),
}

imgmath_image_format = "svg"
imgmath_font_size = 14

autodoc_member_order = "bysource"
