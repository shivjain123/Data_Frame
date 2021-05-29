import pandas as pd
import plotly.express as px

""" list1 = [1, 2, 3]
list2 = [4, 5, 6]

frame = pd.DataFrame([list1, list2])

print(frame) """


df = pd.read_csv("C:/Users/HP/OneDrive/Documents/Python (WhiteHatJr)/.py/csv files/line_chart.csv")

print(df)

figure = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")

figure.show()

""" df = pd.read_csv("C:/Users/HP/OneDrive/Documents/Python (WhiteHatJr)/.py/csv files/data.csv")

print(df)

figure = px.scatter(df, x = "Population", y = "InternetUsers", title = "No. of Internet Users", size = "Percentage", size_max= 30)

figure.show() """