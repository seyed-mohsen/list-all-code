#sha256 هک با رنگین کمان
from hashlib import sha256
import csv

def hash_password_hack(input_file_name, output_file_name):
    hash_shode ={}
    for i in range(1000,10000):
        h = sha256(b'%i'%i).hexdigest()
        hash_shode[h] = i
    with open(input_file_name , 'r') as fin :
        rider = csv.reader(fin)
        for i in rider :
            name = i[0]
            code = i[1]
            ancode = hash_shode[code]
    with open(output_file_name , 'w' , newline='') as fot :
        riter = csv.writer(fot)
        riter.writerows([name,',',ancode])