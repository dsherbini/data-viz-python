# PPHA 30537: Python Programming for Public Policy
# Spring 2023
# HW6: Data Viz with Matplotlib & Seaborn
# Author: Danya Sherbini

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_plot.png", "q2_plot.png", etc. using fig.savefig.
# If a question calls for more than one plot, name them "q1a_plot", "q1b_plot", 
# etc.


# Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW6 Q1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

base_path = '/Users/danya/Documents/GitHub/personal github/homework-6-dsherbini'
os.chdir(base_path)


x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

fig, ax = plt.subplots()
ax.scatter(x, y1, color = 'black', label = 'y1')
ax.plot(x, y2, color ='red', label='y2')
ax.legend(loc='best')
ax.set_xlabel('Date')
ax.set_ylabel('Values')
ax.set_title('HW6 Q1')
ax.tick_params(axis = 'x', rotation = 45, labelsize = 8)
fig.savefig('q1_plot.png')

fig.clear()


# Question 2: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

path = os.path.join(base_path, 'mpg.csv')
df = pd.read_csv(path)


fig, ax = plt.subplots()
ax.scatter(df['displacement'], df['mpg'], color='blue')
ax.set_xlabel('Engine Displacement')
ax.set_ylabel('Gas Mileage (mpg)')
ax.set_title('Impact of Displacement on Gas Mileage')
fig.savefig('q3a_plot.png')

fig.clear()

fig, ax = plt.subplots()
ax.scatter(df['weight'], df['horsepower'], color='blue')
ax.set_xlabel('Weight')
ax.set_ylabel('Hosepower')
ax.set_title('Impact of Weight on Horsepower')
fig.savefig('q3b_plot.png')

fig.clear()


# Question 3: Continuing with the data from question 3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.

fig, ax = plt.subplots()
ax.scatter(df['cylinders'], df['mpg'], color='blue')

fig.clear()

# this plot shouldn't be a scatter plot because the cylinder type acts 
# as a categorical variable

sns.set() 
fig, ax = plt.subplots()
ax = sns.boxplot(x='cylinders', y='mpg', data = df)
ax.set_ylabel('Gas Mileage (mpg)')
ax.set_xlabel('Cylinders')
ax.set_title('Gas Mileage by Cylinders')
fig.savefig('q4_plot.png')

fig.clear()


# Question 4: Continuing with the data from question 3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.

    
fig, axs = plt.subplots(2, 2, sharey = True, figsize = (8,8))   
axs[0, 0].scatter(df['displacement'], df['mpg'])
axs[0, 0].set_xlabel('Displacement')
axs[0, 1].scatter(df['horsepower'], df['mpg'], color = 'red')
axs[0, 1].set_xlabel('Horsepower')
axs[1, 0].scatter(df['weight'], df['mpg'], color = 'green')
axs[1, 0].set_xlabel('Weight')
axs[1, 1].scatter(df['acceleration'], df['mpg'], color = 'orange')
axs[1, 1].set_xlabel('Acceleration')
fig.suptitle('Changes in MPG', y = .94)
fig.supylabel('mpg')
fig.savefig('q5_plot.png')

fig.clear()



# Question 5: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.

sns.set() 
fig, ax = plt.subplots()
ax = sns.barplot(x='origin', y='mpg', data = df)
ax.set_xlabel('Origin')
ax.set_ylabel('Gas Mileage (mpg)')
ax.set_title('Average Gas Mileage by Country')
fig.savefig('q6_plot.png')

fig.clear()

# Cars from the USA are the least feul efficient on average

# Question 6: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.

sns.set() 
fig, ax = plt.subplots()
ax = sns.scatterplot(x='displacement', y='mpg', data = df, hue = 'origin')
ax.set_ylabel('Gas Mileage (mpg)')
ax.set_xlabel('Displacement')
ax.set_title('Gas Mileage by Displacement')
fig.savefig('q7_plot.png')

fig.clear()

