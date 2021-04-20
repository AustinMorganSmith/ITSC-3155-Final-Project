import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

df1 = pd.read_csv('../Datasets/Police dep fisc_full_dataset_2017_update.csv', nrows=41)
df1['year'] = pd.to_numeric(df1['year'])
df = pd.read_csv('../Datasets/City Crime reports ucr_crime_1975_2015.csv')
df['year'] = pd.to_numeric(df['year'])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# styling the sidebar
SIDEBAR_STYLE = {
    "color": "royalblue",
    "margin-left": "250px",
    "margin-right": "250px",
    "margin-bottom": "50px",
    "background-color": "#3b3b3b",
    "align": "center",
    "text-align": "center",
}

# padding for the page content
CONTENT_STYLE = {
    "padding-left": "250px",
    "padding-right": "250px"
}

sidebar = html.Div(
    [
        html.H2("Budget Hawk"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Police Budgets and Crime rate', style={'textAlign': 'center'}),
                dcc.Graph(id='bargraph', figure=px.line(df, x='year', y=['violent_crime'], color='department_name'))
                ]
    elif pathname == "/page-1":
        return [
                html.H1('Page 1', style={'textAlign': 'center'}),
                html.Br(),
                html.P("The Budget Hawk seeks to minimize budgetary expenditures in various cities and states by "
                       "comparing police department spending against crime rates reported by the FBI. Thus, allowing "
                       "for policy makers in those cities and states to minimize and properly prioritize their budgets "
                       "if crime rates have been reliably declining."),
                html.P("Recently the media has been plagued with reactions and analyses of police actions against "
                       "suspects and other civilians. The outrage by the public called for the defunding of police "
                       "departments as they were deemed unnecessary or excessive in how they protected communities. The"
                       " ways in which police have handled past cases varies, but it heavily relies not only on the "
                       "personnel they employ, but also the budget given to them. Higher budgets and costs are mainly "
                       "for those departments who are in high crime-ridden areas where there is a huge need for "
                       "resources for police officers to use to protect the general public."),
                html.P("This raises the question of how much is actually necessary for police departments to be able to"
                       " effectively protect the people and enforce laws? It’s given that when there is a lot of crime,"
                       " a lot of money is needed to sort out and solve these problems; however, what happens when "
                       "crime rates go back down? How can we tell how the budget should be adjusted when the crime "
                       "rates seem to dwindle? There is a need for regulation and efficiency in the budgets provided "
                       "to police departments, so the departments can protect the community without putting a strain "
                       "on the rest of the government budgets needed for regulation of the community.")
                ]
    elif pathname == "/page-2":
        return [
                html.H1('Page 2',
                        style={'textAlign': 'center'}),
                ]


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
