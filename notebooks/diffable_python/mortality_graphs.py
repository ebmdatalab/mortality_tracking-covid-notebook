# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import plotly.graph_objects as go
from datetime import date
import numpy as np

# +
weeks = ['3 Jan 2020', '10 Jan 2020', '17 Jan 2020', '24 Jan 2020', '31 Jan 2020', 
         '7 Feb 2020', '14 Feb 2020', '21 Feb 2020', '28 Feb 2020', '6 Mar 2020', '13 Mar 2020',
         '20 Mar 2020']
all_mortality = np.array([12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 
                          10895, 11019, 10645], 
                         dtype=np.float)
rep_deaths = np.array([2141, 2477, 2188, 1894, 1746, 1572, 1602, 1618, 1529, 1551, 1488, 1514], dtype=np.float)

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=np.multiply(rep_deaths/all_mortality, 100), fill=None,
                    mode= 'lines+markers', name='Percent of All Mortality Caused by Respiratory Disease'
                        ))

fig.update_layout(title={'text': 'Percent of All Mortality Caused by Respiratory Disease in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  xaxis_title='Week Ending Date',
                  yaxis_title='% of All Mortality',
                  yaxis_range=(0, 25), 
                  xaxis = dict(tickangle=-30))#,
                  #annotations=[dict(x='10 Jan 2020', y=14058, text='Peak All Cause Mortality', showarrow=True)])

fig.write_html("html/resp_mortality.html")
fig.show()

# +
weeks = ['3 Jan 2020', '10 Jan 2020', '17 Jan 2020', '24 Jan 2020', '31 Jan 2020', 
         '7 Feb 2020', '14 Feb 2020', '21 Feb 2020', '28 Feb 2020', '6 Mar 2020', '13 Mar 2020', 
         '20 Mar 2020']
all_mortality = [12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 10895, 11019, 10645]
five_year_mort = [12175, 13822, 13216, 12760, 12206, 11925, 11627, 11548, 11183, 11498, 11205, 10573]

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=all_mortality, fill=None,
                    mode= 'lines', name='All Cause <br> Mortality 2020'
                        ))

fig.add_trace(go.Scatter(x= weeks, y=five_year_mort, fill=None,
                    mode='lines', name='Average All Cause <br> Mortality 2015-19'
                    ))


fig.add_shape(
        # Line Vertical
        dict(
            type='line',
            x0='31 Jan 2020',
            y0=10000,
            x1='31 Jan 2020',
            y1=16000,
            line=dict(
                color='Orange',
                width=2
            )
))

fig.update_layout(title={'text': 'All Cause Mortality in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  xaxis_title='Week Ending Date',
                  yaxis_title='Number of Deaths',
                  xaxis = dict(tickangle=-45),
                  annotations=[dict(x='10 Jan 2020', y=14058, text='2020 Peak', ax=40, ay=-25),
                               dict(x='31 Jan 2020', y=14000, text='COVID-19 Confirmed in UK', ax=120, ay=10),
                               dict(x='20 Mar 2020', y=10645, text='2020 Low', ax=-40, ay=10)
                              ])

fig.show()
fig.write_html("html/all_mortality.html")

# +
weeks = ['3 Jan 2020', '10 Jan 2020', '17 Jan 2020', '24 Jan 2020', '31 Jan 2020', 
         '7 Feb 2020', '14 Feb 2020', '21 Feb 2020', '28 Feb 2020', '6 Mar 2020', 
         '13 Mar 2020', '20 Mar 2020']
all_mortality = np.array([12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 10895, 11019, 10645], 
                         dtype=np.float)
deaths_under_1 = np.array([48, 50, 69, 53, 50, 31, 43, 51, 49, 56, 53, 44], dtype=np.float)
deaths_1_14 = np.array([16, 26, 15, 21, 15, 16, 12, 18, 20, 20, 22, 12], dtype=np.float)
deaths_15_44 = np.array([189, 275, 313, 314, 308, 271, 284, 321, 314, 313, 311, 275], dtype=np.float)
deaths_45_64 = np.array([1202, 1500, 1517, 1357, 1349, 1331, 1289, 1271, 1257, 1252, 1341, 1263], 
                        dtype=np.float)
deaths_65_74 = np.array([1860, 2198, 2013, 1958, 1927, 1808, 1753, 1744, 1795, 1769, 1754, 1780], 
                        dtype=np.float)
deaths_75_84 = np.array([3583, 4014, 3715, 3337, 3257, 3056, 3008, 3032, 2967, 3124, 3104, 3066], 
                        dtype=np.float)
deaths_over_85 = np.array([5356, 5995, 5348, 4816, 4706, 4473, 4555, 4404, 4414, 4361, 4434, 4205], 
                          dtype=np.float)

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=deaths_under_1, fill='tonexty',
                    mode= 'none', stackgroup='one', name='<1'
                        ))

fig.add_trace(go.Scatter(x= weeks, y=deaths_1_14, fill='tonexty',
                    mode='none', stackgroup='one', name='1-14'
                    ))

fig.add_trace(go.Scatter(x= weeks, y=deaths_15_44, fill='tonexty',
                    mode='none', stackgroup='one', name='15-44' 
                    ))

fig.add_trace(go.Scatter(x= weeks, y=deaths_45_64, fill='tonexty',
                    mode='none', stackgroup='one', name='45-64' 
                    ))

fig.add_trace(go.Scatter(x= weeks, y=deaths_65_74, fill='tonexty',
                    mode='none', stackgroup='one', name='65-74' 
                    ))

fig.add_trace(go.Scatter(x= weeks, y=deaths_75_84, fill='tonexty',
                    mode='none', stackgroup='one', name='75-84' 
                    ))

fig.add_trace(go.Scatter(x= weeks, y=deaths_over_85, fill='tonexty',
                    mode='none', stackgroup='one', name='85+' 
                    ))

fig.update_layout(title={'text': 'All Cause Mortality By Age in England and Wales: 2020', 'xanchor': 'center', 'x': 0.5}, 
                  #yaxis_range=(0, 100), 
                 xaxis_title='Week Ending Date',
                 yaxis_title='Number of Deaths',
                 xaxis = dict(tickangle=-45))
fig.show()
fig.write_html("html/all_mortality_age.html")
# -


