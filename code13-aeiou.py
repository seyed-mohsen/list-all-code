#۱ - تمامی حروف صدادار رو پاک کنه.
#۲ - قبل از هر حرف بی صدا یک نقطه چاپ کنه.
#۳ - تمام حروف بی صدا که باقی مانده اند را به صورت کوچک بنویسد
def remove(string):
    vol = 'aeiou'
    res = ""
    for chek in string:
        if chek.lower() not in vol :
            res += chek.lower()
    return res

vorodi = input('')
output = remove(vorodi)
for chek in output :
    print('.' , end = '')
    print(chek, end = '')
print()