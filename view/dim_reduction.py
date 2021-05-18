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
                  html.H1("Redução de dimensionalidade"),
                  html.H2("UMAP + KMeans"),
                  html.H3("Renda ou comorbidades"),
                  dcc.RadioItems(
                      id='hovermode',
                      labelStyle={'display': 'inline-block'},
                      options=[{'label': x, 'value': x} 
                              for x in ['Renda', 'Comorbidades']],
                      value='Renda'
                  ),
                  dcc.Graph(
                      id='renda_kmeans',
                      figure=visu.umap_kmeans_revenue(gp_clusters.revenue())
                  )
                  ]
    )
    return dim_red_page
'''
    @dim_red_page.callback(
        Output("graph", "figure"), 
        [Input("hovermode", "value")], 
        [State('graph', 'figure')]
    )
    
    def update_hovermode(mode, fig_json):
        # fig = px.Figure(fig_json)
        # fig.update_layout(hovermode=mode)
        if mode == 'Renda':
            figure=visu.umap_kmeans_revenue(gp_clusters.revenue())
            figure.update_layout()
            return figure
        else:
            figure=visu.umap_kmeans_sickness(gp_clusters.sickness())
            figure.update_layout()
            return figure
'''    
   
