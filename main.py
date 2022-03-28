import math

import pandas as pd
import openpyxl

df = pd.read_excel('data.xlsx', sheet_name='bands')
sixList = df['Unnamed: 6'].to_list()
zeroList = df['Unnamed: 0'].to_list()

threepdList = [round((round((i * 1.27) + 0.05, 1) - 0.01), 2) if type(i) == float or type(i) == int else 0 for i in df['Unnamed: 6']]

description = pd.Series(zeroList)
price = pd.Series(sixList)
delivery = pd.Series(threepdList)

dict = {'Description': description, 'Price': price, 'Delivery': delivery}
output_df = pd.DataFrame(dict)
print(output_df)
output_df.to_excel('output.xlsx')

input("PRESS ENTER TO EXIT.")



