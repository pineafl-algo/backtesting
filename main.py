import pandas as pd 
import numpy as np 
import yfinance as yf  
import matplotlib.pyplot as plt 
import matplotlib.style 
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dash_table, dcc


msft = yf.Ticker("MSFT")
msft_data=msft.history(start='2018-01-01',end='2024-01-24')
msft_data.reset_index(inplace=True)

msft_data['Date'] = msft_data['Date'].dt.strftime('%Y/%m/%d')
plt.figure(figsize=(26,16))
plt.plot(msft_data['Close'])
fig = go.Figure([go.Scatter(x=msft_data['Date'], y=msft_data['Close'])])
fig.show()

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Data'),
    dash_table.DataTable(data=msft_data.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(msft_data, x='Date', y='Close', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)