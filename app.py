# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'visuProject'
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('data/owid-covid-data.csv')
df_base = df[df['iso_code'].isin(["BRA", "MEX", "USA", "VNM", "KOR", "CHN", "GBR", "NZL", "AUS", "DEU", "FRA", "SWE"])]

cases = px.line(df_base, x='date', y='total_cases', color='location')

new_cases_smooth = px.line(df_base, x='date', y='new_cases_smoothed', color='location')

deaths = px.line(df_base, x='date', y='total_deaths', color='location')

new_deaths = px.line(df_base, x='date', y='new_deaths_smoothed', color='location')

rep_rate = px.line(df_base, x='date', y='reproduction_rate', color='location')

app.layout = html.Div(children=[
    html.H1(children='Visualizações básicas'),
    html.H4(children="Total de casos"),
    dcc.Graph(
        id='cases',
        figure=cases
    ),

    html.H4(children="Média móvel de 7 dias de novos casos"),
    dcc.Graph(
        id='new_cases_smooth',
        figure=new_cases_smooth
    ),

    html.H4(children="Mortes totais por país"),
    dcc.Graph(
        id='deaths',
        figure=deaths
    ),
    html.H4(children="Média móvel de 7 dias de mortes"),
    dcc.Graph(
        id='new_deaths',
        figure=new_deaths
    ),
    html.H4(children="Taxa de reprodução (R) do vírus"),
    dcc.Graph(
        id='rep_rate',
        figure=rep_rate
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)