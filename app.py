# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Local imports
import src.country_clusters as countries
import src.visualizations as visu

import view.views as views

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'visuProject'
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(children=[views.navbar, views.landing_text,
    html.H1(children='Dados gerais globais'),
    html.H2(children="Total de casos"),
    dcc.Graph(
        id='cases',
        figure=visu.total_cases(countries.general())
    ),

    html.H2(children="Média móvel de 7 dias de novos casos por milhão de habitantes"),
    dcc.Graph(
        id='new_cases_smooth',
        figure=visu.new_cases_smooth_mil(countries.general())
    ),

    html.H2(children="Mortes totais por país"),
    dcc.Graph(
        id='deaths',
        figure=visu.total_deaths(countries.general())
    ),
    html.H2(children="Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
    dcc.Graph(
        id='new_deaths',
        figure=visu.new_deaths_smooth_mil(countries.general())
    ),
    html.H2(children="Taxa de reprodução (R) do vírus"),
    dcc.Graph(
        id='rep_rate',
        figure=visu.r_rate(countries.general())
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
