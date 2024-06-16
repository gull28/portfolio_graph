import plotly
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


import plotly.graph_objs as go
import pandas as pd

def accountToDict(account):
    return {
        'id': account.id,
        'blocked': account.blocked,
        'free': account.free,
        'invested': account.invested,
        'pie_cash': account.pie_cash,
        'result': account.result,
        'total': account.total,
        'timestamp': account.timestamp
    }

def generateAccountGraph(accountHistoryData):
    accountHistoryData = [accountToDict(account) for account in accountHistoryData]
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
    print(accountHistory)
    for account in accountHistory:
        print("zaza" , account)
    accountHistory['timestamp'] = pd.to_datetime(accountHistory['timestamp'])
    accountHistory['total'] = accountHistory['total'].astype(float)
    print(accountHistory['timestamp'])
    accountHistory = accountHistory.sort_values(by='timestamp')
    
    fig = go.Figure()


    
    fig.add_trace(go.Scatter(
        x=accountHistory['timestamp'],
        y=accountHistory['total'],
        mode='lines', 
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
