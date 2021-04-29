import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Load CSV file from Datasets folder

# Police department fiscal spending from 1977-2017 but trimmed to 1977-2015
df1 = pd.read_csv('Datasets/Police dep fisc_full_dataset_2017_update.csv')
df1.groupby(['department_name', 'year', 'Nominal_Total_100k', 'ORI'])
df1.reset_index(inplace=True)

# Crime rates for cities trimmed to match the police department.csv
df2 = pd.read_csv('Datasets/City Crime reports ucr_crime_1975_2015.csv')
df2.groupby(['department_name', 'year', 'violent_per_100k', 'ORI'])
df2.reset_index(inplace=True)

# bootstrap theme simplex below
# https://bootswatch.com/simplex/
app = dash.Dash(external_stylesheets=[dbc.themes.SIMPLEX])

cityNames = ["AZ: Mesa", "AZ: Phoenix", "AZ: Tucson", "CA: Oakland", "CA: Fresno", "CA: Long Beach", "CA: Los Angeles",
             "CA: Sacramento", "CA: San Diego", "CA: San Francisco", "CA: San Jose", "CO: Aurora", "CO: Denver",
             "DC: Washington", "FL: Miami", "FL: Jacksonville", "FL: Tampa", "FL: Orlando", "GA: Atlanta",
             "IL: Chicago", "IN: Indianapolis", "KS: Wichita", "KY: Louisville", "LA: New Orleans", "MA: Boston",
             "MD: Baltimore", "MI: Detroit", "MN: Minneapolis", "MO: Kansas City", "NE: Omaha", "NC: Charlotte",
             "NC: Raleigh", "NM: Albuquerque", "NV: Las Vegas", "NY: Buffalo", "NY: New York", "OH: Cincinnati",
             "OH: Cleveland", "OH: Columbus", "OK: Oklahoma", "OK: Tulsa", "OR: Portland", "PA: Philadelphia",
             "PA: Pittsburgh", "TN: Nashville", "TN: Memphis", "TX: El Paso", "TX: Arlington", "TX: Austin",
             "TX: Dallas", "TX: Houston", "TX: San Antonio", "UT: Salt Lake City", "VA: Virginia Beach", "WA: Seattle",
             "WI: Milwaukee", "National"]

# Multi Line Chart

multiline_df = df1[df1['city_name'] == cityNames[0]]

multiline_df2 = df2[df2['city_name'] == cityNames[0]]

# Content for first graph Police Department and Crime Rates
trace1_multiline = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_Total_100k'], mode='lines',
                              name='Police department nominal')
trace2_multiline = go.Scatter(x=multiline_df2['year'], y=multiline_df2['violent_per_100k'], mode='lines',
                              name='Violent Crimes')
trace3_multiline = go.Scatter(x=multiline_df2['year'], y=multiline_df2['homs_per_100k'], mode='lines',
                              name='Homicides')
trace4_multiline = go.Scatter(x=multiline_df2['year'], y=multiline_df2['rape_per_100k'], mode='lines',
                              name='Rapes')
trace5_multiline = go.Scatter(x=multiline_df2['year'], y=multiline_df2['rob_per_100k'], mode='lines',
                              name='Robberies')
trace6_multiline = go.Scatter(x=multiline_df2['year'], y=multiline_df2['agg_ass_per_100k'], mode='lines',
                              name='Aggregated Assaults')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline, trace5_multiline, trace6_multiline]

# Content for 2nd Graph
trace1_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_police'], mode='lines',
                               name='Police department')
trace2_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_fire'], mode='lines',
                               name='Fire department')
trace3_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_education'], mode='lines',
                               name='Education')
trace4_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_welfare'], mode='lines',
                               name='Public Welfare')
trace5_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_hospital'], mode='lines',
                               name='Hospital')
trace6_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_health'], mode='lines',
                               name='Health')
trace7_multiline2 = go.Scatter(x=multiline_df['year'], y=multiline_df['Nominal_per_cap_housing'], mode='lines',
                               name='Housing')
data_multiline2 = [trace1_multiline2, trace2_multiline2, trace3_multiline2, trace4_multiline2,
                   trace5_multiline2, trace6_multiline2, trace7_multiline2]

