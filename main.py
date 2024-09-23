import panel as pn

from fastapi import FastAPI, Request
from panel.io.fastapi import add_application

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    return {"Hello": "World", "root_path": request.scope.get("root_path")}

@add_application('/panel1', app=app, title='App 1')
def create_panel_app():
    slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
    return slider.rx() * '⭐'

@add_application('/panel2', app=app, title='App 2')
def create_panel_app():
    slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
    return slider.rx() * '❤️'