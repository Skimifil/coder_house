import pandas as pd

df_csv = pd.read_csv("cancer_data.csv", sep=",", decimal=".")
print(df_csv.head())

df_excel = pd.read_excel("fastfood.xlsx", sheet_name="fastfood")
print(df_excel.head(515))

df_excel.to_csv("fastfood2.csv",sep=";", index=False)

dataframe_manual = pd.DataFrame({'nome': ['John', 'Leandro'], 'idade': [45, 28]})
print(dataframe_manual.info())
print(dataframe_manual.shape)
print(dataframe_manual.describe().round(2))
