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
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('data/owid-covid-data.csv')
df_base = df[df['iso_code'].isin(["BRA", "MEX", "USA", "VNM", "KOR", "CHN", "GBR", "NZL", "AUS", "DEU", "FRA", "SWE"])]

fig = px.scatter(df_base, x='date', y='total_cases', color='location')

app.layout = html.Div(children=[
    html.H1(children='Pitão p/ visú de dados \U0001F919'),
    html.Div(children='''
        Smash & Dash: The only way to smash is to then dash \U0001F609
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)