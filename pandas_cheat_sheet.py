import pandas as pd
df = pd.read_csv('aapl_02_04.csv')

#print the data
# print(df)

#print first 5 rows and for last 5 print(df.tail(5))
# print(df.head(5))

#read headers
# print(df.columns)

#read each column
# print(df['Close'])

#read a row... uses index, in this case 4 through 8
# print(df.iloc[4:8])

#read a location by index [rowIndex, columnIndex]
# print(df.iloc[4,1])

#iterate through row
# for index, row in df.iterrows():
#   print(index, row)

#print all rows where percent change is greater than .01
# print(df.loc[df['Pct_Chg'] > .01])

#gives us stats
# print(df.describe())

#sort values, you can pass in multiple columns
# print(df.sort_values(['Change'], ascending=True))

# reset index
# df = df.reset_index(drop=True)

#use contains function to filter, check docs

#group a column by mean
# print(df.groupby(['Volume']).mean())
