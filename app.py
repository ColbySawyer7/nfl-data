from pywebio.session import set_env
import pywebio.input 
from pywebio.output import *
from pywebio.session import *
from pywebio.platform.tornado_http import start_server
import argparse
import asyncio

from backend.struc import show_main_menu, show_python_editor

def app():
    set_env(title="NFL-data")
    put_markdown("""# A Python implementation of popular NFL data tools
        More will be coming soon.....
    """)
    show_main_menu()
    #show_python_editor()
    dev_notes()

def dev_notes():
    # Add Developement Notes (notably the proper nods)
    put_html('<img src="https://media.giphy.com/media/xUPOqo6E1XvWXwlCyQ/giphy.gif" alt="Thats all folks"  width="250" />')
    put_markdown("""## Developer Notes
        ### Recognition
        Special thanks to [cooperdff](https://github.com/cooperdff) for the great python library, as well as [Ben Baldwin](https://twitter.com/benbbaldwin), 
        [Sebastian Carl](https://twitter.com/mrcaseb), and [Lee Sharpe](https://twitter.com/LeeSharpeNFL) for making this data freely available and easy to access.
        ### Contrib
        Code is available Open-Source (GPLv3) [here](https://github.com/ColbySawyer7/nfl-data), please open issues for discussion prior to changes
        ### Contact
        For more information or any general inquiry feel free to [Reach out](http://colby-sawyer.com)
    """, lstrip=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(app, port=args.port)



