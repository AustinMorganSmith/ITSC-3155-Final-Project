import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder

# Police department fiscal spending from 1977-2017 but trimmed to 1977-2015
df1 = pd.read_csv('Datasets/Police dep fisc_full_dataset_2017_update.csv')
df1.groupby(['department_name', 'year', 'Nominal_Total_100k', 'ORI'])
df1.reset_index(inplace=True)

# Crime rates for cities trimmed to match the police department.csv
df2 = pd.read_csv('Datasets/City Crime reports ucr_crime_1975_2015.csv')
df2.groupby(['department_name', 'year', 'violent_per_100k', 'ORI'])
df2.reset_index(inplace=True)

app = dash.Dash()

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

# Layout
app.layout = html.Div(children=[
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('The Budget Hawk', style={'color': '#df1e56'}),
    html.Div(
        'This multiline chart tracks police department funding, violent crimes, homicides, rapes, robberies, and '
        'aggregated assaults reports.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Police Department Funding vs Crime Rates From 1977-2015',
                      xaxis={'title': 'Year'}, yaxis={'title': 'Per 100k Population'})
              }
              ),
    html.Div('Please select a city', style={'color': '#ef3e18', 'margin': '10px'}),
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
    )
])


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
            'layout': go.Layout(title='Police Department Funding and Crime Rates From 1977-2015 ' + selected_city_name ,
                                xaxis={'title': 'Year'},
                                yaxis={'title': 'Per 100k population'})}


if __name__ == '__main__':
    app.run_server()
