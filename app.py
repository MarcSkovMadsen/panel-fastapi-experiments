import panel as pn

pn.extension()


slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
pn.panel(slider.rx() * '⭐').servable()