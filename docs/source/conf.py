# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'WRF-GC'
copyright = '2018-2024 The WRF-GC Authors'
author = 'Haipeng Lin, Xu Feng, Tzung-May Fu'

release = '2.0'
version = '2.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_extra_path = ['_extras']
#html_logo = "_static/wrfgc_logo.png"
# html_theme_options = {
#     'logo_only': True,
#     'display_version': False,
# }

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file('custom.css')
