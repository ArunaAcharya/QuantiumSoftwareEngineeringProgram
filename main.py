import pandas as pd
import dash
from dash import dcc, html
import os
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt



csv_files= os.path.abspath("data/")
file_list= os.listdir(csv_files)



# df= pd.concat([pd.read_csv(f"data/{file}") for file in file_list], ignore_index=True)
# df= df.query("product == 'pink morsel' ")
# df['date']= pd.to_datetime(df['date'], format="%Y-%m")
# df.sort_values('date',inplace=True)
df= pd.read_csv("pinkmorsel_data.csv")

app= dash.Dash(__name__)
# plt.figure(figsize=(14, 8), dpi=200)
#     plt.title("Total number of sales over time")
#     ax1= plt.gca()
#     ax2= ax1.twinx()
#
#     ax1.grid(color= "grey")
#     ax1.plot(df['date'],
#              df['quantity'],
#              color= 'skyblue',
#              linewidth= 3)
#     ax2.plot(df['date'],
#              df['price'],
#              color= 'crimson',
#              linewidth= 2)
#     plt.show()
def pinkmorsell_sell():
    fig= go.Figure([go.Scatter(x= df['date'], y= df['sales'],
                    line=dict(color='crimson',
                              width= 4),
                               name='Pink Morsel')
                    ])
    fig.update_layout(title='Pink Morsel sell over time',
                      xaxis_title= "Dates",
                      yaxis_title= 'sales'
                      )
    return fig
app.layout= html.Div(
    id= 'parent',
    children=[
        html.H1(id="H1", children="Pink Morcel Analytics",style={"textAlign":"center"}),
        html.P(children= "Analyze the sales of pink morsel candy sold in the date between 2018 febrouary 6 to 2018 june 10 "),
        dcc.Graph(
            id= 'line_plot',
            figure= pinkmorsell_sell()
            # figure= {
            #
            #     "data":[
            #         {
            #             "x": df['date'],
            #             "y":df['quantity'],
            #
            #
            #
            #         },
            #     ],
            #     "layout": {"title": "Sales of Pink Morsel in 2018"}
            # },
        ),
        dcc.Graph(
            figure={
                "data":[
                    {
                        "x":df['date'],
                        "y":df['price'],
                    }
                ],
                "layout":{"title":"Pink Morcel candy sold"},
            }
        ),

    ]
)

if __name__ =="__main__":
    app.run_server(debug= True)