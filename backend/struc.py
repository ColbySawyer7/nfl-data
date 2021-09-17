from pywebio.session import set_env, download
from pywebio.input import textarea, input_group
from pywebio.output import put_markdown, put_buttons, put_row, put_loading
from pywebio.platform.tornado_http import start_server
from pywebio.pin import *

import argparse
from backend.constant import YEARS 
from backend.data import get_year_data, get_all_data, get_player_data


def show_main_menu():
    #TODO First set of quickly available charts
    #       Positional Comparisons, Raw Stats Presentations, PPR stats, Charts to go along with those
    #       QB Heat Maps
    #       Team Tiers
        put_loading()
        data = get_year_data(2021)
        show_player_comparison_menu(data)

def show_player_comparison_menu(data, years=YEARS):
    players = data['name'].tolist()
    put_row([
        select(label="Player 1", content=players),
        put_markdown("## vs"),
        select(label="Player 2", content=players),
    ])
    return

def show_python_editor():
    # Python Editor Default
    put_markdown("""# Python Playground
    ## Write your own implementation of our functions
    """, lstrip=True)
    textarea('py_text', rows=18, code={'theme':'dracula','mode': 'python'})
    put_buttons(['Download content'], lambda _: download('saved.py', pin.py_text.encode('utf8')), small=True)

