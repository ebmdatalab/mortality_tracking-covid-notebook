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

# +
import plotly.graph_objects as go
from datetime import date
import numpy as np

#raw data from https://docs.google.com/spreadsheets/d/1W7ugZvJI8JQu_smwWlkM_6ofasDdYyftMmAkZ_D_tfg/edit#gid=0

# +
#from https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/articles/ukpopulationpyramidinteractive/2020-01-08

eng_wales_ages_18 = [669797, 10004735, 22447913, 15162118, 5906928, 3476922, 1447396]

def deaths_ht(deaths, pop):
    return round((deaths/pop) * 100000,2)


# +
weeks = ['3 Jan 2020', '10 Jan 2020', '17 Jan 2020', '24 Jan 2020', '31 Jan 2020', 
         '7 Feb 2020', '14 Feb 2020', '21 Feb 2020', '28 Feb 2020', '6 Mar 2020', '13 Mar 2020',
         '20 Mar 2020', '27 Mar 2020', '3 Apr 2020']
all_mortality = np.array([12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 
                          10895, 11019, 10645, 11141, 16387], 
                         dtype=np.float)
rep_deaths = np.array([2141, 2477, 2188, 1894, 1746, 1572, 1602, 1618, 1529, 1551, 1488, 1514, 1534, 2106], dtype=np.float)

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
weeks = ['3 Jan 2020 <br> (Week 1)', '10 Jan 2020', '17 Jan 2020', '24 Jan 2020', '31 Jan 2020', 
         '7 Feb 2020', '14 Feb 2020', '21 Feb 2020', '28 Feb 2020', '6 Mar 2020', '13 Mar 2020', 
         '20 Mar 2020', '27 Mar 2020', '3 Apr 2020 <br> (Week 14)']
all_mortality = [12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 10895, 11019, 10645, 11141, 16387]
five_year_mort = [12175, 13822, 13216, 12760, 12206, 11925, 11627, 11548, 11183, 11498, 11205, 10573, 10130, 10305]

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
            y1=17000,
            line=dict(
                color='Orange',
                width=2
            )
))

