#سارا به تازگی یادگرفته تایپ کنه و وارد اینترنت بشه. همینکه وارد اینترنت شد تصمیم گرفت وارد یه چت روم بشه و به همه سلام کنه. سارا یه کلمه را توی چت روم وارد کرد. اگه بشه تعدادی از حروف کلمه ای که سارا وارد کرده را حذف کرد و در آخر کلمه ی hello باقی بمونه یعنی سارا تونسته بگه hello در غیر این صورت خیر.
h ='0'
e ='0'
l ='0'
ll ='0'
o ='0'
t = input()
h = t.find('h')
o =t.rfind('o')
ll = t.rfind('l',0,int(o))
l = t.find('l',int(e),int(ll))
e = t.find('e',int(h),int(l))
kam = t[h]+t[e]+t[l]+t[ll]+t[o]
if kam == 'hello' :
    print ('YES')
else :
    print ('NO')