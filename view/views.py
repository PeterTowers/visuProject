import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Dashboard visual da COVID-19", href="/", style={'font-size': 'large'})),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Técnicas utilizadas", style={'font-size': 'medium'}),
             dbc.DropdownMenuItem("Redução de dimensionalidade",
                                  href="/reducao-dim",
                                  style={'font-size': 'medium'}),
             dbc.DropdownMenuItem("Agrupamento por K-means", style={'font-size': 'medium'})],
            label="Técnicas de agrupamento",
            nav=True,
        ),
        dbc.NavItem(dbc.NavLink("América do Sul", href="/america-sul")),
        dbc.NavItem(dbc.NavLink("Países nódicos", href="/paises-nordicos")),
        dbc.NavItem(dbc.NavLink("Países desenvolvidos", href="/paises-desenvolvidos")),
        dbc.NavItem(dbc.NavLink("Faça seu cluster", href="/easter-egg"))
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