import pandas
df = pandas.read_csv(r'clean_all_data.csv')
df2 = pandas.read_csv(r'complete_data.csv')

listOfDFRows = df.to_numpy().tolist()
listOfDFRows2 = df2.to_numpy().tolist()
print(len(listOfDFRows[0]))
print(len(listOfDFRows2[0]))
