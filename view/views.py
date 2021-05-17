import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Dashboard visual da COVID-19", href="#", style={'font-size': 'large'})),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Técnicas utilizadas"),
             dbc.DropdownMenuItem("Agrupamento por UMAP"),
             dbc.DropdownMenuItem("Agrupamento por K-means")],
            label="Técnicas de agrupamento",
            nav=True,
        ),
        dbc.NavItem(dbc.NavLink("América do Sul", href="#")),
        dbc.NavItem(dbc.NavLink("Países nódicos", href="#")),
        dbc.NavItem(dbc.NavLink("Países desenvolvidos", href="#")),
        dbc.NavItem(dbc.NavLink("Faça seu cluster", href="#"))
    ], className="navbar bg-secondary", style={'font-size': 'medium'}
)

landing_text = html.Section(
    html.Div(
        html.Div(
            html.Div(
                children=[
                    html.H1("Dashboard visual da COVID-19", className="display-3"),
                    html.P("Texto para falar coisas.",
                           className="text-muted",
                           style={'font-size': 'large'})
                ],
                className="col-lg-8 col-md-8 mx-auto"
            ),
            className="row py-lg-5"
        ),
        className="py-5 text-center container"
    )
)