# Layout
app.title = "The Budget Hawk"  # Names the web page in the browser to "The Budget Hawk"

# creates content for web page
# creates a navbar on top of the page
navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url("hawkLogo3-1.jpg"), height="50px")),
                    dbc.Col(dbc.NavbarBrand("The Budget Hawk", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            # brand link
            href="/",
        ),
        html.Div(
            dbc.Row(
                [  # Scrolls to respective chart on web page
                    dbc.NavItem(dbc.NavLink("Police Department Funding and Crime Rates", href="#Tracker1",
                                            external_link=True)),
                    dbc.NavItem(dbc.NavLink("Police Department Funding vs Other Services", href="#Tracker2",
                                            external_link=True)),
                    dbc.NavItem(dbc.NavLink("Dataset Sources", href="#Team",
                                            external_link=True)),
                ],
                align="center",
                style={"list-style": "none"}
            ),
            style={"padding-left": "40px"},
        ),
    ],
    # Navbar styling
    style={"padding-top": "20px"},
    color="light",
    light=True,
    className="sticky-top"
)

# creates intro written by Kylee in the proposal explaining the situation
introContent = dbc.Container(
    children=[
        html.H3("The Budget Hawk: A Simplistic Police Department Funding Tracker", style={"color": "#d9230f"}),
        html.P(
            "Recently the media has been plagued with reactions and analyses of police actions against suspects and "
            "other civilians. The outrage by the public called for the defunding of police departments as they were "
            "deemed unnecessary or excessive in how they protected communities. The ways in which police have handled "
            "past cases varies, but it heavily relies not only on the personnel they employ, but also the budget "
            "given to them. Higher budgets and costs are mainly for those departments who are in high crime-ridden "
            "areas where there is a huge need for resources for police officers to use to protect the general public. ",
            style={"padding": "10px"}
        ),
        html.P(
            "This raises the question of how much is actually necessary for police departments to be able to "
            "effectively protect the people and enforce laws? It’s given that when there is a lot of crime, "
            "a lot of money is needed to sort out and solve these problems; however, what happens when crime rates go "
            "back down? How can we tell how the budget should be adjusted when the crime rates seem to dwindle? There "
            "is a need for regulation and efficiency in the budgets provided to police departments, "
            "so the departments can protect the community without putting a strain on the rest of the government "
            "budgets needed for regulation of the community. ",
            style={"padding": " 0px 10px"}
        ),
    ],
    style={"padding": "40px 0px", "text-align": "center"},
)

