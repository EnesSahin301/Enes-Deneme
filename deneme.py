import datetime
tarıh = input("tarih giriniz ")
tarıh = tarıh.split(".")
bugun = datetime.datetime.now()
yarın = datetime.datetime(int(tarıh[0]),int(tarıh[1]),int(tarıh[2]))
fark = bugun-yarın
print(str(fark.days)+" Gün Olmuştur")