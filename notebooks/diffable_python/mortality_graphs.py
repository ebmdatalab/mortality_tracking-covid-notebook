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
#Code to extract data is at bottom of notebook

eng_wales_ages_18 = [669797, 10004735, 22447913, 15162118, 5906928, 3476922, 1447396]

def deaths_ht(deaths, pop):
    return round((deaths/pop) * 100000,2)


# +
weeks = ["3 Jan '20 <br> (Week 1)", '10 Jan', '17 Jan', '24 Jan', '31 Jan', 
         '7 Feb', '14 Feb', '21 Feb', '28 Feb', '6 Mar', '13 Mar', 
         '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May' , '8 May', 
         '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul',
         '10 Jul', '17 Jul', '24 Jul <br> (Week 30)']
all_mortality = np.array([12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 
                          10895, 11019, 10645, 11141, 16387, 18516, 22351, 21997, 17953, 
                          12657, 14573, 12288, 9824, 10709, 9976, 9339, 8979, 9140, 8690, 8823, 
                          8891], dtype=np.float)
rep_deaths = np.array([2141, 2477, 2188, 1894, 1746, 1572, 1602, 1619, 1547, 1583, 1508, 
                       1546, 1538, 1969, 1776, 1795, 1597, 1293, 948, 1167, 979, 812, 962, 
                       861, 869, 793, 846, 789, 721, 791], dtype=np.float)

five_year_mort = np.array([12175, 13822, 13216, 12760, 12206, 11925, 11627, 11548, 11183, 11498, 11205, 
                           10573, 10130, 10305, 10520, 10497, 10458, 9941, 9576, 10188, 9940, 8171, 9977, 
                           9417, 9404, 9293, 9183, 9250, 9093, 9052], dtype=np.float)
five_year_resp_rate = np.array([17.82, 19.05, 18.62, 17.95, 17.28, 16.83, 16.55, 16.65, 16.39, 15.94, 15.71, 15.1, 14.87, 15.3, 
                            14.8, 14.34, 13.8, 13.72, 13.39, 13.07], dtype=np.float)

f_y_rep_sd = np.array([0.019, 0.023, 0.026, 0.016, 0.01, 0.009, 0.004, 0.009, 0.008, 0.012, 0.013, 0.01, 
                       0.016, 0.014, 0.012, 0.005, .006, .007, .007, .005]) * 100

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=np.multiply(rep_deaths/all_mortality, 100), fill=None,
                    mode= 'lines+markers', name='<br>2020<br>'
                        ))


fig.add_trace(go.Scatter(x=weeks, y=five_year_resp_rate, fill=None,
                    mode= 'lines+markers', name='2015-19 <br> Average <br> (95% CI)', 
                         error_y=dict(type='data', array=f_y_rep_sd, visible=True)
                        ))

fig.update_layout(title={'text': 'Percent of All Mortality Caused by Respiratory Disease in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  xaxis_title='Week Ending Date',
                  yaxis_title='% of All Mortality',
                  yaxis_range=(0, 25), 
                  xaxis = dict(tickangle=-40))

fig.write_html("html/resp_mortality.html")
fig.show()

# +
weeks = ["3 Jan '20 <br> (Week 1)", '10 Jan', '17 Jan', '24 Jan', '31 Jan', 
         '7 Feb', '14 Feb', '21 Feb', '28 Feb', '6 Mar', '13 Mar', 
         '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May' , '8 May', 
         '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul',
         '10 Jul', '17 Jul', '24 Jul <br> (Week 30)']
all_mortality = [12254, 14058, 12990, 11856, 11612, 10986, 10944, 10841, 10816, 
                 10895, 11019, 10645, 11141, 16387, 18516, 22351, 21997, 17953, 
                 12657, 14573, 12288, 9824, 10709, 9976, 9339, 8979, 9140, 8690, 8823, 
                 8891]
five_year_mort = [12175, 13822, 13216, 12760, 12206, 11925, 11627, 11548, 11183, 11498, 11205, 
                  10573, 10130, 10305, 10520, 10497, 10458, 9941, 9576, 10188, 9940, 8171, 9977, 
                  9417, 9404, 9293, 9183, 9250, 9093, 9052]

sds = [804, 1885, 1486, 1214, 985, 524, 620, 428, 238, 869, 904, 831, 260, 952, 1443, 1108, 319, 
       880, 1008, 146, 258, 162, 170, 82, 145, 133, 85, 156, 195, 217]

ub = np.add(np.array(five_year_mort, dtype=np.float), np.array(sds, dtype=np.float))

lb = np.add(np.array(five_year_mort, dtype=np.float), -1 * np.array(sds, dtype=np.float))

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=ub, mode='lines', showlegend=False, line=dict(width=.01)))

