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
            font=dict(size=20),
            font_color="white"
        )
        fig.update_layout(
            title={
                'text': 'Account History',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'color': 'white'}
            },
            xaxis_title={
                'text': 'Date',
                'font': {'color': 'white'}
            },
            yaxis_title={
                'text': 'Value',
                'font': {'color': 'white'}
            },
            template='plotly_white',
            plot_bgcolor='black',
            paper_bgcolor='black',
            font=dict(color='white')
        )
        return fig.to_json()

    accountHistory['timestamp'] = pd.to_datetime(accountHistory['timestamp'], errors='coerce')
    accountHistory['total'] = accountHistory['total'].astype(float)
    accountHistory = accountHistory.dropna(subset=['timestamp'])
    accountHistory = accountHistory.sort_values(by='timestamp')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=accountHistory['timestamp'],
        y=accountHistory['total'],
        mode='lines',
        name='Total value',
        line=dict(color='#2596be')
    ))

    fig.update_layout(
        title={
            'text': 'Account History',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'color': 'white'}
        },
        template='plotly_white',
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white'),
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1d',
                         step='day',
                         stepmode='backward'),
                    dict(count=7,
                         label='1w',
                         step='day',
                         stepmode='backward'),
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(step='all',
                         label='All time')
                ]),
                activecolor='white',
                bgcolor='black',
                bordercolor='#2596be',
                font=dict(color='#2596be')
            ),
            type='date',
            color='white',
            showgrid=False,
            linecolor='#2596be',
            showline=False,
        ),
        yaxis=dict(
            color='white',
            showgrid=False,
            linecolor='white',
            showline=False
        ),
        legend=dict(
            font=dict(color='white'),
            bgcolor='black',
            bordercolor='#2596be'
        )
    )

    plotToJson = fig.to_json()
    
    return plotToJson
