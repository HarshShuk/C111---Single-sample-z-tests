from re import M
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv 

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
standerdeveation=statistics.stdev(data)
def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range (0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)
standerdeveation=statistics.stdev(mean_list)
first_stdev_start,first_stdev_end=mean-standerdeveation,mean+standerdeveation
second_stdev_start,second_stdev_end=mean-2*standerdeveation,mean+2*standerdeveation
third_stdev_start,third_stdev_end=mean-3*standerdeveation,mean+3*standerdeveation

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
mean_sample3=statistics.mean(data)
print("mean:",mean_sample3)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,0.17],mode="lines",name="MEAN OF STUDENT WHO GOT SHEETS"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="STANDER DEVEATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name="STANDER DEVEATION 3 END"))
fig.show()

zscore=(mean-mean_sample3)/standerdeveation
print("zscore is :",zscore)