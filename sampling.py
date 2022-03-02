import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("C:/Users/dell/Desktop/Python/folderA/datas/medium_data.csv")
data=df["reading_time"].to_list()
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()
#dataSet=[]
#for i in range(0,100):
   # randomIndex=random.randint(0,len(data))
   # value=data[randomIndex]
   # dataSet.append(value)
#mean=statistics.mean(dataSet)
#stdev=statistics.stdev(dataSet)
#print("Mean: "mean)
#print("Standard Deviation: "stdev)
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return(mean)
def showFig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    meanList=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        meanList.append(setOfMean)
    showFig(meanList)
    mean=statistics.mean(meanList)
    print(mean)
    
setup()
populationMean=statistics.mean(data)
print(populationMean)
def standard_deviation():
    meanList=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        meanList.append(setOfMean)
    stddev=statistics.stdev(meanList)
    print(stddev)
standard_deviation()





    




