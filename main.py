import pandas as pd
import dash
from dash import dcc, html, Input, Output
import os
import plotly.express as px
from plotly.express import line
import plotly.graph_objs as go
import matplotlib.pyplot as plt



csv_files= os.path.abspath("data/")
file_list= os.listdir(csv_files)


df= pd.read_csv("pinkmorsel_data.csv")
df= df.sort_values(by='date')
df['date']= pd.to_datetime(df['date'], format="%Y-%m")

app= dash.Dash(__name__)

app.layout= html.Div(
    id= 'parent',
    style={},
    children=[
        html.H1(id="H1", children="Pink Morsel Analytics",style={"textAlign":"center"}),
        html.P(children= "Sales of pink morsel candy over the time"),
        dcc.Graph(id='graph'),
    dcc.Checklist(
        id='checklist',
        options=['east', 'west', 'north', 'south'],
        value=['east'],
        inline=True

    ),
    ])
@app.callback(
    Output('graph','figure'),
    Input('checklist', 'value'))
def update_line_chart(regions):
    mask= df.region.isin(regions)
    fig= px.line(df[mask],
                 x='date', y='sales', color='region')
    return fig

if __name__ =="__main__":
    app.run_server(debug= True)