import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colours = data['Primary Fur Color'].unique().tolist()
fur_counts = [[f,len(data[data['Primary Fur Color'] == f])] for f in fur_colours[1:]]
fur_count_dict = {"Colour":[],"Count":[]}
for colour,ct in fur_counts:
    fur_count_dict["Colour"].append(colour)
    fur_count_dict["Count"].append(ct)
fur_count_df = pandas.DataFrame.from_dict(fur_count_dict)
fur_count_df.to_csv("squirrel_colour_counts.csv")
print(fur_count_df)
# print(fur_data)