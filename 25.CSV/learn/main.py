# import csv

# with open('./25.CSV/weather-data.csv' ,mode='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     day = []
#     for row in data:
#         day.append(row[0])
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     print(day)

import pandas

# data = pandas.read_csv("./25.CSV/weather-data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)

# mean = data['temp'].mean()
# print(mean) 

data = pandas.read_csv("./25.CSV/squirrel_count.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinammon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(data)
print(grey_squirrel)
print(cinammon_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, cinammon_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./25.CSV/squirrel_output.csv")