fig.update_layout(title={'text': 'All Cause Mortality in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  xaxis_title='Week Ending Date',
                  yaxis_title='Number of Deaths',
                  xaxis = dict(tickangle=-45),
                  font = dict(size=10),
                  annotations=[dict(x='10 Jan 2020', y=14058, text='2020 Peak', ax=40, ay=-25),
                               dict(x='31 Jan 2020', y=14000, text='COVID-19 Confirmed in UK', ax=120, ay=10),
                               dict(x='20 Mar 2020', y=10645, text='2020 Low', ax=-40, ay=10)
                              ])

fig.show()
fig.write_html("html/all_mortality.html")

# +
weeks = ['3 Jan 2020', '10 Jan 2020', '17 Jan 2020', '24 Jan 2020', '31 Jan 2020', 
         '7 Feb 2020', '14 Feb 2020', '21 Feb 2020', '28 Feb 2020', '6 Mar 2020', 
         '13 Mar 2020', '20 Mar 2020', '27 Mar 2020', '3 Apr 2020']
all_mortality = np.array([12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 10895, 11019, 10645], 
                         dtype=np.float)
deaths_under_1 = np.array([48, 50, 69, 53, 50, 31, 43, 51, 49, 56, 53, 44, 49, 51], dtype=np.float)
deaths_1_14 = np.array([16, 26, 15, 21, 15, 16, 12, 18, 20, 20, 22, 12, 13, 21], dtype=np.float)
deaths_15_44 = np.array([189, 275, 313, 314, 308, 271, 284, 321, 314, 313, 311, 275, 282, 288], dtype=np.float)
deaths_45_64 = np.array([1202, 1500, 1517, 1357, 1349, 1331, 1289, 1271, 1257, 1252, 1341, 1263, 1301, 1860], 
                        dtype=np.float)
deaths_65_74 = np.array([1860, 2198, 2013, 1958, 1927, 1808, 1753, 1744, 1795, 1769, 1754, 1780, 1805, 2734], 
                        dtype=np.float)
deaths_75_84 = np.array([3583, 4014, 3715, 3337, 3257, 3056, 3008, 3032, 2967, 3124, 3104, 3066, 3247, 5005], 
                        dtype=np.float)
deaths_over_85 = np.array([5356, 5995, 5348, 4816, 4706, 4473, 4555, 4404, 4414, 4361, 4434, 4205, 4444, 6428], 
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
# +
c_weeks = ['20 Mar 2020', '27 Mar 2020']

c_deaths_under_1 = np.array([0,0], dtype=np.float)
c_deaths_1_14 = np.array([0,0], dtype=np.float)
c_deaths_15_44 = np.array([1,8], dtype=np.float)
c_deaths_45_64 = np.array([6,63], 
                        dtype=np.float)
c_deaths_65_74 = np.array([20,99], 
                        dtype=np.float)
c_deaths_75_84 = np.array([31, 181], 
                        dtype=np.float)
c_deaths_over_85 = np.array([45, 188], 
                          dtype=np.float)

fig = go.Figure()

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_under_1, fill='tonexty',
                    mode= 'none', stackgroup='one', name='<1'
                        ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_1_14, fill='tonexty',
                    mode='none', stackgroup='one', name='1-14'
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_15_44, fill='tonexty',
                    mode='none', stackgroup='one', name='15-44' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_45_64, fill='tonexty',
                    mode='none', stackgroup='one', name='45-64' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_65_74, fill='tonexty',
                    mode='none', stackgroup='one', name='65-74' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_75_84, fill='tonexty',
                    mode='none', stackgroup='one', name='75-84' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_over_85, fill='tonexty',
                    mode='none', stackgroup='one', name='85+' 
                    ))

fig.update_layout(title={'text': 'COVID Mortality By Age in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  #yaxis_range=(0, 100), 
                 xaxis_title='Week Ending Date',
                 yaxis_title='Number of Deaths',
                 xaxis = dict(tickangle=-45))
fig.show()
#fig.write_html("html/covid_mortality_age.html")


# +
ft_ff = [deaths_ht(1,eng_wales_ages_18[2]), deaths_ht(8,eng_wales_ages_18[2]), deaths_ht(43,eng_wales_ages_18[2])]
ff_sf = [deaths_ht(6,eng_wales_ages_18[3]), deaths_ht(63,eng_wales_ages_18[3]), deaths_ht(412,eng_wales_ages_18[3])]
sf_sf = [deaths_ht(20,eng_wales_ages_18[4]), deaths_ht(99,eng_wales_ages_18[4]), deaths_ht(626,eng_wales_ages_18[4])]
sf_ef = [deaths_ht(31,eng_wales_ages_18[5]), deaths_ht(181,eng_wales_ages_18[5]), deaths_ht(1231,eng_wales_ages_18[5])]
ef_plus = [deaths_ht(45,eng_wales_ages_18[6]), deaths_ht(188,eng_wales_ages_18[6]), deaths_ht(1163,eng_wales_ages_18[6])]

c_weeks = ['20 Mar 2020', '27 Mar 2020', '3 Apr 2020']

fig = go.Figure(data = [
    go.Bar(name='<1', x=c_weeks, y=[0,0,0], text=[0,0,0], textposition='outside'),
    go.Bar(name='1-14', x=c_weeks, y=[0,0,0], text=[0,0,0], textposition='outside'),
    go.Bar(name='15-44', x=c_weeks, y=ft_ff, text=ft_ff, textposition='outside'),
    go.Bar(name='45-64', x=c_weeks, y=ff_sf, text=ff_sf, textposition='outside'),
    go.Bar(name='65-74', x=c_weeks, y=sf_sf, text=sf_sf, textposition='outside'),
    go.Bar(name='75-84', x=c_weeks, y=sf_ef, text=sf_ef, textposition='outside'),
    go.Bar(name='85+', x=c_weeks, y=ef_plus, text=ef_plus, textposition='outside')
])

fig.update_layout(title={'text': 'COVID-19 Mortality By Age per 100,000 population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5},
                  barmode='group', 
                  yaxis_range=(0, 90),  
                  xaxis_title='Week Ending Date', 
                  yaxis_title='Deaths/100000 pop')
fig.show()
fig.write_html("html/covid_mortality_age_adj.html")
# +
c_weeks = ['20 Mar 2020', '27 Mar 2020', '03 Apr 2020']

c_deaths_under_1 = np.array([0,0,0], dtype=np.float)
c_deaths_1_14 = np.array([0,0,0], dtype=np.float)
c_deaths_15_44 = np.array(ft_ff, dtype=np.float)
c_deaths_45_64 = np.array(ff_sf, 
                        dtype=np.float)
c_deaths_65_74 = np.array(sf_sf, 
                        dtype=np.float)
c_deaths_75_84 = np.array(sf_ef, 
                        dtype=np.float)
c_deaths_over_85 = np.array(ef_plus, 
                          dtype=np.float)

fig = go.Figure()

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_under_1, fill=None,
                    mode= 'lines+markers', name='<1'
                        ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_1_14, fill=None,
                    mode='lines+markers', name='1-14'
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_15_44, fill=None,
                    mode='lines+markers', name='15-44' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_45_64, fill=None,
                    mode='lines+markers', name='45-64' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_65_74, fill=None,
                    mode='lines+markers',  name='65-74' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_75_84, fill=None,
                    mode='lines+markers', name='75-84' 
                    ))