# Page main content. Contains the graphs and other things
mainContent = dbc.Container(children=[
    html.Hr(),  # top border
    # h3 header after border
    html.H3("Police Department and Crime Rates Tracker",
            style={'color': '#d9230f', "padding": "10px"}, id="Tracker1"),
    html.Div(
        'This multiline chart tracks police department funding and violent crimes, which consist of homicides, rapes, '
        'robberies, and '
        'aggregated assaults reports for the respective city or on the national level.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Police Department Funding vs Crime Rates From 1977-2015',
                      xaxis={'title': 'Year'}, yaxis={'title': 'Per 100k Population'})
              }
              ),
    html.Div('Please select a city', style={'color': '#d9230f', 'margin': '10px'}),  # Text before dropdown
    dcc.Dropdown(
        id='select-city_name',
        options=[
            {'label': cityNames[0], 'value': cityNames[0]},
            {'label': cityNames[1], 'value': cityNames[1]},
            {'label': cityNames[2], 'value': cityNames[2]},
            {'label': cityNames[3], 'value': cityNames[3]},
            {'label': cityNames[4], 'value': cityNames[4]},
            {'label': cityNames[5], 'value': cityNames[5]},
            {'label': cityNames[6], 'value': cityNames[6]},
            {'label': cityNames[7], 'value': cityNames[7]},
            {'label': cityNames[8], 'value': cityNames[8]},
            {'label': cityNames[9], 'value': cityNames[9]},
            {'label': cityNames[10], 'value': cityNames[10]},
            {'label': cityNames[11], 'value': cityNames[11]},
            {'label': cityNames[12], 'value': cityNames[12]},
            {'label': cityNames[13], 'value': cityNames[13]},
            {'label': cityNames[14], 'value': cityNames[14]},
            {'label': cityNames[15], 'value': cityNames[15]},
            {'label': cityNames[16], 'value': cityNames[16]},
            {'label': cityNames[17], 'value': cityNames[17]},
            {'label': cityNames[18], 'value': cityNames[18]},
            {'label': cityNames[19], 'value': cityNames[19]},
            {'label': cityNames[20], 'value': cityNames[20]},
            {'label': cityNames[21], 'value': cityNames[21]},
            {'label': cityNames[22], 'value': cityNames[22]},
            {'label': cityNames[23], 'value': cityNames[23]},
            {'label': cityNames[24], 'value': cityNames[24]},
            {'label': cityNames[25], 'value': cityNames[25]},
            {'label': cityNames[26], 'value': cityNames[26]},
            {'label': cityNames[27], 'value': cityNames[27]},
            {'label': cityNames[28], 'value': cityNames[28]},
            {'label': cityNames[29], 'value': cityNames[29]},
            {'label': cityNames[30], 'value': cityNames[30]},
            {'label': cityNames[31], 'value': cityNames[31]},
            {'label': cityNames[32], 'value': cityNames[32]},
            {'label': cityNames[33], 'value': cityNames[33]},
            {'label': cityNames[34], 'value': cityNames[34]},
            {'label': cityNames[35], 'value': cityNames[35]},
            {'label': cityNames[36], 'value': cityNames[36]},
            {'label': cityNames[37], 'value': cityNames[37]},
            {'label': cityNames[38], 'value': cityNames[38]},
            {'label': cityNames[39], 'value': cityNames[39]},
            {'label': cityNames[40], 'value': cityNames[40]},
            {'label': cityNames[41], 'value': cityNames[41]},
            {'label': cityNames[42], 'value': cityNames[42]},
            {'label': cityNames[43], 'value': cityNames[43]},
            {'label': cityNames[44], 'value': cityNames[44]},
            {'label': cityNames[45], 'value': cityNames[45]},
            {'label': cityNames[46], 'value': cityNames[46]},
            {'label': cityNames[47], 'value': cityNames[47]},
            {'label': cityNames[48], 'value': cityNames[48]},
            {'label': cityNames[49], 'value': cityNames[49]},
            {'label': cityNames[50], 'value': cityNames[50]},
            {'label': cityNames[51], 'value': cityNames[51]},
            {'label': cityNames[52], 'value': cityNames[52]},
            {'label': cityNames[53], 'value': cityNames[53]},
            {'label': cityNames[54], 'value': cityNames[54]},
            {'label': cityNames[55], 'value': cityNames[55]},
            {'label': cityNames[56], 'value': cityNames[56]}
        ],
        value=cityNames[0]
    ),
    html.Div(
        style={"padding-bottom": "40px"}
    ),

    # 2nd graph comparing Police Department funding vs Other Departments

    # top border
    html.Hr(),
    # h3 header after border
    html.H3("Police Department Funding vs Other Services Tracker",
            style={'color': '#d9230f', "padding": "10px"}, id="Tracker2"),
    html.Div(
        'This multiline chart tracks police department, fire department, education, public welfare, '
        'hospital, health, and housing funding for the respective city or on the national level.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_multiline2,
                  'layout': go.Layout(
                      title='Police Department Funding vs Other Services From 1977-2015',
                      xaxis={'title': 'Year'}, yaxis={'title': 'Nominal Dollars Per Capita'})
              }
              ),
    html.Div('Please select a city', style={'color': '#d9230f', 'margin': '10px'}),  # Text before dropdown
    dcc.Dropdown(
        id='select-city_name2',
        options=[
            {'label': cityNames[0], 'value': cityNames[0]},
            {'label': cityNames[1], 'value': cityNames[1]},
            {'label': cityNames[2], 'value': cityNames[2]},
            {'label': cityNames[3], 'value': cityNames[3]},
            {'label': cityNames[4], 'value': cityNames[4]},
            {'label': cityNames[5], 'value': cityNames[5]},
            {'label': cityNames[6], 'value': cityNames[6]},
            {'label': cityNames[7], 'value': cityNames[7]},
            {'label': cityNames[8], 'value': cityNames[8]},
            {'label': cityNames[9], 'value': cityNames[9]},
            {'label': cityNames[10], 'value': cityNames[10]},
            {'label': cityNames[11], 'value': cityNames[11]},
            {'label': cityNames[12], 'value': cityNames[12]},
            {'label': cityNames[13], 'value': cityNames[13]},
            {'label': cityNames[14], 'value': cityNames[14]},
            {'label': cityNames[15], 'value': cityNames[15]},
            {'label': cityNames[16], 'value': cityNames[16]},
            {'label': cityNames[17], 'value': cityNames[17]},
            {'label': cityNames[18], 'value': cityNames[18]},
            {'label': cityNames[19], 'value': cityNames[19]},
            {'label': cityNames[20], 'value': cityNames[20]},
            {'label': cityNames[21], 'value': cityNames[21]},
            {'label': cityNames[22], 'value': cityNames[22]},
            {'label': cityNames[23], 'value': cityNames[23]},
            {'label': cityNames[24], 'value': cityNames[24]},
            {'label': cityNames[25], 'value': cityNames[25]},
            {'label': cityNames[26], 'value': cityNames[26]},
            {'label': cityNames[27], 'value': cityNames[27]},
            {'label': cityNames[28], 'value': cityNames[28]},
            {'label': cityNames[29], 'value': cityNames[29]},
            {'label': cityNames[30], 'value': cityNames[30]},
            {'label': cityNames[31], 'value': cityNames[31]},
            {'label': cityNames[32], 'value': cityNames[32]},
            {'label': cityNames[33], 'value': cityNames[33]},
            {'label': cityNames[34], 'value': cityNames[34]},
            {'label': cityNames[35], 'value': cityNames[35]},
            {'label': cityNames[36], 'value': cityNames[36]},
            {'label': cityNames[37], 'value': cityNames[37]},
            {'label': cityNames[38], 'value': cityNames[38]},
            {'label': cityNames[39], 'value': cityNames[39]},
            {'label': cityNames[40], 'value': cityNames[40]},
            {'label': cityNames[41], 'value': cityNames[41]},
            {'label': cityNames[42], 'value': cityNames[42]},
            {'label': cityNames[43], 'value': cityNames[43]},
            {'label': cityNames[44], 'value': cityNames[44]},
            {'label': cityNames[45], 'value': cityNames[45]},
            {'label': cityNames[46], 'value': cityNames[46]},
            {'label': cityNames[47], 'value': cityNames[47]},
            {'label': cityNames[48], 'value': cityNames[48]},
            {'label': cityNames[49], 'value': cityNames[49]},
            {'label': cityNames[50], 'value': cityNames[50]},
            {'label': cityNames[51], 'value': cityNames[51]},
            {'label': cityNames[52], 'value': cityNames[52]},
            {'label': cityNames[53], 'value': cityNames[53]},
            {'label': cityNames[54], 'value': cityNames[54]},
            {'label': cityNames[55], 'value': cityNames[55]},
            {'label': cityNames[56], 'value': cityNames[56]}
        ],
        value=cityNames[0]
    ),
],
    style={"text-align": "center", "padding-bottom": "60px"}
)

