import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from view import views
import src.country_clusters as countries
import src.visualizations as visu


def sa_page():
    page = html.Div(
        children=[views.navbar, views.landing_text,
                  html.H1("Dados agrupados dos países da América do Sul"),
                  html.H2("Total de casos"),
                  dcc.Graph(
                      id='cases',
                      figure=visu.total_cases(countries.south_america())
                  ),

                  html.H2("Total de casos por milhão de habitantes"),
                  dcc.Graph(
                      id='cases',
                      figure=visu.total_cases_mil(countries.south_america())
                  ),

                  html.H2("Média móvel de 7 dias de novos casos por milhão de habitantes"),
                  dcc.Graph(
                      id='new_cases_smooth',
                      figure=visu.new_cases_smooth_mil(countries.south_america())
                  ),

                  html.H2("Mortes totais por país"),
                  dcc.Graph(
                      id='deaths',
                      figure=visu.total_deaths(countries.south_america())
                  ),

                  html.H2("Mortes totais por milhão de habitantes"),
                  dcc.Graph(
                      id='deaths',
                      figure=visu.total_deaths_mil(countries.south_america())
                  ),

                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                  dcc.Graph(
                      id='new_deaths',
                      figure=visu.new_deaths_smooth_mil(countries.south_america())
                  ),

                  html.H2("PIB per capita"),
                  dcc.Graph(
                      id='rep_rate',
                      figure=visu.gdp(countries.south_america())
                  ),

                  html.H2("IDH dos países da América do Sul"),
                  dcc.Graph(
                      id='rep_rate',
                      figure=visu.hdi(countries.south_america())
                  ),

                  html.H2("Índice de Gini"),
                  dcc.Graph(
                      id='rep_rate',
                      figure=visu.gini(countries.south_america())
                  )]
    )
    return page
