#آقای ژوبین آرتاباز رئیس سازمان ملل متحد هست و قراره راجع به انتخاب هیئت رئیسه یک رای گیری انجام بده! دادمهر جمشیدی که مسئول کامپیوتر سازمان ملل هست برنامه ای نوشته که می شمره هر کشور چند رائ رو کسب کرده. شما قراره با نوشتن برنامه ای به دادمهر کمک کنید تا آراء رو شمارش کنه.
#خط اول ورودی شامل عدد n هست که تعداد کل آراء رو نمایش میده. هر یک از n خط بعدی شامل اسم یک کشور می باشد. اسم کشورها از حروف کوچک انگلیسی ساخته شده اند.
#در خروجی m خط چاپ کنید که شامل تعداد آراء هر یک از کشورها می باشد. نام کشورها را به ترتیب الفبا در خروجی بنویسید. برای اطلاعات بیشتر به ورودی نمونه و خروجی نمونه مراجعه کنید.
#نکته: سیستم داوری آنلاین از پایتون 3.4 استفاده می کند، در این نسخه دیکشنری ها ترتیب ورود اطلاعات به خود را به یاد نمی آورند و ممکن است در صورت مرتب سازی آنها به نتیجه مطلوب نرسید، برای رفع این مشکل به جای dict از OrderedDict استفاده کنید، این ساختار داده را می توانید از کتابخانه collections در برنامه وارد کنید.
import collections

ted = int(input())
L = []
for i in range(0, ted):
	v = input()
	L.append(v)
#print(L)
d = collections.OrderedDict()
for asm in L:
	d[asm]=d.get(asm,0)+1
#print(d)
kol= list(d.keys())
kol.sort()
for i in kol:
	print(i,d[i])