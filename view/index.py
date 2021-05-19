import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from view import views
import src.country_clusters as countries
import src.visualizations as visu


def index_page():
    page = page = html.Div(
        children=[views.navbar, views.landing_text,
                  html.H1("Dados gerais globais", className="text-center"),
                      dbc.Container(children=[
                          dbc.Row(children=[
                              dbc.Col(
                                  html.Div(
                                      children=[
                                          html.H2("Total de casos"),
                                          dcc.Graph(
                                              id='cases',
                                              figure=visu.total_cases(countries.general())
                                          )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6),
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2("Total de casos por milhão de habitantes"),
                                      dcc.Graph(
                                          id='cases-per-million',
                                          figure=visu.total_cases_mil(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              )], className="g-5"
                          ),
                          dbc.Row(children=[
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2("Média móvel de 7 dias de novos casos por milhão de habitantes"),
                                      dcc.Graph(
                                          id='new-cases-smooth-per-million',
                                          figure=visu.new_cases_smooth_mil(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              ),
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2("Mortes totais por país"),
                                      dcc.Graph(
                                          id='total-deaths',
                                          figure=visu.total_deaths(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              )], className="g-5"
                          ),
                          dbc.Row(children=[
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2("Mortes totais por milhão de habitantes"),
                                      dcc.Graph(
                                          id='deaths-per-million',
                                          figure=visu.total_deaths_mil(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              ),
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                      dcc.Graph(
                                          id='new-deaths-smooth',
                                          figure=visu.new_deaths_smooth_mil(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              )], className="g-5"
                          ),
                          dbc.Row(children=[
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2("PIB per capita"),
                                      dcc.Graph(
                                          id='gdp-per-capita',
                                          figure=visu.gdp(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              ),
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2('''Índice de Desenvolvimento Humano:
                                       mede a qualidade de vida em um país'''),
                                      dcc.Graph(
                                          id='hd-index',
                                          figure=visu.hdi(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              )], className="g-5"
                          ),
                          dbc.Row(
                              dbc.Col(
                                  html.Div(children=[
                                      html.H2(
                                          "Índice de Gini - medido de 0 a 100, quanto maior, mais desigual é o país"),
                                      dcc.Graph(
                                          id='gini-index',
                                          figure=visu.gini(countries.general())
                                      )], className="p-4"
                                  ), xs=11, sm=11, md=6, lg=6
                              ), justify="center", className="g-5"
                          )],
                          fluid=True)
                  ]
    )
    return page
