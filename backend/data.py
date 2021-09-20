from numpy.lib.function_base import median
import nfl_data_py as nfl
from pywebio.input import select
from pywebio.session import set_env
from pywebio.output import put_markdown, put_html, put_column, put_row, popup
from pywebio.platform.tornado_http import start_server

from backend.constant import YEARS

import base64
import pandas as pd
import plotly.express as px
import numpy as np
from bs4 import BeautifulSoup
import argparse


#TODO clean up the documentation

def get_pbp_data(year=2021):
    return nfl.import_pbp_data(year)

def get_all_team_data():
    return nfl.import_team_desc()

def get_all_data():
    return nfl.import_weekly_data(YEARS, downcast=True)

def get_year_data(year):
    return nfl.import_weekly_data([year], downcast=True)

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

def get_player_data(data, player_name, week=None, removeZeros=True):
    # ============================================================
    # get_player_data
    # ============================================================
    # param: player_name: players name; type str (strict)
    #        data: whole current dataframe: type dataframe (strict)
    # output: dataframe (player dataframe)
    # ============================================================
    #Fetch Players data
    player = data.loc[data['player_name'] == player_name]
    if not removeZeros:
        if week is not None:
            player = player.loc[player['week'] == week]
    else:
        player = player.loc[:, (player != 0).any(axis=0)]
        if week is not None:
            player = player.loc[player['week'] == week]

    return player

def print_bar_chart(data, category, title):
    fig = px.bar(data, x='player_name', y=category, color='player_name', title = title)
    return fig

def print_line_chart(data, category, title):
    fig = px.line(data, x='week', y=category, color ='player_name', markers=True, title = title)
    return fig
