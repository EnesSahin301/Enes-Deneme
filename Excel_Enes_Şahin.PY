import pandas as pd
import re

idList = []
isimList = []
soyisimList = []
bolumList = []
sinifList = []

excelDosyasi = 'ogrenci_bilgileri.xlsx'

veri = pd.read_excel(excelDosyasi, header=None)

ogrenciler = veri.iloc[0].tolist()

for i in range(len(ogrenciler)):
    idList.append(re.search(r'#(\d+)', ogrenciler[i]).group(1))
    isimList.append(re.search(r'\$(.*?)\$', ogrenciler[i]).group(1))
    soyisimList.append(re.search(r'\$[^$]*\$([^_]*)__', ogrenciler[i]).group(1))
    bolumList.append(re.search(r'__(.*?)__', ogrenciler[i]).group(1))
    sinifList.append(re.search(r'__(\d+)', ogrenciler[i]).group(1))

bilgilerList = [idList, isimList, soyisimList, bolumList, sinifList]

dataframesList = []
for i in range(len(bilgilerList[0])):
    row_data = {
        'ID': bilgilerList[0][i],
        'İsim': bilgilerList[1][i],
        'Soyisim': bilgilerList[2][i],
        'Bölüm': bilgilerList[3][i],
        'Sınıf': bilgilerList[4][i]
    }
    dataframesList.append(pd.DataFrame(row_data, index=[0]))

yeniVeri = pd.concat(dataframesList, ignore_index=True)

yeniVeri.to_excel('yeni_ogrenciler.xlsx',index=False)
#bu kodu yardım alarak yaptım bazı metotlarla birlikte umarım istediğiniz gibi olmuştur