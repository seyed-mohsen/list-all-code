#جهانگیر توی یه شرکت کامپیوتری کار می کنه. قراره جهانگیر برنامه ای بنویسه که تعیین کنه آیا می توان AB و BA رو در یک رشته ی دیگه پیدا کرد بدونه اینکه با هم همپوشانی (overlap) داشته باشن؟ ترتیبش AB و BA هم مهم نیست. یعنی مثلا اگه ورودی ABBA باشه پاسخ YES هست. اگه ورودی BAAB هم باشه بازم پاسخ YES هست. ولی اگه ورودی ABA باشه پاسخ NO هست یا اگه ورودی ABHA باشه بازم پاسخ NO هست. می تونید کمک جهانگیر کنید این برنامه رو بنویسه؟
#لطفا YES و NO را دقیقا به همین شکل با حروف بزرگ در خروجی چاپ کنید.
a = input()
a = a.replace('AB', '!')
a = a.replace('BA', '@')
vaziat = ''
if ('!' in a) and ('@' in a):
    vaziat = 'YES'
else:
    vaziat = 'NO'
print(vaziat)