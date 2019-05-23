import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
  # add Product Name and Color here
})

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115],
],
  columns=['Store ID','Location','Number of Employees'])
  
df = pd.read_csv('sample.csv')  


df3 = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south = df3[['clinic_north','clinic_south']]
df3.iloc[2]
april_may_june = df3.iloc[3:6]
january = df[df3.month=='January']
march_april = df[(df3.month == 'March') | (df3.month == 'April')]
january_feb_march= df[(df3.month.isin(['January','February','March'])]
                       
df4=df.loc[[1,3,5]]                       
df5 = df4.reset_index()
print(df5)

df4.reset_index(inplace = True, drop = True)

print(df4)          
                       
orders = pd.read_csv('shoefly.csv')

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]

print(comfy_shoes)
