#برنامه ای بنویسید که یک عدد از ورودی بخواند اولین مضرب بعدی ۱۰ که بزرگتر از این عدد است را چاپ کند. به عنوان مثال در صورتی که از ورودی عدد ۱۱ خوانده شد باید عدد ۲۰ چاپ شود. اگر عدد ۴۰ خوانده شد باید عدد ۵۰ چاپ شود.
asl = ( int ( input ()))
badi = ((asl-(asl %10))+10)
print ( badi )
