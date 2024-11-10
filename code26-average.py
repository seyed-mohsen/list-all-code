#1-معدل هر فرد را محاسبه کند و همراه با نام هر فرد ذخیره کند، ترتیب خروجی اسامی باید دقیقا مساوی ترتیب فایل ورودی باشد. 
#2-معدل ها را به ترتیب صعودی همراه با نام هر فرد ذخیره کند. لطفا توجه کنید اگر از dict استفاده می کنید ترتیب معدل ها در آن مشخص نیست برای اطلاعات بیشتر به این لینک مراجعه کنید. https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries
#۳-سه معدل برتر را با نام هر فرد ذخیره کند
#۴-سه معدل پایین را بدون نام هر فرد ذخیره کند.
#5-میانگین معدل ها را محاسبه و ذخیره کند.
import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name , output_file_name):
    with open (input_file_name, 'r') as fin :
        rider = csv.reader(fin)
        with open (output_file_name,'w',newline = '')as fot:
            for i in rider :
                name = i [0]
                adad = list(map(int,i[1:]))
                gread = mean(adad)
                rite = csv.writer(fot)
                rite.writerow([name,gread])

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name , 'r')as fin :
        rider = csv.reader(fin)
        num1 = []
        with open (output_file_name , 'w' , newline = '')as fot :
            for i in rider :
                name = i [0]
                adad = list(map(int,i[1:]))
                gread = mean(adad)
                num1.append([name,gread])
            sort = sorted(num1,key=lambda x : (x[1],x[0]))
            rite = csv.writer(fot)
            rite.writerows(sort)

def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name , 'r')as fin :
        rider = csv.reader(fin)
        num1 = []
        with open (output_file_name , 'w' , newline = '')as fot :
            for i in rider :
                name = i [0]
                adad = list(map(int,i[1:]))
                gread = mean(adad)
                num1.append([name,gread])
            sort = sorted(num1)
            one_sort = sorted(sort,key=lambda x : (-x[1],x[0]))
            up = one_sort[:3]
            rite = csv.writer(fot)
            rite.writerows(up)

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name , 'r')as fin :
        rider = csv.reader(fin)
        num1 = []
        with open (output_file_name , 'w' , newline = '')as fot :
            for i in rider :
                name = i [0]
                adad = list(map(int,i[1:]))
                gread = mean(adad)
                num1.append([gread])
            sort = sorted(num1)
            lower = sort[:3]
            rite =csv.writer(fot)
            rite.writerows(lower)

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name , 'r')as fin :
        rider = csv.reader(fin)
        num1 = []
        with open (output_file_name , 'w' , newline = '')as fot :
            for i in rider :
                name = i [0]
                adad = list(map(int,i[1:]))
                gread = mean(adad)
                num1.append(gread)
            num1 = [mean(num1)]
            rite = csv.writer(fot)
            rite.writerows([num1])