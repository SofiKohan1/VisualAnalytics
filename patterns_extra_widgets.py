import pandas as pd
from IPython.display import Image
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
import plotly.express as px
import matplotlib.pyplot as plt 
pd.options.mode.chained_assignment = None  # default='warn'
import seaborn as sns
import numpy as np
from ipywidgets import widgets

mc1 = pd.read_csv('datasets/MC1Data/Lekagul Sensor Data.csv')

mc1['datetime'] = pd.to_datetime(mc1['Timestamp'], format="%Y-%m-%d %H:%M:%S")
mc1['month'] = mc1['datetime'].dt.month
mc1['day'] = mc1['datetime'].dt.day
mc1['year'] = mc1['datetime'].dt.year
mc1['hour'] = mc1['datetime'].dt.hour
mc1['minute'] = mc1['datetime'].dt.minute

car_grouping = mc1.groupby(['car-type']).size().reset_index(name='count').sort_values(['count'],ascending=False)
cars = pd.DataFrame(columns=["car-idx", "car-type", "car-count"])
cars['car-type'] = car_grouping['car-type']
cars['car-idx'] = range(len(car_grouping))
cars['car-count'] = car_grouping['count']
mc1 = pd.merge(mc1,cars ,on='car-type')

gate_grouping = mc1.groupby(['gate-name']).size().reset_index(name='count')#.sort_values(['count'],ascending=True)
gating = pd.DataFrame(columns=["gate-idx", "gate-name", "gate-count"])
gating['gate-name'] = gate_grouping['gate-name']
gating['gate-idx'] = range(len(gate_grouping))
gating['gate-idx'].astype('float64')
gating['gate-count'] = gate_grouping['count']
mc1 = pd.merge(mc1,gating ,on='gate-name')

id_grouping = mc1.groupby(['car-id']).size().reset_index(name='count')#.sort_values(['count'],ascending=True)
car_id = pd.DataFrame(columns=["car-id-idxx", "car-id", "car-id-count"])
car_id['car-id'] = id_grouping['car-id']
car_id['car-id-idxx'] = range(len(id_grouping))
car_id['car-id-count'] = id_grouping['count']
mc1 = pd.merge(mc1, car_id ,on='car-id')

df2015 = mc1['year'] == 2015
df2015 = mc1[df2015]

df2016 = mc1['year'] == 2016
df2016 = mc1[df2016]

type_1 = mc1['car-type'] == '1'
type_2 = mc1['car-type'] == '2'
type_3 = mc1['car-type'] == '3'
type_4 = mc1['car-type'] == '4'
type_5 = mc1['car-type'] == '5'
type_6 = mc1['car-type'] == '6'
type_7 = mc1['car-type'] == '2P'

type_1 = mc1[type_1] 
type_2 = mc1[type_2] 
type_3 = mc1[type_3] 
type_4 = mc1[type_4] 
type_5 = mc1[type_5] 
type_6 = mc1[type_6] 
type_7 = mc1[type_7] 
    
def type_per_moment_15(choose):   
    fig1 = px.histogram(type_1[type_1['year']==2015], x=choose, color='gate-name', 
                       title= 'Frequency plots showing gates registeres by car type 1')
    fig1.show()
    fig2 = px.histogram(type_2[type_2['year']==2015], x=choose, color='gate-name',
                       title= 'Frequency plots showing gates registeres by car type 2')
    fig2.show()
    fig3 = px.histogram(type_3[type_3['year']==2015], x=choose, color='gate-name',
                       title= 'Frequency plots showing gates registeres by car type 3')
    fig3.show()
    fig4 = px.histogram(type_4[type_4['year']==2015], x=choose, color='gate-name',
                       title= 'Frequency plots showing gates registeres by car type 4')
    fig4.show()
    fig5 = px.histogram(type_5[type_5['year']==2015], x=choose, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 5')
    fig5.show()
    fig6 = px.histogram(type_6[type_6['year']==2015], x=choose, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 6')
    fig6.show()
    fig7 = px.histogram(type_7[type_7['year']==2015], x=choose, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 7')
    fig7.show()

def type_per_moment_16(choose_):
    fig01 = px.histogram(type_1[type_1['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 1')
    fig01.show()
    fig02 = px.histogram(type_2[type_2['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 2')
    fig02.show()
    fig03 = px.histogram(type_3[type_3['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 3')
    fig03.show()
    fig04 = px.histogram(type_4[type_4['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 4')
    fig04.show()
    fig05 = px.histogram(type_5[type_5['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 5')
    fig05.show()
    fig06 = px.histogram(type_6[type_6['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 6')
    fig06.show()
    fig07 = px.histogram(type_7[type_7['year']==2016], x=choose_, color='gate-name',
                        title= 'Frequency plots showing gates registeres by car type 7')
    fig07.show()


def heatmaps(y):
    fig8 = px.density_heatmap(mc1, x="gate-name", y=y, title= 'Heatmaps to detect frequency of gates used through time and car types')
    fig8.show()
    
'''
def scatter_(type_):
    fig_timelapse01 = px.scatter(df2015[df2015['car-type'] == type_], x='datetime', y='car-id-idxx', color='gate-name',
                                title= 'Gates registeres by time per car corresponding to type 1')
    fig_timelapse01.show()
    fig_timelapse02 = px.scatter(df2016[df2016['car-type'] == type_], x='datetime', y='car-id-idxx', color='gate-name')
    fig_timelapse02.show()
'''

'''
def scatter1(car_id1):
    fig_timelapse = px.scatter(type_1[(type_1['car-id-idxx'] == car_id1) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()    

def scatter2(car_id2):
    fig_timelapse = px.scatter(type_2[(type_2['car-id-idxx'] == car_id2) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()
    
def scatter3(car_id3):
    fig_timelapse = px.scatter(type_3[(type_3['car-id-idxx'] == car_id3) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()    
    
def scatter4(car_id4):
    fig_timelapse = px.scatter(type_4[(type_4['car-id-idxx'] == car_id4) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()    
    
def scatter5(car_id5):
    fig_timelapse = px.scatter(type_5[(type_5['car-id-idxx'] == car_id5) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()

def scatter6(car_id6):
    fig_timelapse = px.scatter(type_6[(type_6['car-id-idxx'] == car_id6) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()

def scatter7(car_id7):
    fig_timelapse = px.scatter(type_7[(type_7['car-id-idxx'] == car_id7) ], x='datetime', y='gate-name', color='gate-name')
    fig_timelapse.show()

'''

