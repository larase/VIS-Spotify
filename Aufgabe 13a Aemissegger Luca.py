#importieren 
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output

#Datenbearbeitung mit panda
df = pd.read_csv('https://raw.githubusercontent.com/elyesmanai/Data-Science-Datasets/main/EDA%20-%20Spotify%20Top10%202010%20-%202019.csv')


#gestalten der App
app=dash.Dash(__name__)
app.layout= html.Div([
    html.H1('Aufgabe 13a/Anzahl von Top Hits nach Artist'),
    dcc.Dropdown(id='year-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted (df.year.unique())],
                 value='2010'
                 ),
    
    dcc.Graph(id='my-graph',figure={})
    ])

#callback einbauen
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='year-choice', component_property='value')
    )
def anpassen(value_year):
    dff = df[df.year==value_year]
    figure=px.bar(data_frame=dff, x='artist', y='year')
    return figure
if __name__ =='__main__':
    app.run_server()
