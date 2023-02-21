#import chart_studio.plotly as py
import pandas as pd
#import plotly.io as pio
#pio.renderers.default='browser'
from plotly.offline import plot
import plotly.graph_objs as go

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

df = pd.read_csv('FulaStats.csv', encoding = 'unicode_escape')
df.head()

data = dict(type='choropleth',
            colorscale = 'Turbo',
            locations = df['Country'],
            z = df['Total'],
            locationmode = 'country names',
            text = df['Distribution'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"People"}
            ) 

layout = dict(title = 'Fula speakers by country',
              geo = dict(scope='africa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )

choromap = go.Figure(data = [data],layout = layout)

plot(choromap)

