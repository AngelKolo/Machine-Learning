import pandas as pd

df = pd.read_csv('excels.xlsx', sheetname='Sheet1')

lst = []
for i in df.index:
    data = {}
    data['kota'] = df['Kota'][i]
    data['jumlah_penduduk'] = df['Jumlah_Penduduk'][i]
    data['pedapatan_harian'] = df['Pendapatan_Harian'][i]
    lst.append(data)

print(lst)    