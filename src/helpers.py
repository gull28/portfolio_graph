import plotly
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


import plotly.graph_objs as go
import pandas as pd

def generateAccountGraph(accountHistoryData):
    accountHistory = pd.DataFrame(accountHistoryData)

    if accountHistory.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No data available",
            xref="paper", yref="paper",
            showarrow=False,
            font=dict(size=20)
        )
        fig.update_layout(
            title='Account History',
            xaxis_title='Date',
            yaxis_title='Value',
            template='plotly_white'
        )
        return fig.to_json()
        
    accountHistory['timestamp'] = pd.to_datetime(accountHistory['timestamp'])
    
    accountHistory = accountHistory.sort_values(by='timestamp')
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=accountHistory['timestamp'],
        y=accountHistory['total'],
        mode='lines+markers', 
        name='Total value'
    ))
    
    fig.update_layout(
        title='Account History',
        xaxis_title='Date',
        yaxis_title='Value',
        template='plotly_white' 
    )

    plotToJson = fig.to_json()
    
    return plotToJson
