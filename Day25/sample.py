# import os, csv, pandas

# path_to_file = os.path.join((os.path.dirname(__file__)),'weather_data.csv')
# with open(path_to_file) as file:
#     data = file.readlines()
#     print(data)

# with open(path_to_file) as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp": 
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

# data = pandas.read_csv(os.path.join((os.path.dirname(__file__)),'weather_data.csv'))
# temp_list = data["temp"]
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data[data.temp == data.temp.max()])

# data = pandas.read_csv(os.path.join((os.path.dirname(__file__)),'squirells.csv'))
# fur_colors = data["Primary Fur Color"].unique()
# counts = []
# for color in fur_colors[1:]:
#     counts.append(len(data["Primary Fur Color"] == color))
# squirells_dic = {"Fur Colour": fur_colors[1:], "Count": counts}
# df = pandas.DataFrame(squirells_dic)
# print(df)