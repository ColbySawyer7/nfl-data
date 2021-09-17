from numpy.lib.function_base import median
import nfl_data_py as nfl
from pywebio.input import select
from pywebio.session import set_env
from pywebio.output import put_markdown, put_html, put_column, put_row, popup
from pywebio.platform.tornado_http import start_server
import base64
import pandas as pd
import plotly.express as px
import numpy as np
from bs4 import BeautifulSoup
import argparse

def getCurrentLeader(data):
    gaskin_yds = data['rushing_yards'].loc[data['player_name'] == 'M.Gaskin'].values[0]
    #print(gaskin_yds)
    zeke_yds = data['rushing_yards'].loc[data['player_name'] == 'E.Elliott'].values[0]
    #print(zeke_yds)
    if gaskin_yds > zeke_yds:
        data_uri = base64.b64encode(open('imgs/gaskin.png', 'rb').read()).decode('utf-8')
    else:
        data_uri = base64.b64encode(open('imgs/zeke.png', 'rb').read()).decode('utf-8')

    img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
    return img_tag

def getPlayerData(name, year_data):
    return year_data.loc[year_data['player_name'] == name]

def printBarChart(data, title="Total Rushing Yards 2021"):
    fig = px.bar(data, x='player_name', y='rushing_yards', color='player_name', title = title)
    return fig

def printLineChart(data):
    fig = px.line(data, x='week', y='rushing_yards', color ='player_name', markers=True, title = 'Weekly Rushing Yards 2021')
    return fig
