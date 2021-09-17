from pywebio.session import set_env
import pywebio.input 
from pywebio.output import put_markdown
from pywebio.platform.tornado_http import start_server
import argparse

def app():
    set_env(title="NFL-data")
    put_markdown("<h2>A Python implementation of popular NFL data tools</h2>")
    put_markdown("More will be coming soon..... ")
    put_markdown("[For more information or additional insight](mailto:colby.sawyer17@gmail.com)")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(app, port=args.port)



