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
                 value='2010'
                 ),
    dcc.Dropdown(id='artist-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.artist.unique())],
                 value='Drake'
                 ),
    dcc.Graph(id='my-graph', figure={})
])

# callback einbauen
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='year-choice', component_property='value'),
    Input(component_id='artist-choice', component_property='value')]
)

def update(value_year, value_artist):
    dff = df[df.year == value_year]
    dff = df[df.artist == value_artist]
    # Plotly
    figure = px.bar(data_frame=dff, x='title', y='pop',
                    title="Songs von "+value_artist+" im Jahr "+value_year)

    return figure

if __name__ == '__main__':
    app.run_server()