# About Development Team
footContent = dbc.Container(children=[
    html.Hr(),
    html.H3("Dataset Sources:",
            style={'color': '#d9230f', "padding": "10px"},  id="Team"),
    html.P(
        ["These are the sources utilized for the graph creation:",
         html.Br(),
         html.Br(),
         dbc.NavItem(dbc.NavLink("TheMarshallProject crime numbers for US cities from 1975-2015",
                                 href="https://github.com/themarshallproject/city-crime/blob/master/data"
                                      "/ucr_crime_1975_2015.csv")),
         "This source is the 2017 crimes reports in the United States of America directly from TheMarshallProject "
         "which pulled the numbers from the FBI. This source when paired with the fiscal spending of police "
         "departments in 2017 illustrates that police department funding increases with no correlation to the crime "
         "rates reported by the FBI.",
         html.Br(),
         html.Br(),
         dbc.NavItem(dbc.NavLink("FiSC database for police spending for US cities from 1977-2017",
                                 href="https://www.lincolninst.edu/research-data/data-toolkits/fiscally-standardized"
                                      "-cities/search-database")),
         "This source is the fiscal spending of every police department in the United States of America in 2017 from "
         "the Lincoln Institute of Land Policy. This datasets allows our group to establish what various select "
         "cities budgetary expenditures are for their police departments. When paired with the crime reports from the "
         "FBI we can establish that police department funding increases regardless of the crime rates within their "
         "policing jurisdiction.",
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         "Designed by: Austin Smith, Jack Hamilton, Kevin Hudson, Kylee Mucher"
         ]
    )
],
    style={"text-align": "center", "padding": "0px 10px 60px", "list-style": "none"}
)

