import csv
import pandas as pd 
import plotly.figure_factory as ff
import statistics 
import random
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

data = df['Math_score'].tolist()

########fig = ff.create_distplot([data], ['math score'], show_hist= False)
########fig.show()

mean = statistics.mean(data)
sd = statistics.stdev(data)

print('this is the mean ', mean)
print('this is the standard deviation ', sd)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

sd = statistics.stdev(mean_list)
first_sd_start, first_sd_end = mean-sd, mean+sd
second_sd_start, second_sd_end = mean-(2*sd), mean+(2*sd)
third_sd_start, third_sd_end = mean-(3*sd), mean+(3*sd)

df = pd.read_csv('data1.csv')
data = df['Math_score'].tolist()
mean_sample1 = statistics.mean(data)
print('meen of sample 1', mean_sample1)
fig = ff.create_distplot([mean_list], ['student marks'], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_sample1,mean_sample1], y = [0,0.17], mode = 'lines', name = 'MEAN OF SAMPLE '))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = 'lines', name = 'STANDARD DEVIATION ONE END'))
fig.show()


df = pd.read_csv('data2.csv')
data = df['Math_score'].tolist()
mean_sample2 = statistics.mean(data)
print('meen of sample 2', mean_sample2)
fig = ff.create_distplot([mean_list], ['student marks'], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_sample2,mean_sample2], y = [0,0.17], mode = 'lines', name = 'MEAN OF SAMPLE '))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = 'lines', name = 'STANDARD DEVIATION ONE END'))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.17], mode = 'lines', name = 'STANDARD DEVIATION TWO END'))
fig.show()

df = pd.read_csv('data3.csv')
data = df['Math_score'].tolist()
mean_sample3 = statistics.mean(data)
print('meen of sample 3', mean_sample3)
fig = ff.create_distplot([mean_list], ['student marks'], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_sample3,mean_sample3], y = [0,0.17], mode = 'lines', name = 'MEAN OF SAMPLE '))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = 'lines', name = 'STANDARD DEVIATION ONE END'))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.17], mode = 'lines', name = 'STANDARD DEVIATION TWO END'))
fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.17], mode = 'lines', name = 'STANDARD DEVIATION THREE END'))
fig.show()

z_score = (mean_sample1 - mean)/sd
print('the z score is ', z_score)

z_score = (mean_sample2 - mean)/sd
print('the z score is ', z_score)

z_score = (mean_sample3 - mean)/sd
print('the z score is ', z_score)