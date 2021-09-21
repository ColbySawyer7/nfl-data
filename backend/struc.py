from pywebio.session import set_env, download
from pywebio.input import *
from pywebio.output import *
from pywebio.platform.tornado_http import start_server
from pywebio.pin import *

import requests
from io import BytesIO
import pandas as pd
import argparse

from backend.constant import YEARS 
from backend.data import get_all_team_data, get_pbp_data, get_year_data, get_all_data, get_player_data

from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import stats
import seaborn as sns

def show_main_menu():
    #TODO First set of quickly available charts
    #       Positional Comparisons, Raw Stats Presentations, PPR stats, Charts to go along with those
    #       QB Heat Maps
    #       Team Tiers
    #options =  ['Single Player Stats','Player Comparison', 'Team Tier Chart']
    data = get_year_data(2021)
    options =  ['Single Player Stats']
    put_input('menu',input_group(inputs=[actions('Common_Tools', options)]))
    if pin.menu == options[0]:
        show_single_player_stats(data)

def show_team_tier_chart():
    data = get_pbp_data([2021])
    epa_df = pd.DataFrame({
    'offense_epa': data.groupby('posteam')['epa'].sum(),
    'offense_plays': data['posteam'].value_counts(),
    'offense_yards': data.groupby('posteam')['yards_gained'].sum(), 
    })

    epa_df['offense_epa/play'] = epa_df['offense_epa'] / epa_df['offense_plays']

    epa_df.sort_values(by='offense_epa/play', ascending=False).head()

    plt.style.use('ggplot')
    plt.rcParams["font.family"] = "Ubuntu"

    x = epa_df['offense_epa/play'].values
    y = epa_df['defense_epa/play'].values

    fig, ax = plt.subplots(figsize=(20, 15))

    ax.grid(alpha=0.5)
    # plot a vertical and horixontal line to create separate quadrants
    ax.vlines(np.mean(x), y.min() - 0.05, y.max() + 0.05, color='#fcc331', alpha=0.7, lw=4, linestyles='dashed')
    ax.hlines(np.mean(y), x.min() - 0.05, x.max() + 0.05, color='#fcc331', alpha=0.7, lw=4, linestyles='dashed')
    ax.set_ylim(y.min() - 0.05, y.max() + 0.05)
    ax.set_xlim(x.min() - 0.05, x.max() + 0.05)
    ax.set_xlabel('Offense EPA/play', fontsize=20)
    ax.set_ylabel('Defense EPA/play', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    annot_styles = {
        'bbox': {'boxstyle': 'round,pad=0.5', 'facecolor': 'none', 'edgecolor':'#fcc331'},
        'fontsize': 20,
        'color': '#202f52'
    }

    # annotate the quadrants
    ax.annotate('Good offense, good defense', xy=(x.max() - 0.06, y.min() - 0.02), **annot_styles)
    ax.annotate('Bad offense, good defense', xy=(x.min(), y.min() - 0.02), **annot_styles)
    ax.annotate('Good offense, bad defense', xy=(x.max() - 0.06, y.max() + 0.02), **annot_styles)
    ax.annotate('Bad offense, bad defense', xy=(x.min(), y.max() + 0.02), **annot_styles)

    team_colors = pd.read_csv('https://raw.githubusercontent.com/guga31bb/nflfastR-data/master/teams_colors_logos.csv')

    # annotate the points with team logos
    for idx, row in epa_df.iterrows():
        offense_epa = row['offense_epa/play']
        defense_epa = row['defense_epa/play']
        logo_src = team_colors[team_colors['team_abbr'] == idx]['team_logo_wikipedia'].values[0]
        res = requests.get(logo_src)
        img = plt.imread(BytesIO(res.content))
        ax.imshow(img, extent=[row['offense_epa/play']-0.0085, row['offense_epa/play']+0.0085, row['defense_epa/play']-0.00725, row['defense_epa/play']+0.00725], aspect='auto', zorder=1000)

    ax.set_title('Offense EPA and Defense EPA', fontsize=20)

    return get_all_team_data()

def show_player_comparison_menu(data, years=YEARS):
    players = data['player_name'].tolist()
    title = 'Player Stats: '
    popup(title,[
            put_text('Hello')
        ], size='large')
    return

def show_single_player_stats(data):
    players = data['player_name'].tolist()
    player_name = select('Player', players)
    available_weeks = list(set(data['week'].tolist()))
    available_weeks.insert(0,'Total')
    week = select('Week', available_weeks)
    title = 'Player Stats: ' + player_name
    if week == 'Total':
        week = None
    popup(title,[
            put_markdown(get_player_data(data,player_name, week, removeZeros=True).transpose().to_markdown())
        ], size='large')
    return

def show_ppr_by_week(data):
    players = data['player_name'].tolist()
    player_name = select('Player', players)
    available_weeks.insert(0,'Total')
    week = select('Week', available_weeks)
    title = player_name + 'PPR Output'
    popup(title,[
            put_markdown(get_player_data(data,player_name, week, removeZeros=True).transpose().to_markdown())
        ], size='large')
    return 

def show_player_charts_menu(data):
    title = 'Common Player Charts'
    options = ['PPR/Week Line']
    
    return 

def show_python_editor():
    # Python Editor Default
        put_markdown("""# Python Playground
        ## Write your own implementation of our functions
        """, lstrip=True)

        options_code = [{"label":'Run Code',"value":'submit',"type":'submit'},
                        {"label":'Reset',"value":'cancel',"type":'cancel'},
                        {"label":'Run Code',"value":'submit',"type":'submit'}]
        options_help =['Import basic line graph', 'Import basic bar chart', 'Import basic year data']

        inputs = put_input([
            textarea('Python Code Edit', rows=10, code={'theme':'dracula','mode': 'python'}, value='import something\n# Write your python code', name='code'),
            actions(buttons=options_code, name='actions_code'),
            actions('Helpful Code', buttons=options_help, name='actions_help'),
            put_buttons(dict(value=['Continue'], color='succcess'), onclick=set_contin())
        ])
        put_markdown("Your code:\n '''python\n%s\n'''" % code)
        put_buttons(['Download content'], lambda _: download('saved.py', pin.code.encode('utf8')), small=True)

def set_panda_format():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)
    return