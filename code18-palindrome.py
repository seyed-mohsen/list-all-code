#زرگیسو که تازه با برنامه نویسی آشنا شده می خواد برنامه ای بنویسه که تعیین کنه آیا یک کلمه palindrome هست یا خیر. به کلمه ای میگن palindrome که چه از چپ چه از راست بخونیش یه چیز بشه. مثلا Madam یه palindrome هستش ولی tehran یک palindrome نیست. حالا شما باید به زرگیسو کمک کنی این برنامه رو بنویسه.
# لطفا توجه کنید که کوچک یا بزرگ بودن حروف مهم نیست همونطور که گفتیم Madam یک palindrome هست همانطور که maDAM یک palindrome است.
def isPalindrome(s):
 
    return s == s[::-1]
 
s = input().lower()
 
if isPalindrome(s):
 
    print("palindrome")
 
else:
 
    print("not palindrome")