fig.add_trace(go.Scatter(x=c_weeks, y=c_deaths_over_85, fill=None,
                    mode='lines+markers', name='85+' 
                    ))

fig.update_layout(title={'text': 'COVID-19 Mortality By Age per 100,000 population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  #yaxis_range=(0, 100), 
                 xaxis_title='Week Ending Date',
                 yaxis_title='Deaths/100000 pop',
                 xaxis = dict(tickangle=-45))
fig.show()
#fig.write_html("html/covid_mortality_age.html")

# +



# +
#Run this to get England and Wales population data

import requests

england_pop = requests.get('https://www.ons.gov.uk/visualisations/dvc671/pyramids2/pyramids/data/england.json').json()

wales_pop = requests.get('https://www.ons.gov.uk/visualisations/dvc671/pyramids2/pyramids/data/wales.json').json()

ages = england_pop['ons']['dimension']['index']

def age_range(x, lower, upper):
    if x>=lower and x<=upper:
        return True
    else:
        return False

england_wales = {}

for age in ages:
    i = int(age.replace('+', ''))
    e_m = england_pop['ons']['value'][0][i][2][0]
    e_f = england_pop['ons']['value'][1][i][2][0]
    w_m = wales_pop['ons']['value'][0][i][2][0]
    w_f = wales_pop['ons']['value'][1][i][2][0]
    england_wales[i] = e_m + e_f + w_m + w_f
    
under_ones = []
one_fourteen = []
fifteen_fourtyfour = []
fourtyfive_sixtyfour = []
sixtyfive_seventyfour = []
seventyfive_eightyfour = []
eightyfive_plus = []

for age, total in england_wales.items():
    if age == 0:
        under_ones.append(total)
    elif age_range(age, 1, 14):
        one_fourteen.append(total)
    elif age_range(age, 15, 44):
        fifteen_fourtyfour.append(total)
    elif age_range(age, 45, 64):
        fourtyfive_sixtyfour.append(total)
    elif age_range(age, 65, 74):
        sixtyfive_seventyfour.append(total)
    elif age_range(age, 75, 84):
        seventyfive_eightyfour.append(total)
    elif age > 84:
        eightyfive_plus.append(total)
# -


