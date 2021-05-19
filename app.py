# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output

# Local imports
from view import index, page_not_found, south_america, nordic_countries, dim_reduction

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'visuProject'
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return index.index_page()
    elif pathname == "/america-sul":
        return south_america.sa_page()
    elif pathname == "/paises-nordicos":
        return nordic_countries.nordic_page()
    elif pathname == "/reducao-dim-renda":
        return dim_reduction.dim_red_page()
    elif pathname == "/reducao-dim-comorb":
        return dim_reduction.dim_red_page_sick()
    elif pathname == "/reducao-dim-renda-tsne":
        return dim_reduction.dim_red_page_tsne()
    elif pathname == "/reducao-dim-comorb-tsne":
        return dim_reduction.dim_red_page_tsne_sick()

    # If the user tries to reach a different page, return a 404 message
    else:
        return page_not_found.page_not_found(pathname)


if __name__ == '__main__':
    app.run_server(debug=True)
