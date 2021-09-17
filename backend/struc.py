from pywebio.session import set_env, download
from pywebio.input import textarea
from pywebio.output import put_markdown, put_buttons
from pywebio.platform.tornado_http import start_server
from pywebio.pin import *

import argparse

def show_main_menu():
#TODO First set of quickly available charts
#       Positional Comparisons, Raw Stats Presentations, PPR stats, Charts to go along with those
#       QB Heat Maps
#       Team Tiers

#TODO Implement Python code textarea (runnable)
   #show_python_editor()
   #TODO include inserts for code area (Pre-made charting funcitons)
    return

def show_python_editor():
    # Python Editor Default
    set_env(output_animation=False)

    put_markdown("""# Markdown Live Preview
    ## Write your Markdown
    """, lstrip=True)
    textarea('md_text', rows=18, code={'mode': 'python'})

    put_buttons(['Download content'], lambda _: download('saved.py', pin.md_text.encode('utf8')), small=True)

    put_markdown('## Preview')
    while True:
        change_detail = pin_wait_change('md_text')
        with use_scope('md', clear=True):
            put_markdown(change_detail['value'], sanitize=False)
