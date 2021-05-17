import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from view import views
import src.country_clusters as countries
import src.visualizations as visu


def nordic_page():
    nordic_page = html.Div(
        children=[views.navbar, views.landing_text,
                  html.H1("Dados gerais globais"),
                  html.H2("Total de casos"),
                  dcc.Graph(
                      id='cases',
                      figure=visu.total_cases(countries.nordic())
                  ),

                  html.H2("Média móvel de 7 dias de novos casos por milhão de habitantes"),
                  dcc.Graph(
                      id='new_cases_smooth',
                      figure=visu.new_cases_smooth_mil(countries.nordic())
                  ),

                  html.H2("Mortes totais por país"),
                  dcc.Graph(
                      id='deaths',
                      figure=visu.total_deaths(countries.nordic())
                  ),

                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                  dcc.Graph(
                      id='new_deaths',
                      figure=visu.new_deaths_smooth_mil(countries.nordic())
                  ),

                  html.H2("Taxa de reprodução (R) do vírus"),
                  dcc.Graph(
                      id='rep_rate',
                      figure=visu.r_rate(countries.nordic())
                  ),
                  
                  html.H2("Índice Gini"),
                  dcc.Graph(
                      id='gini',
                      figure=visu.gini(countries.nordic())
                  ),
                  
                  html.H2("IDH"),
                  dcc.Graph(
                      id='hdi',
                      figure=visu.hdi(countries.nordic())
                  )
                  ]
    )
    return nordic_page
