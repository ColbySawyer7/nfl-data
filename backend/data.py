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


def compare_players(data, player_name1, player_name2):
    # ============================================================
    # compare_players
    # ============================================================
    # param: player_name[1-2] : players name; type: str (strict)
    #        data: whole current dataset; type: dataframe (strict)
    # output: dataframe (both players in same dataframe)
    # ============================================================
    #Fetch Players data
    player1 = get_player_data(player_name1, data)
    #print(gaskin)
    player2 = get_player_data(player_name2, data)
    #print(zeke)
    return pd.concat([player1, player2], axis=0)

def get_player_data(data, player_name):
    # ============================================================
    # get
    # ============================================================
    # param: player_name: players name; type str (strict)
    #        data: whole current dataframe: type dataframe (strict)
    # output: dataframe (player dataframe)
    # ============================================================
    #Fetch Players data
    return data.loc[data['player_name'] == player_name]

def printBarChart(data, category, title):
    fig = px.bar(data, x='player_name', y=category, color='player_name', title = title)
    return fig

def printLineChart(data, category, title):
    fig = px.line(data, x='week', y=category, color ='player_name', markers=True, title = title)
    return fig