fig.add_trace(go.Scatter(x=weeks, y=lb, mode='lines', showlegend=False, fill='tonextx', fillcolor='rgba(255, 0, 0, 0.1)',
                         line=dict(width=.01)))

fig.add_trace(go.Scatter(x=weeks, y=all_mortality, fill=None,
                    mode= 'lines', name='All Cause <br> Mortality 2020', line=dict(color='blue')
                        ))

fig.add_trace(go.Scatter(x= weeks, y=five_year_mort, fill=None,
                    mode='lines', name='Average All Cause <br> Mortality 2015-19 <br> (95% CI)', line=dict(color='red')
                    ))


fig.add_shape(
        # Line Vertical
        dict(
            type='line',
            x0='31 Jan',
            y0=0,
            x1='31 Jan',
            y1=25000,
            opacity=.5,
            line=dict(
                color='Orange',
                width=2
            )))
            
fig.add_shape(
        # Line Vertical
        dict(
            type='line',
            x0=11.4,
            y0=0,
            x1=11.4,
            y1=25000,
            opacity=.5,
            line=dict(
                color='Orange',
                width=2
            )))

fig.add_shape(
        # Line Vertical
        dict(
            type='line',
            x0=18.7,
            y0=0,
            x1=18.7,
            y1=25000,
            opacity=.5,
            line=dict(
                color='Orange',
                width=2
            )))

fig.update_layout(title={'text': 'All Cause Mortality in England and Wales by Week', 'xanchor': 'center', 'x': 0.5}, 
                  yaxis_range=(0, 25000),
                  xaxis_title='Week Ending Date',
                  yaxis_title='Number of Deaths',
                  xaxis = dict(tickangle=-45),
                  font = dict(size=10),
                  annotations=[dict(x='10 Jan', y=14058, text='Pre-COVID 2020 Peak', ax=40, ay=-35),
                               dict(x='31 Jan', y=7000, text='COVID-19 <br> Confirmed in UK', ax=50, ay=0),
                               dict(x=11.4, y=18000, text='Lockdown <br> Announced', ax=-50, ay=0),
                               dict(x=18.7, y=6000, text='First Steps to <br> Ease Lockdown', ax=-50, ay=0),
                               dict(x='20 Mar', y=10645, text='2020 Low', ax=-40, ay=-30),
                               dict(x='17 Apr', y=22531, text='2020 Peak', ax=-40, ay=-10),
                               dict(x='15 May', y=14573, text='Bank Holiday <br> Reporting Delay', ax=-8, ay=-30)
                              ])

fig.show()
fig.write_html("html/all_mortality.html")

# +
weeks = ["3 Jan '20", '10 Jan', '17 Jan', '24 Jan', '31 Jan', 
         '7 Feb', '14 Feb', '21 Feb', '28 Feb', '6 Mar', '13 Mar', 
         '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May' , '8 May', 
         '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul',
         '10 Jul', '17 Jul', '24 Jul']
deaths_under_1 = np.array([48, 50, 69, 53, 50, 31, 43, 51, 49, 56, 53, 44, 49, 51, 38, 51, 54, 48, 
                           28, 56, 51, 40, 44, 44, 48, 47, 47, 58, 35, 49], dtype=np.float)
deaths_1_14 = np.array([16, 26, 15, 21, 15, 16, 12, 18, 20, 20, 22, 12, 13, 21, 14, 15, 12, 11, 20, 
                        19, 16, 14, 16, 11, 28, 13, 27, 21, 20, 12], dtype=np.float)
deaths_15_44 = np.array([189, 275, 313, 314, 308, 271, 284, 321, 314, 313, 311, 275, 282, 288, 332, 353, 
                         404, 345, 233, 287, 339, 232, 267, 287, 263, 219, 272, 264, 277, 275], dtype=np.float)
