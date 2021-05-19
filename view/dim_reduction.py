import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from view import views
import src.country_clusters as countries
import src.general_purposes_clusters as gp_clusters
import src.visualizations as visu
import plotly.express as px


# https://dash.plotly.com/interactive-graphing
# Update Graphs on Hover


def dim_red_page():
    dim_red_page = html.Div(
        children=[views.navbar, views.landing_text,
                  dbc.Container(children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H1("Redução de dimensionalidade com relação à renda"),
                              html.H3('''Utilizamos UMAP + KMeans para agrupar os dados relacionados a PIB per capta,
                               expectativa de vida, número de leitos de hospital por mil habitantes, IDH e Gini.''',
                                      className="text-muted"),

                              dcc.Graph(
                                  id='renda_kmeans',
                                  figure=visu.dim_red_kmeans(gp_clusters.revenue(), 'renda', 'umap')
                              )], xs=11, sm=11, md=8, lg=8
                          )], justify="center", className="g-5, text-center"
                      ),
                      dbc.Row(children=[
                          dbc.Col(
                              html.Div(
                                  children=[
                                      html.H2("Total de casos"),
                                      dcc.Graph(
                                          id='cases',
                                          figure=visu.total_cases(countries.dim_reduct())
                                      )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Total de casos por milhão de habitantes"),
                                  dcc.Graph(
                                      id='cases-per-million',
                                      figure=visu.total_cases_mil(countries.dim_reduct())
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
                                      figure=visu.new_cases_smooth_mil(countries.dim_reduct())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Mortes totais por país"),
                                  dcc.Graph(
                                      id='total-deaths',
                                      figure=visu.total_deaths(countries.dim_reduct())
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
                                      figure=visu.total_deaths_mil(countries.dim_reduct())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                  dcc.Graph(
                                      id='new-deaths-smooth',
                                      figure=visu.new_deaths_smooth_mil(countries.dim_reduct())
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
                                      figure=visu.gdp(countries.dim_reduct())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2('''IDH dos países da América do Sul -
                                           o IDH mede a qualidade de vida em um país'''),
                                  dcc.Graph(
                                      id='hd-index',
                                      figure=visu.hdi(countries.dim_reduct())
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
                                      figure=visu.gini(countries.dim_reduct())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ), justify="center", className="g-5"
                      )], fluid=True
                  )]
    )
    return dim_red_page

def dim_red_page_tsne():
    dim_red_page_tsne = html.Div(
        children=[views.navbar, views.landing_text,
                  dbc.Container(children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H1("Redução de dimensionalidade com relação à renda"),
                              html.H3('''Utilizamos TSNE + KMeans para agrupar os dados relacionados a PIB per capta,
                               expectativa de vida, número de leitos de hospital por mil habitantes, IDH e Gini.''',
                                      className="text-muted"),

                              dcc.Graph(
                                  id='comorb_kmeans',
                                  figure=visu.dim_red_kmeans(gp_clusters.revenue(), 'renda', 'tsne')
                              )], xs=11, sm=11, md=8, lg=8
                          )], justify="center", className="g-5, text-center"
                      ),
                      dbc.Row(children=[
                          dbc.Col(
                              html.Div(
                                  children=[
                                      html.H2("Total de casos"),
                                      dcc.Graph(
                                          id='cases',
                                          figure=visu.total_cases(countries.tsne_revenue())
                                      )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Total de casos por milhão de habitantes"),
                                  dcc.Graph(
                                      id='cases-per-million',
                                      figure=visu.total_cases_mil(countries.tsne_revenue())
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
                                      figure=visu.new_cases_smooth_mil(countries.tsne_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Mortes totais por país"),
                                  dcc.Graph(
                                      id='total-deaths',
                                      figure=visu.total_deaths(countries.tsne_revenue())
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
                                      figure=visu.total_deaths_mil(countries.tsne_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                  dcc.Graph(
                                      id='new-deaths-smooth',
                                      figure=visu.new_deaths_smooth_mil(countries.tsne_revenue())
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
                                      figure=visu.gdp(countries.tsne_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2('''IDH -
                                           o IDH mede a qualidade de vida em um país'''),
                                  dcc.Graph(
                                      id='hd-index',
                                      figure=visu.hdi(countries.tsne_revenue())
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
                                      figure=visu.gini(countries.tsne_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ), justify="center", className="g-5"
                      )], fluid=True
                  )]
    )
    return dim_red_page_tsne

def dim_red_page_sick():
    dim_red_page_sick = html.Div(
        children=[views.navbar, views.landing_text,
                  dbc.Container(children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H1("Redução de dimensionalidade com relação à comorbidades"),
                              html.H3('''Utilizamos UMAP + KMeans para agrupar os dados relacionados a proporção de diabéticos,
                               proporção de fumantes entre homens e entre mulheres, número de leitos
                               de hospital por mil habitantes e proporção de doenças cardiovasculares.''',
                                      className="text-muted"),

                              dcc.Graph(
                                  id='comorb_kmeans',
                                  figure=visu.dim_red_kmeans(gp_clusters.sickness(), 'sickness', 'umap')
                              )], xs=11, sm=11, md=8, lg=8
                          )], justify="center", className="g-5, text-center"
                      ),
                      dbc.Row(children=[
                          dbc.Col(
                              html.Div(
                                  children=[
                                      html.H2("Total de casos"),
                                      dcc.Graph(
                                          id='cases',
                                          figure=visu.total_cases(countries.dim_reduct_sickness())
                                      )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Total de casos por milhão de habitantes"),
                                  dcc.Graph(
                                      id='cases-per-million',
                                      figure=visu.total_cases_mil(countries.dim_reduct_sickness())
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
                                      figure=visu.new_cases_smooth_mil(countries.dim_reduct_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Mortes totais por país"),
                                  dcc.Graph(
                                      id='total-deaths',
                                      figure=visu.total_deaths(countries.dim_reduct_sickness())
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
                                      figure=visu.total_deaths_mil(countries.dim_reduct_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                  dcc.Graph(
                                      id='new-deaths-smooth',
                                      figure=visu.new_deaths_smooth_mil(countries.dim_reduct_sickness())
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
                                      figure=visu.gdp(countries.dim_reduct_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2('''IDH -
                                           o IDH mede a qualidade de vida em um país'''),
                                  dcc.Graph(
                                      id='hd-index',
                                      figure=visu.hdi(countries.dim_reduct_sickness())
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
                                      figure=visu.gini(countries.dim_reduct_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ), justify="center", className="g-5"
                      )], fluid=True
                  )]
    )
    return dim_red_page_sick

def dim_red_page_tsne_sick():
    dim_red_page_tsne_sick = html.Div(
        children=[views.navbar, views.landing_text,
                  dbc.Container(children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H1("Redução de dimensionalidade com relação à comorbidades"),
                              html.H3('''Utilizamos TSNE + KMeans para agrupar os dados relacionados a proporção de diabéticos,
                               proporção de fumantes entre homens e entre mulheres, número de leitos
                               de hospital por mil habitantes e proporção de doenças cardiovasculares.''',
                                      className="text-muted"),

                              dcc.Graph(
                                  id='comorb_kmeans',
                                  figure=visu.dim_red_kmeans(gp_clusters.sickness(), 'sickness', 'tsne')
                              )], xs=11, sm=11, md=8, lg=8
                          )], justify="center", className="g-5, text-center"
                      ),
                      dbc.Row(children=[
                          dbc.Col(
                              html.Div(
                                  children=[
                                      html.H2("Total de casos"),
                                      dcc.Graph(
                                          id='cases',
                                          figure=visu.total_cases(countries.tsne_sickness())
                                      )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Total de casos por milhão de habitantes"),
                                  dcc.Graph(
                                      id='cases-per-million',
                                      figure=visu.total_cases_mil(countries.tsne_sickness())
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
                                      figure=visu.new_cases_smooth_mil(countries.tsne_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Mortes totais por país"),
                                  dcc.Graph(
                                      id='total-deaths',
                                      figure=visu.total_deaths(countries.tsne_sickness())
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
                                      figure=visu.total_deaths_mil(countries.tsne_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                  dcc.Graph(
                                      id='new-deaths-smooth',
                                      figure=visu.new_deaths_smooth_mil(countries.tsne_sickness())
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
                                      figure=visu.gdp(countries.tsne_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2('''IDH -
                                           o IDH mede a qualidade de vida em um país'''),
                                  dcc.Graph(
                                      id='hd-index',
                                      figure=visu.hdi(countries.tsne_sickness())
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
                                      figure=visu.gini(countries.tsne_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ), justify="center", className="g-5"
                      )], fluid=True
                  )]
    )
    return dim_red_page_tsne_sick

def dim_red_page_pca():
    dim_red_page_pca = html.Div(
        children=[views.navbar, views.landing_text,
                  dbc.Container(children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H1("Redução de dimensionalidade com relação à renda"),
                              html.H3('''Utilizamos PCA + KMeans para agrupar os dados relacionados a PIB per capta,
                               expectativa de vida, número de leitos de hospital por mil habitantes, IDH e Gini.''',
                                      className="text-muted"),

                              dcc.Graph(
                                  id='renda_kmeans',
                                  figure=visu.dim_red_kmeans(gp_clusters.revenue(), 'renda', 'pca')
                              )], xs=11, sm=11, md=8, lg=8
                          )], justify="center", className="g-5, text-center"
                      ),
                      dbc.Row(children=[
                          dbc.Col(
                              html.Div(
                                  children=[
                                      html.H2("Total de casos"),
                                      dcc.Graph(
                                          id='cases',
                                          figure=visu.total_cases(countries.pca_revenue())
                                      )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Total de casos por milhão de habitantes"),
                                  dcc.Graph(
                                      id='cases-per-million',
                                      figure=visu.total_cases_mil(countries.pca_revenue())
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
                                      figure=visu.new_cases_smooth_mil(countries.pca_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Mortes totais por país"),
                                  dcc.Graph(
                                      id='total-deaths',
                                      figure=visu.total_deaths(countries.pca_revenue())
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
                                      figure=visu.total_deaths_mil(countries.pca_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                  dcc.Graph(
                                      id='new-deaths-smooth',
                                      figure=visu.new_deaths_smooth_mil(countries.pca_revenue())
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
                                      figure=visu.gdp(countries.pca_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2('''IDH -
                                           o IDH mede a qualidade de vida em um país'''),
                                  dcc.Graph(
                                      id='hd-index',
                                      figure=visu.hdi(countries.pca_revenue())
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
                                      figure=visu.gini(countries.pca_revenue())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ), justify="center", className="g-5"
                      )], fluid=True
                  )]
    )
    return dim_red_page_pca

def dim_red_page_pca_sick():
    dim_red_page_pca_sick = html.Div(
        children=[views.navbar, views.landing_text,
                  dbc.Container(children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H1("Redução de dimensionalidade com relação à comorbidades"),
                              html.H3('''Utilizamos PCA + KMeans para agrupar os dados relacionados a proporção de diabéticos,
                                         proporção de fumantes entre homens e entre mulheres, número de leitos
                                         de hospital por mil habitantes e proporção de doenças cardiovasculares..''',
                                      className="text-muted"),

                              dcc.Graph(
                                  id='renda_kmeans',
                                  figure=visu.dim_red_kmeans(gp_clusters.sickness(), 'comorb', 'pca')
                              )], xs=11, sm=11, md=8, lg=8
                          )], justify="center", className="g-5, text-center"
                      ),
                      dbc.Row(children=[
                          dbc.Col(
                              html.Div(
                                  children=[
                                      html.H2("Total de casos"),
                                      dcc.Graph(
                                          id='cases',
                                          figure=visu.total_cases(countries.pca_sickness())
                                      )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Total de casos por milhão de habitantes"),
                                  dcc.Graph(
                                      id='cases-per-million',
                                      figure=visu.total_cases_mil(countries.pca_sickness())
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
                                      figure=visu.new_cases_smooth_mil(countries.pca_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Mortes totais por país"),
                                  dcc.Graph(
                                      id='total-deaths',
                                      figure=visu.total_deaths(countries.pca_sickness())
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
                                      figure=visu.total_deaths_mil(countries.pca_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2("Média móvel de mortes dos últimos 7 dias por milhão de habitantes"),
                                  dcc.Graph(
                                      id='new-deaths-smooth',
                                      figure=visu.new_deaths_smooth_mil(countries.pca_sickness())
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
                                      figure=visu.gdp(countries.pca_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ),
                          dbc.Col(
                              html.Div(children=[
                                  html.H2('''IDH -
                                           o IDH mede a qualidade de vida em um país'''),
                                  dcc.Graph(
                                      id='hd-index',
                                      figure=visu.hdi(countries.pca_sickness())
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
                                      figure=visu.gini(countries.pca_sickness())
                                  )], className="p-4"
                              ), xs=11, sm=11, md=6, lg=6
                          ), justify="center", className="g-5"
                      )], fluid=True
                  )]
    )
    return dim_red_page_pca_sick