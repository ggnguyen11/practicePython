# visualizations for SNHU's DAT-510-Q3232 Foundations of Data Final Project

# importing pandas package
import pandas as pd

# assigning object p to variable data, to read in excel sheet
data = pd.read_csv(\
"C:/Users/b/Desktop/schoolstuff/SNHU/DAT-510-Q3232/Scenario_DataSets/\
Chapter04DataSet.csv")

# constructing correlation matrix, w/ values rounded to hundredths place
cMatrix = data.corr().round(2)

# displaying 6x6 correlation matrix to the terminal
print(cMatrix)