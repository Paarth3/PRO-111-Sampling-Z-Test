import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random
import numpy as np

df = pd.read_csv("C:/Users/ADMIN/Desktop/WhiteHat_Jr/General/Data/medium_data.csv")
new_df = pd.read_csv("C:/Users/ADMIN/Desktop/WhiteHat_Jr/General/Data/sample_2.csv")

population_mean = statistics.mean(df["reading_time"])

all_means = []
for i in range(100):
    temp_mean_list = []
    for i in range(30):
        value =random.choice(df["reading_time"])
        temp_mean_list.append(float(value))
    all_means.append(float(statistics.mean(temp_mean_list)))


sampling_mean = statistics.mean(all_means)
std = statistics.stdev(all_means)

std_1_start = sampling_mean  - 1*std
std_1_end = sampling_mean  + 1*std
std_2_start = sampling_mean  - 2*std
std_2_end = sampling_mean  + 2*std
std_3_start = sampling_mean  - 3*std
std_3_end = sampling_mean  + 3*std

fig = ff.create_distplot([all_means], ["Mean"], show_hist=False)
fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 0.90], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[std_1_start, std_1_start], y=[0, 0.90], mode="lines", name="Standard Deviation 1 Start"))
fig.add_trace(go.Scatter(x=[std_1_end, std_1_end], y=[0, 0.90], mode="lines", name="Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[std_2_start, std_2_start], y=[0, 0.90], mode="lines", name="Standard Deviation 2 Start"))
fig.add_trace(go.Scatter(x=[std_2_end, std_2_end], y=[0, 0.90], mode="lines", name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[std_3_start, std_3_start], y=[0, 0.90], mode="lines", name="Standard Deviation 3 Start"))
fig.add_trace(go.Scatter(x=[std_3_end, std_3_end], y=[0, 0.90], mode="lines", name="Standard Deviation 3 End"))

new_mean = statistics.mean(new_df["reading_time"])
fig.add_trace(go.Scatter(x=[new_mean, new_mean], y=[0, 0.90], mode="lines", name="New Data Mean"))

fig.show()

z_score = (new_mean - sampling_mean)/std
print(z_score)