# Creates the actual web page with load order of content
app.layout = html.Div([
    navbar,
    introContent,  # Intro for project
    mainContent,  # graphs
    footContent
])


# callback updating graph 1
@app.callback(Output('graph1', 'figure'),
              [Input('select-city_name', 'value')])
def update_figure(selected_city_name):
    new_multiline_df = df1[df1['city_name'] == selected_city_name]

    new_multiline_df2 = df2[df2['city_name'] == selected_city_name]

    new_trace1_multiline = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_Total_100k'],
                                      mode='lines',
                                      name='Police Department Nominal')
    new_trace2_multiline = go.Scatter(x=new_multiline_df2['year'], y=new_multiline_df2['violent_per_100k'],
                                      mode='lines',
                                      name='Violent Crimes')
    new_trace3_multiline = go.Scatter(x=new_multiline_df2['year'], y=new_multiline_df2['homs_per_100k'], mode='lines',
                                      name='Homicides')
    new_trace4_multiline = go.Scatter(x=new_multiline_df2['year'], y=new_multiline_df2['rape_per_100k'], mode='lines',
                                      name='Rapes')
    new_trace5_multiline = go.Scatter(x=new_multiline_df2['year'], y=new_multiline_df2['rob_per_100k'], mode='lines',
                                      name='Robberies')
    new_trace6_multiline = go.Scatter(x=new_multiline_df2['year'], y=new_multiline_df2['agg_ass_per_100k'],
                                      mode='lines', name='Aggregated Assaults')
    new_data_multiline = [new_trace1_multiline, new_trace2_multiline, new_trace3_multiline, new_trace4_multiline,
                          new_trace5_multiline, new_trace6_multiline]
    return {'data': new_data_multiline,
            'layout': go.Layout(title='Police Department Funding and Crime Rates From 1977-2015 ' + selected_city_name,
                                xaxis={'title': 'Year'},
                                yaxis={'title': 'Per 100k population'})}


# Group 2 callback
@app.callback(Output('graph2', 'figure'),
              [Input('select-city_name2', 'value')])
def update_figure(selected_city_name2):
    new_multiline_df = df1[df1['city_name'] == selected_city_name2]

    new_trace1_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_police'],
                                       mode='lines', name='Police department')
    new_trace2_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_fire'],
                                       mode='lines', name='Fire department')
    new_trace3_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_education'],
                                       mode='lines', name='Education')
    new_trace4_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_welfare'],
                                       mode='lines', name='Public Welfare')
    new_trace5_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_hospital'],
                                       mode='lines', name='Hospital')
    new_trace6_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_health'],
                                       mode='lines', name='Health')
    new_trace7_multiline2 = go.Scatter(x=new_multiline_df['year'], y=new_multiline_df['Nominal_per_cap_housing'],
                                       mode='lines', name='Housing')
    new_data_multiline2 = [new_trace1_multiline2, new_trace2_multiline2, new_trace3_multiline2, new_trace4_multiline2,
                           new_trace5_multiline2, new_trace6_multiline2, new_trace7_multiline2]
    return {'data': new_data_multiline2,
            'layout': go.Layout(title='Police Department Funding vs Other Services From 1977-2015 ' +
                                      selected_city_name2,
                                xaxis={'title': 'Year'},
                                yaxis={'title': 'Per Capita Nominal'})}


if __name__ == '__main__':
    app.run_server()
