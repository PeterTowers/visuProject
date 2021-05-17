import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from view import views
import src.country_clusters as countries
import src.visualizations as visu


def page_not_found(pathname):
    page = html.Div(
        children=[views.navbar,
                  html.Section(
                      html.Div(
                          html.Div(
                              html.Div(children=[
                                  html.H1("Erro 404: Página não encontrada \U0001F615",
                                          className="display-3 text-danger"),
                                  html.P('''Os hamsters que fazem a magia da internet acontecer não encontraram
                                                                        esse caminho:''',
                                         className="text-muted",
                                         style={'font-size': 'large'}),
                                  html.P(f"{pathname}",
                                         className="text-warning",
                                         style={'font-size': 'large'}),
                                  html.P("Mas fique com esse gif para não perder a viagem:",
                                         className="text-muted",
                                         style={'font-size': 'large'}
                                         ),
                                  html.Img(src="https://media1.tenor.com/images/664132cc68eb5ed11cda3c9b5f24ad3d/tenor.gif?itemid=21293093")
                              ],
                                  className="col-lg-8 col-md-8 mx-auto"
                              ),
                              className="row py-lg-5"
                          ),
                          className="py-5 text-center container"
                      )
                  )]
    )
    return page