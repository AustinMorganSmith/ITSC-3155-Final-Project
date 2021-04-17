import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
dpFisc = pd.read_csv('Datasets/Police dep fisc_full_dataset_2017_update.csv', nrows=41)
dpFisc['year'] = pd.to_numeric(dpFisc['year'])
ccRep = pd.read_csv('Datasets/City Crime reports ucr_crime_1975_2015.csv', nrows=41)
ccRep['year'] = pd.to_numeric(ccRep['year'])

# Preparing data
trace1 = go.Scatter(x=dpFisc['year'], y=dpFisc['Nominal_Total_100k'], mode='lines', name='Police department nominal '
                                                                                         'per 100k')
trace2 = go.Scatter(x=ccRep['year'], y=ccRep['violent_per_100k'], mode='lines', name='Violent Crimes per 100k')
trace3 = go.Scatter(x=ccRep['year'], y=ccRep['homs_per_100k'], mode='lines', name='Homicides per 100k')
trace4 = go.Scatter(x=ccRep['year'], y=ccRep['rape_per_100k'], mode='lines', name='Rapes per 100k')
trace5 = go.Scatter(x=ccRep['year'], y=ccRep['rob_per_100k'], mode='lines', name='Robberies per 100k')
trace6 = go.Scatter(x=ccRep['year'], y=ccRep['agg_ass_per_100k'], mode='lines', name='Aggregated Assaults per 100k')
data = [trace1, trace2, trace3, trace4, trace5, trace6]

# Preparing layout
layout = go.Layout(title='Test run', xaxis_title="Year",
                   yaxis_title="Per 100k City Population")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart - Copy.html')