# importieren
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Datenbearbeitung mit panda
df = pd.read_csv('https://raw.githubusercontent.com/elyesmanai/Data-Science-Datasets/main/EDA%20-%20Spotify%20Top10%202010%20-%202019.csv')

# gestalten der App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('welcome to hell'),
    dcc.Dropdown(id='year-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.year.unique())],
                 value='2013'
                 ),
    dcc.Dropdown(id='artist-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.artist.unique())],
                 value='Demi Lovato'
                 ),
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
                value='pop'
                 ),
    dcc.Graph(id='my-graph', figure={})
])

# callback einbauen
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='year-choice', component_property='value'),
    Input(component_id='artist-choice', component_property='value'),
    Input(component_id='value-choice', component_property='value')]
)

def update(value_year, value_artist, value_value):
    dff = df.copy()
    dff = dff[df.year == value_year]
    dff = dff[df.artist == value_artist]
    # Plotly
    figure = px.bar(data_frame=dff, x='title', y=value_value #,
    #                title="Songs von "+value_artist+" im Jahr "+value_year+", verglichen anhand "+value_value
                    )
    return figure

if __name__ == '__main__':
    app.run_server()