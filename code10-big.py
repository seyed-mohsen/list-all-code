#برنامه ای بنویسید که سن کاندیداهای مجلس شورای اسلامی را از ورودی بخواند و سن بزرگترین آنها را در خروجی چاپ کند. برنامه ی شما تا زمانی به خواندن از ورودی ادامه می دهد که عدد منفی یک وارد نشده باشد. به محض اینکه این عدد در ورودی ظاهر شد برنامه باید خواندن ورودی را خاتمه دهد و بزرگترین سن را چاپ کند. سن افراد در بازه ی ۱۰ تا ۹۰ سال می باشد.
vorodi = (int (input ()))
b = 0
k = 0
while vorodi != -1 :
    if vorodi > b :
        b = vorodi
    vorodi = (int (input ()))
print ( b )