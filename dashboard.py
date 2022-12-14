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
                          for x in sorted(df.year.unique())] + [{'label': 'Alle Jahre', 'value': 'all_values'}],
                 value='all_values'
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
                          for x in sorted(df.artist.unique())] + [{'label': 'Alle Künstler', 'value': 'all_values'}],
                         value='Drake')
        ]
                ,width=3)
    ]),
    dbc.Row(
        [
        dbc.Col([
            html.Label('Auswahl der Künstler'),
            dcc.Dropdown(id='value-choice',
                options=[
                    {'label': 'Energy', 'value': 'nrgy'},
                    {'label': 'Liveness', 'value': 'liv'},
                    {'label': 'Dancability', 'value': 'dnce'},
                    {'label': 'Valence', 'value': 'val'},
                    {'label': 'Durability', 'value': 'dur'},
                    {'label': 'Acousticness', 'value': 'acous'},
                    {'label': 'Speech', 'value': 'spch'},
                    {'label': 'Popularity', 'value': 'pop'}],
                value='pop')
            ],width=3)
    ]),
    dbc.Row(
        [
        dbc.Col([
            #einfügen der 1.Grafik
            html.Label('Balkendiagramm'),
            dcc.Graph(id='bar', figure={})]
                )]),

        dbc.Col([
                #einfügen der 2.Grafik
                html.Label('Streudiagramm'),
                dcc.Graph(id='scatter', figure={})]),

        dbc.Col([
                #einfügen der 3.Grafik
                html.Label('Liniendiagramm'),
                dcc.Graph(id='line_chart', figure={})]),

        dbc.Col([
                #einfügen der 4.Grafik
                html.Label('Spiderdiagramm'),
                dcc.Graph(id='spider', figure={})])

    ])
#ende des Designblockes

#callback einbauen
@app.callback(
    [Output(component_id='bar', component_property='figure'),
    Output(component_id='scatter', component_property='figure'),
    Output(component_id='line_chart', component_property='figure'),
    Output(component_id='spider', component_property='figure')],
    [Input(component_id='year-choice', component_property='value'),
    Input(component_id='artist-choice', component_property='value'),
    Input(component_id='value-choice', component_property='value')]
)

def update(value_year, value_artist, value_value):
    dff = df.copy()
    # Filterwert für Jahre auswerten
    if value_year == 'all_values':
        print("all")
    else:
        dff = df[df.year == value_year]

    # Filterwert für Künstler auswerten
    if value_artist == 'all_values':
        print("all artists")
    else:
        dff = df[df.artist == value_artist]

    # Plotly Diagramme
    bar = px.bar(data_frame=dff, x='title', y=value_value #,
    #title="Songs von "+value_artist+" im Jahr "+value_year+", verglichen anhand "+value_value
                    )
    scatter = px.scatter(data_frame=dff, x="title", y=value_value)

    line_chart = px.line(dff, x="year", y=value_value)

    # Spider-Diagramm für 2. Zeile (Prototyp)
    dff = pd.DataFrame(dict(
        r=[df["pop"][1], df["spch"][1], df["dnce"][1], df["nrgy"][1], df["acous"][1], df["val"][1], df["live"][1]],
        theta=['Popularity', 'Speech', 'Danceability','Energy', 'acousticness', 'Valence', "Livliness"]))

    spider = px.line_polar(dff, r='r', theta='theta', line_close=True)

    return bar, scatter, line_chart, spider

if __name__ == '__main__':
    app.run_server()
