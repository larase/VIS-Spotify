# importieren
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
#importieren der Bootstrap komponenten
import dash_bootstrap_components as dbc

# Dateneinlesen mit panda
df = pd.read_csv('https://raw.githubusercontent.com/elyesmanai/Data-Science-Datasets/main/EDA%20-%20Spotify%20Top10%202010%20-%202019.csv')

# thema auswählen
app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])
#thema auswählen)



print(df.columns)#AUSGABE DER ZELLEN ÜBERSCHRIFTEN

# Gestalten der App
app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("Willkommen zu Unserem Prototypen des Dashboards")
       ], width=12)
    ], justify="center"),
    
#einfügen des 1.Dropdown Filters für das Jahr
    dbc.Row(
        [
        dbc.Col([
            html.Label('Jahresauswahl'),
            dcc.Dropdown(id='year-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.year.unique())],
                 value='2010'
                 ),
        ]
                ,width=3)]),
#Einfügen des 2.Dropdownfilters für den künstler
    dbc.Row(
        [
        dbc.Col([
            html.Label('Künstlerauswahl'),
            dcc.Dropdown(id='artist-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.artist.unique())],
                         value='Drake')
        ]
                ,width=3)
    ]),
    dbc.Row(
        [
        dbc.Col([
            #einfügen der 1.Grafik
            html.Label('Unsere 1. Grafik'),
            dcc.Graph(id='my-graph', figure={})]
                )]),
    
        dbc.Col([
                #einfügen der 2.Grafik
                html.Label('Unsere 2. Grafik'),
                dcc.Graph(id='my-graph2', figure={})]#leere grafik als platzhalter
                    )

    
    ])
#ende des Designblockes

#callback einbauen
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='year-choice', component_property='value'),
    Input(component_id='artist-choice', component_property='value')]
)

def update(value_year, value_artist):
    dff = df[df.year == value_year]
    dff = df[df.artist == value_artist]
    # 1..grafik erstellen
    figure = px.bar(data_frame=dff, x='title', y='pop',
                    title="Songs von "+value_artist+" im Jahr "+value_year)
    
    

    return figure

if __name__ == '__main__':
    app.run_server()