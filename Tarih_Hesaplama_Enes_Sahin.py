Years= input(" Bugünün Yılı giriniz ")
Month = input(" Bugünün Ayını Giriniz ")
Day=input("Bugünün Gününü Giriniz ")
Years2 =abs((1919-int(Years))*365)
Month2 =abs((5- int(Month))*30)
Day2 = abs(19-int(Day))
Years3=abs((1923-int(Years))*365)
Month3=abs((10-int(Month))*30)
Day3 =abs(29-int(Day))
BirthdayYears=input("Doğum Yılınızı Yazınız ")
BirthdayMonth=input("Doğum Ayınızı Yazınız ")
BirthdayDay=input("Doğum Gününüzü Yazınız ")
Years4 =abs((int(BirthdayYears)-int(Years))*365)
Month4 =abs((int(BirthdayMonth)-int(Month))*30)
Day4=abs(int(BirthdayDay)-int(Day))
print("Doğum Gününüz "+ str(Years4+Month4+Day4)+" gün önce olmuştur ")
print("Atatürkün Samsuna çıkışı "+ str(Years2+Month2+Day2)+"  gün önce olmuştur  ")
print("Cumhuriyetin ilanı "+ str(Years3+Month3+Day3)+" gün önce olmuştur ")