import pandas as pd
import plotly.express as px
import numpy as np

# data = pd.read_csv("Student Marks vs Days Present.csv")
# fig = px.scatter(data, x = "Days Present", y = "Marks In Percentage")
# fig.show()
# corr = np.corrcoef(data["Days Present"], data["Marks In Percentage"])
# print(corr)

data = pd.read_csv("cups of coffee vs hours of sleep.csv")
fig = px.scatter(data, x = "Coffee in ml", y = "sleep in hours")
fig.show()
corr = np.corrcoef(data["Coffee in ml"], data["sleep in hours"])
print(corr)