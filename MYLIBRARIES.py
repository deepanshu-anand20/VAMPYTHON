# Numpy :- data set creation 
# Pandas :- data set represent
# Matplotlib :- graphically data representation 
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
years = np.array([2020,2022,2023])
grade = np.array([81,83,73])
# plt.plot(years,grade,marker='o') #for creating a graph with marker. 
# plt.title("MY ACADEMIC PERFORMANCE") #for giving a title. 
# plt.xlabel("Years........")#for naming x axis. 
# plt.ylabel("Grades.......")#for naming y axis. 
# plt.grid()#for a grid.
# plt.show()#for showing a graph.
# x = np.array([90,75,80,65,50,70,50,65,57])

# plt.pie(x)
# plt.title("...PIE CHART...")
# name = np.array(["Python","Java","React","C++","C","C#","R","CSS","RUBY"])
# plt.legend(name) #for showing the titles.
# plt.show()
# Creation a bar graph 
# plt.bar(years,grade)
# creating a scatter graph 
plt.scatter(years,grade)

plt.show()

