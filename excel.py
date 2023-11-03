import pandas as pd

# Excel dosyasını oku
input_file = "Enes Şahin - kulucka_ogrenci_listesi.xlsx"
output_file = "anan.xlsx"

# Veriyi oku
df = pd.read_excel(input_file)

# Veriyi düzenle (örneğin, sütunları filtrele veya dönüştür)
# Örnek: Sadece "Ad" ve "Soyad" sütunlarını al
df = df[["#1$Yiğit$Özan__Elektrik Elektronik Mühendisliği__2", "#2$Efecan$Karatut__Elektrik Elektronik Mühendisliği__2"]]

# Başlıkları yeniden adlandır
df = df.rename(columns={"Ad": "Yiğit ", "Soyad": "Özan"})

# Veriyi yeni bir Excel dosyasına kaydet
df.to_excel(output_file, index=False)

print(f"Excel dosyası düzenlendi ve '{output_file}' olarak kaydedildi.")
