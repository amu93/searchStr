import pandas as pd

# reading csv file

data = pd.read_csv("python_assesment.csv")
data.dropna(inplace=True)

# search,sort and produce first 20 suggestions in result

searchText = input("Enter the string for searching: ")
stringOutput = data.loc[data['name'].str.contains(searchText, case=False)]
stringList = stringOutput['name'].values.tolist()
stringList.sort()
finalResult = '\n'.join(map(str, stringList[:20]))

print(finalResult)