deaths_45_64 = np.array([1202, 1500, 1517, 1357, 1349, 1331, 1289, 1271, 1257, 1252, 1341, 1263, 1301, 
                         1860, 2111, 2294, 2283, 1897, 1370, 1643, 1481, 1123, 1308, 1270, 1311, 1240, 
                         1285, 1190, 1302, 1208], dtype=np.float)
deaths_65_74 = np.array([1860, 2198, 2013, 1958, 1927, 1808, 1753, 1744, 1795, 1769, 1754, 1780, 1805, 
                         2734, 2946, 3380, 3238, 2601, 1935, 2188, 1883, 1567, 1791, 1719, 1615, 1568, 
                         1601, 1543, 1546, 1517], dtype=np.float)
deaths_75_84 = np.array([3583, 4014, 3715, 3337, 3257, 3056, 3008, 3032, 2967, 3124, 3104, 3066, 3247, 
                         5005, 5613, 6657, 6513, 5142, 3627, 4167, 5455, 2880, 3142, 2866, 2680, 2607, 
                         2630, 2529, 2547, 2506], dtype=np.float)
deaths_over_85 = np.array([5356, 5995, 5348, 4816, 4706, 4473, 4555, 4404, 4414, 4361, 4434, 4205, 4444, 
                           6428, 7462, 9601, 9493, 7909, 5444, 6213, 5063, 3968, 4141, 3779, 3508, 3377, 
                           3396, 3178, 3210, 3324], dtype=np.float)

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
ac_u_1_pop = np.around((deaths_under_1 / eng_wales_ages_18[0]) * 100000, decimals=2)
ac_1_14_pop = np.around((deaths_1_14 / eng_wales_ages_18[1]) * 100000, decimals=2)
ac_15_44_pop = np.around((deaths_15_44 / eng_wales_ages_18[2]) * 100000, decimals=2)
ac_45_64_pop = np.around((deaths_45_64 / eng_wales_ages_18[3]) * 100000, decimals=2)
ac_65_74_pop = np.around((deaths_65_74 / eng_wales_ages_18[4]) * 100000, decimals=2)
ac_75_84_pop = np.around((deaths_75_84 / eng_wales_ages_18[5]) * 100000, decimals=2)
ac_over_85_pop = np.around((deaths_over_85 / eng_wales_ages_18[6]) * 100000, decimals=2)

# +
ac_weeks = ["3 Jan '20", '10 Jan', '17 Jan', '24 Jan', '31 Jan', '7 Feb', '14 Feb', '21 Feb', '28 Feb', '6 Mar', '13 Mar', 
            '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May' , '8 May', 
            '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul',
            '10 Jul', '17 Jul', '24 Jul']

fig = go.Figure()

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_u_1_pop, fill=None,
                    mode= 'lines+markers', name='<1'
                        ))

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_1_14_pop, fill=None,
                    mode='lines+markers', name='1-14'
                    ))

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_15_44_pop, fill=None,
                    mode='lines+markers', name='15-44' 
                    ))

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_45_64_pop, fill=None,
                    mode='lines+markers', name='45-64' 
                    ))

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_65_74_pop, fill=None,
                    mode='lines+markers',  name='65-74' 
                    ))

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_75_84_pop, fill=None,
                    mode='lines+markers', name='75-84' 
                    ))

fig.add_trace(go.Scatter(x=ac_weeks, y=ac_over_85_pop, fill=None,
                    mode='lines+markers', name='85+' 
                    ))

