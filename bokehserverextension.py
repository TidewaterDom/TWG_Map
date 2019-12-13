from subprocess import Popen
def load_jupyter_server_extension(nbapp):
    """serve the bokeh_map directory with bokeh server"""
    Popen(["bokeh", "serve", "bokeh_map", "--allow-websocket-origin=*"])