fig.update_layout(title={'text': 'Mortality By Age per 100,000 population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  #yaxis_range=(0, 100), 
                 xaxis_title='Week Ending Date',
                 yaxis_title='Deaths/100000 pop',
                 xaxis = dict(tickangle=-45))
fig.show()
#fig.write_html("html/mortality_age_adj.html")
# -

u_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, deaths_ht(1, eng_wales_ages_18[0]), deaths_ht(1, eng_wales_ages_18[0]), 
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
o_ft = [0, 0, 0, 0, deaths_ht(1,eng_wales_ages_18[1]), deaths_ht(1,eng_wales_ages_18[1]), 
        deaths_ht(1,eng_wales_ages_18[1]), 0, 0, 0, 0,  deaths_ht(1,eng_wales_ages_18[1]), 0, 
        deaths_ht(1,eng_wales_ages_18[1]), 0, 0, 0, 0, 0, 0, 0]
ft_ff = [0, deaths_ht(2,eng_wales_ages_18[2]), deaths_ht(6,eng_wales_ages_18[2]), 
         deaths_ht(38,eng_wales_ages_18[2]), deaths_ht(73,eng_wales_ages_18[2]), 
         deaths_ht(109,eng_wales_ages_18[2]), deaths_ht(93,eng_wales_ages_18[2]), 
         deaths_ht(74,eng_wales_ages_18[2]), deaths_ht(38,eng_wales_ages_18[2]), 
         deaths_ht(33,eng_wales_ages_18[2]), deaths_ht(26,eng_wales_ages_18[2]), 
         deaths_ht(11,eng_wales_ages_18[2]), deaths_ht(13,eng_wales_ages_18[2]), 
         deaths_ht(9,eng_wales_ages_18[2]), deaths_ht(13,eng_wales_ages_18[2]), 
         deaths_ht(6,eng_wales_ages_18[2]), 0, deaths_ht(4,eng_wales_ages_18[2]), 
         deaths_ht(5,eng_wales_ages_18[2]), 0, deaths_ht(3,eng_wales_ages_18[2])]
ff_sf = [0, deaths_ht(6,eng_wales_ages_18[3]), deaths_ht(58,eng_wales_ages_18[3]), 
         deaths_ht(240,eng_wales_ages_18[3]), deaths_ht(654,eng_wales_ages_18[3]), 
         deaths_ht(968,eng_wales_ages_18[3]), deaths_ht(842,eng_wales_ages_18[3]), 
         deaths_ht(648,eng_wales_ages_18[3]), deaths_ht(395,eng_wales_ages_18[3]), 
         deaths_ht(290,eng_wales_ages_18[3]), deaths_ht(192,eng_wales_ages_18[3]), 
         deaths_ht(162,eng_wales_ages_18[3]), deaths_ht(144,eng_wales_ages_18[3]), 
         deaths_ht(81,eng_wales_ages_18[3]), deaths_ht(66,eng_wales_ages_18[3]), 
         deaths_ht(49,eng_wales_ages_18[3]), deaths_ht(44,eng_wales_ages_18[3]), 
         deaths_ht(35,eng_wales_ages_18[3]), deaths_ht(27,eng_wales_ages_18[3]), 
         deaths_ht(19,eng_wales_ages_18[3]), deaths_ht(10,eng_wales_ages_18[3])]
sf_sf = [deaths_ht(1,eng_wales_ages_18[4]), deaths_ht(11,eng_wales_ages_18[4]), 
         deaths_ht(66,eng_wales_ages_18[4]), deaths_ht(347,eng_wales_ages_18[4]), 
         deaths_ht(967,eng_wales_ages_18[4]), deaths_ht(1398,eng_wales_ages_18[4]), 
         deaths_ht(1276,eng_wales_ages_18[4]), deaths_ht(926,eng_wales_ages_18[4]), 
         deaths_ht(660,eng_wales_ages_18[4]), deaths_ht(520,eng_wales_ages_18[4]), 
         deaths_ht(326,eng_wales_ages_18[4]), deaths_ht(265,eng_wales_ages_18[4]), 
         deaths_ht(207,eng_wales_ages_18[4]), deaths_ht(181,eng_wales_ages_18[4]), 
         deaths_ht(103,eng_wales_ages_18[4]), deaths_ht(106,eng_wales_ages_18[4]), 
         deaths_ht(77,eng_wales_ages_18[4]), deaths_ht(54,eng_wales_ages_18[4]), 
         deaths_ht(46,eng_wales_ages_18[4]), deaths_ht(41,eng_wales_ages_18[4]), 
         deaths_ht(28,eng_wales_ages_18[4])]
sf_ef = [deaths_ht(4,eng_wales_ages_18[5]), deaths_ht(10,eng_wales_ages_18[5]), 
         deaths_ht(119,eng_wales_ages_18[5]), deaths_ht(642,eng_wales_ages_18[5]), 
         deaths_ht(1824,eng_wales_ages_18[5]), deaths_ht(2786,eng_wales_ages_18[5]), 
         deaths_ht(2645,eng_wales_ages_18[5]), deaths_ht(2168,eng_wales_ages_18[5]),
         deaths_ht(1652,eng_wales_ages_18[5]), deaths_ht(1187,eng_wales_ages_18[5]), 
         deaths_ht(891,eng_wales_ages_18[5]), deaths_ht(691,eng_wales_ages_18[5]), 
         deaths_ht(562,eng_wales_ages_18[5]), deaths_ht(418,eng_wales_ages_18[5]), 
         deaths_ht(317,eng_wales_ages_18[5]), deaths_ht(213,eng_wales_ages_18[5]), 
         deaths_ht(197,eng_wales_ages_18[5]), deaths_ht(141,eng_wales_ages_18[5]), 
         deaths_ht(100,eng_wales_ages_18[5]), deaths_ht(69,eng_wales_ages_18[5]), 
         deaths_ht(55,eng_wales_ages_18[5])]
ef_plus = [deaths_ht(1,eng_wales_ages_18[6]), deaths_ht(15,eng_wales_ages_18[6]), 
           deaths_ht(153,eng_wales_ages_18[6]), deaths_ht(604,eng_wales_ages_18[6]), 
           deaths_ht(1655,eng_wales_ages_18[6]), deaths_ht(2954,eng_wales_ages_18[6]), 
           deaths_ht(3435,eng_wales_ages_18[6]), deaths_ht(3103,eng_wales_ages_18[6]), 
           deaths_ht(2441,eng_wales_ages_18[6]), deaths_ht(1939,eng_wales_ages_18[6]), 
           deaths_ht(1415,eng_wales_ages_18[6]), deaths_ht(1139,eng_wales_ages_18[6]), 
           deaths_ht(845,eng_wales_ages_18[6]), deaths_ht(614,eng_wales_ages_18[6]), 
           deaths_ht(440,eng_wales_ages_18[6]), deaths_ht(297,eng_wales_ages_18[6]), 
           deaths_ht(259,eng_wales_ages_18[6]), deaths_ht(188,eng_wales_ages_18[6]), 
           deaths_ht(151,eng_wales_ages_18[6]), deaths_ht(87,eng_wales_ages_18[6]), 
           deaths_ht(71,eng_wales_ages_18[6])]

# +
fig = go.Figure(data = [
    go.Bar(name='<1', x=ac_weeks, y=u_1, text=u_1, textposition='outside'),
    go.Bar(name='1-14', x=ac_weeks, y=o_ft, text=o_ft, textposition='outside'),
    go.Bar(name='15-44', x=ac_weeks, y=ft_ff, text=ft_ff, textposition='outside'),
    go.Bar(name='45-64', x=ac_weeks, y=ff_sf, text=ff_sf, textposition='outside'),
    go.Bar(name='65-74', x=ac_weeks, y=sf_sf, text=sf_sf, textposition='outside'),
    go.Bar(name='75-84', x=ac_weeks, y=sf_ef, text=sf_ef, textposition='outside'),
    go.Bar(name='85+', x=ac_weeks, y=ef_plus, text=ef_plus, textposition='outside')
])

fig.update_layout(title={'text': 'COVID-19 Mortality By Age per 100,000 population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5},
                  barmode='group', 
                  yaxis_range=(0, 275),  
                  xaxis_title='Week Ending Date', 
                  yaxis_title='Deaths/100000 pop', 
                  uniformtext_minsize=6, uniformtext_mode='show')
fig.show()
#fig.write_html("html/covid_mortality_age_adj.html")

# +
c_weeks = ['6 Mar <br> 2020', '13 Mar', '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May', 
            '8 May', '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul', '10 Jul', 
            '17 Jul', '24 Jul']

fig = go.Figure(data = [
    go.Bar(name='<1', x=c_weeks, y=ac_u_1_pop, text=ac_u_1_pop, textposition='outside'),
    go.Bar(name='1-14', x=c_weeks, y=ac_1_14_pop, text=ac_1_14_pop, textposition='outside'),
    go.Bar(name='15-44', x=c_weeks, y=ac_15_44_pop, text=ac_15_44_pop, textposition='outside'),
    go.Bar(name='45-64', x=c_weeks, y=ac_45_64_pop, text=ac_45_64_pop, textposition='outside'),
    go.Bar(name='65-74', x=c_weeks, y=ac_65_74_pop, text=ac_65_74_pop, textposition='outside'),
    go.Bar(name='75-84', x=c_weeks, y=ac_75_84_pop, text=ac_75_84_pop, textposition='outside'),
    go.Bar(name='85+', x=c_weeks, y=ac_over_85_pop, text=ac_over_85_pop, textposition='outside')
])

fig.update_layout(title={'text': 'Mortality By Age per 100,000 population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5},
                  barmode='group', 
                  yaxis_range=(0, 800),  
                  xaxis_title='Week Ending Date', 
                  yaxis_title='Deaths/100000 pop', 
                  uniformtext_minsize=5, uniformtext_mode='show')
fig.show()
#fig.write_html("html/covid_mortality_age_adj.html")
# +
c_weeks = ['6 Mar <br> 2020', '13 Mar', '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May', 
            '8 May', '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul', '10 Jul', 
            '17 Jul', '24 Jul']

fig = go.Figure(data = [
    go.Bar(name='<1_covid', x=c_weeks, y=u_1, offsetgroup=0, showlegend=False, marker=dict(color='green')),
    go.Bar(name='<1-14_covid', x=c_weeks, y=o_ft, offsetgroup=1, showlegend=False, marker=dict(color='green')),
    go.Bar(name='15-44_covid', x=c_weeks, y=ft_ff, offsetgroup=2, showlegend=False, marker=dict(color='green')),
    go.Bar(name='45-64_covid', x=c_weeks, y=ff_sf, offsetgroup=3, showlegend=False, marker=dict(color='green')),
    go.Bar(name='65-74_covid', x=c_weeks, y=sf_sf, offsetgroup=4, showlegend=False, marker=dict(color='green')),
    go.Bar(name='75-84_covid', x=c_weeks, y=sf_ef, offsetgroup=5, showlegend=False, marker=dict(color='green')),
    go.Bar(name='85+_covid', x=c_weeks, y=ef_plus, offsetgroup=6, showlegend=False, marker=dict(color='green')),
    
    go.Bar(name='<1', x=c_weeks, y=ac_u_1_pop, text=ac_u_1_pop, textposition='outside', base=[0,0,0,0,0,0], offsetgroup=0),
    go.Bar(name='1-14', x=c_weeks, y=ac_1_14_pop, text=ac_1_14_pop, textposition='outside', base=o_ft, offsetgroup=1),
    go.Bar(name='15-44', x=c_weeks, y=ac_15_44_pop-ft_ff, text=ac_15_44_pop, textposition='outside', base=ft_ff, offsetgroup=2),
    go.Bar(name='45-64', x=c_weeks, y=ac_45_64_pop-ff_sf, text=ac_45_64_pop, textposition='outside', base=ff_sf, offsetgroup=3),
    go.Bar(name='65-74', x=c_weeks, y=ac_65_74_pop-sf_sf, text=ac_65_74_pop, textposition='outside', base=sf_sf, offsetgroup=4),
    go.Bar(name='75-84', x=c_weeks, y=ac_75_84_pop-sf_ef, text=ac_75_84_pop, textposition='outside', base=sf_ef, offsetgroup=5),
    go.Bar(name='85+', x=c_weeks, y=ac_over_85_pop-ef_plus, text=ac_over_85_pop, textposition='outside', base=ef_plus, offsetgroup=6),
    
    go.Bar(name='COVID', x=[None], y=[None], marker=dict(color='green')),
])

fig.update_layout(title={'text': 'Mortality By Age per 100,000 population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5},
                  barmode='group', 
                  yaxis_range=(0, 800),  
                  xaxis_title='Week Ending Date', 
                  yaxis_title='Deaths/100000 pop', 
                  uniformtext_minsize=5, 
                  uniformtext_mode='show', 
                  bargroupgap=.2)
fig.show()
#fig.write_html("html/covid_and_all_cause_mortality_age_adj.html")

# +
c_weeks = ['6 Mar <br> 2020', '13 Mar', '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May', 
            '8 May', '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul', '10 Jul', 
            '17 Jul', '24 Jul']

c_deaths_under_1 = np.array(u_1, dtype=np.float)
c_deaths_1_14 = np.array(o_ft, dtype=np.float)
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
                 uniformtext_minsize=5,
                 xaxis = dict(tickangle=-45))
fig.show()
fig.write_html("html/covid_mortality_age_adj.html")


# -

def deaths_mil(deaths, pop):
    return round((deaths/pop) * 1000000,2)


# +
u_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, deaths_mil(1, eng_wales_ages_18[0]), deaths_mil(1, eng_wales_ages_18[0]), 
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
o_ft = [0, 0, 0, 0, deaths_mil(1,eng_wales_ages_18[1]), deaths_mil(1,eng_wales_ages_18[1]), 
        deaths_mil(1,eng_wales_ages_18[1]), 0, 0, 0, 0,  deaths_mil(1,eng_wales_ages_18[1]), 0, 
        deaths_mil(1,eng_wales_ages_18[1]), 0, 0, 0, 0, 0, 0, 0]
ft_ff = [0, deaths_mil(2,eng_wales_ages_18[2]), deaths_mil(6,eng_wales_ages_18[2]), 
         deaths_mil(38,eng_wales_ages_18[2]), deaths_mil(73,eng_wales_ages_18[2]), 
         deaths_mil(109,eng_wales_ages_18[2]), deaths_mil(93,eng_wales_ages_18[2]), 
         deaths_mil(74,eng_wales_ages_18[2]), deaths_mil(38,eng_wales_ages_18[2]), 
         deaths_mil(33,eng_wales_ages_18[2]), deaths_mil(26,eng_wales_ages_18[2]), 
         deaths_mil(11,eng_wales_ages_18[2]), deaths_mil(13,eng_wales_ages_18[2]), 
         deaths_mil(9,eng_wales_ages_18[2]), deaths_mil(13,eng_wales_ages_18[2]), 
         deaths_mil(6,eng_wales_ages_18[2]), 0, deaths_mil(4,eng_wales_ages_18[2]), 
         deaths_mil(5,eng_wales_ages_18[2]), 0, deaths_mil(3,eng_wales_ages_18[2])]
ff_sf = [0, deaths_mil(6,eng_wales_ages_18[3]), deaths_mil(58,eng_wales_ages_18[3]), 
         deaths_mil(240,eng_wales_ages_18[3]), deaths_mil(654,eng_wales_ages_18[3]), 
         deaths_mil(968,eng_wales_ages_18[3]), deaths_mil(842,eng_wales_ages_18[3]), 
         deaths_mil(648,eng_wales_ages_18[3]), deaths_mil(395,eng_wales_ages_18[3]), 
         deaths_mil(290,eng_wales_ages_18[3]), deaths_mil(192,eng_wales_ages_18[3]), 
         deaths_mil(162,eng_wales_ages_18[3]), deaths_mil(144,eng_wales_ages_18[3]), 
         deaths_mil(81,eng_wales_ages_18[3]), deaths_mil(66,eng_wales_ages_18[3]), 
         deaths_mil(49,eng_wales_ages_18[3]), deaths_mil(44,eng_wales_ages_18[3]), 
         deaths_mil(35,eng_wales_ages_18[3]), deaths_mil(27,eng_wales_ages_18[3]), 
         deaths_mil(19,eng_wales_ages_18[3]), deaths_mil(10,eng_wales_ages_18[3])]
sf_sf = [deaths_mil(1,eng_wales_ages_18[4]), deaths_mil(11,eng_wales_ages_18[4]), 
         deaths_mil(66,eng_wales_ages_18[4]), deaths_mil(347,eng_wales_ages_18[4]), 
         deaths_mil(967,eng_wales_ages_18[4]), deaths_mil(1398,eng_wales_ages_18[4]), 
         deaths_mil(1276,eng_wales_ages_18[4]), deaths_mil(926,eng_wales_ages_18[4]), 
         deaths_mil(660,eng_wales_ages_18[4]), deaths_mil(520,eng_wales_ages_18[4]), 
         deaths_mil(326,eng_wales_ages_18[4]), deaths_mil(265,eng_wales_ages_18[4]), 
         deaths_mil(207,eng_wales_ages_18[4]), deaths_mil(181,eng_wales_ages_18[4]), 
         deaths_mil(103,eng_wales_ages_18[4]), deaths_mil(106,eng_wales_ages_18[4]), 
         deaths_mil(77,eng_wales_ages_18[4]), deaths_mil(54,eng_wales_ages_18[4]), 
         deaths_mil(46,eng_wales_ages_18[4]), deaths_mil(41,eng_wales_ages_18[4]), 
         deaths_mil(28,eng_wales_ages_18[4])]
sf_ef = [deaths_mil(4,eng_wales_ages_18[5]), deaths_mil(10,eng_wales_ages_18[5]), 
         deaths_mil(119,eng_wales_ages_18[5]), deaths_mil(642,eng_wales_ages_18[5]), 
         deaths_mil(1824,eng_wales_ages_18[5]), deaths_mil(2786,eng_wales_ages_18[5]), 
         deaths_mil(2645,eng_wales_ages_18[5]), deaths_mil(2168,eng_wales_ages_18[5]),
         deaths_mil(1652,eng_wales_ages_18[5]), deaths_mil(1187,eng_wales_ages_18[5]), 
         deaths_mil(891,eng_wales_ages_18[5]), deaths_mil(691,eng_wales_ages_18[5]), 
         deaths_mil(562,eng_wales_ages_18[5]), deaths_mil(418,eng_wales_ages_18[5]), 
         deaths_mil(317,eng_wales_ages_18[5]), deaths_mil(213,eng_wales_ages_18[5]), 
         deaths_mil(197,eng_wales_ages_18[5]), deaths_mil(141,eng_wales_ages_18[5]), 
         deaths_mil(100,eng_wales_ages_18[5]), deaths_mil(69,eng_wales_ages_18[5]), 
         deaths_mil(55,eng_wales_ages_18[5])]
ef_plus = [deaths_mil(1,eng_wales_ages_18[6]), deaths_mil(15,eng_wales_ages_18[6]), 
           deaths_mil(153,eng_wales_ages_18[6]), deaths_mil(604,eng_wales_ages_18[6]), 
           deaths_mil(1655,eng_wales_ages_18[6]), deaths_mil(2954,eng_wales_ages_18[6]), 
           deaths_mil(3435,eng_wales_ages_18[6]), deaths_mil(3103,eng_wales_ages_18[6]), 
           deaths_mil(2441,eng_wales_ages_18[6]), deaths_mil(1939,eng_wales_ages_18[6]), 
           deaths_mil(1415,eng_wales_ages_18[6]), deaths_mil(1139,eng_wales_ages_18[6]), 
           deaths_mil(845,eng_wales_ages_18[6]), deaths_mil(614,eng_wales_ages_18[6]), 
           deaths_mil(440,eng_wales_ages_18[6]), deaths_mil(297,eng_wales_ages_18[6]), 
           deaths_mil(259,eng_wales_ages_18[6]), deaths_mil(188,eng_wales_ages_18[6]), 
           deaths_mil(151,eng_wales_ages_18[6]), deaths_mil(87,eng_wales_ages_18[6]), 
           deaths_mil(71,eng_wales_ages_18[6])]


# +
c_weeks = ['6 Mar <br> 2020', '13 Mar', '20 Mar', '27 Mar', '3 Apr', '10 Apr', '17 Apr', '24 Apr', '1 May', 
            '8 May', '15 May', '22 May', '29 May', '5 Jun', '12 Jun', '19 Jun', '26 Jun', '3 Jul', '10 Jul', 
            '17 Jul', '24 Jul']

c_deaths_under_1 = np.array(u_1, dtype=np.float)
c_deaths_1_14 = np.array(o_ft, dtype=np.float)
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

fig.update_layout(title={'text': 'COVID-19 Mortality By Age per Million population <br> in England and Wales', 'xanchor': 'center', 'x': 0.5}, 
                  #yaxis_range=(0, 100), 
                 xaxis_title='Week Ending Date',
                 yaxis_title='Deaths/Million pop',
                 uniformtext_minsize=5,
                 xaxis = dict(tickangle=-45))
fig.show()
fig.write_html("html/covid_mortality_age_adj_per_mil.html")
# -


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



