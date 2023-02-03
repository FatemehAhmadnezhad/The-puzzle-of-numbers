# یه عدد بین 1 تا 9 انتخاب کن
# عدد انتخابی رو در 2 ضرب کن
# جواب رو با عدد 8 جمع کن
# جواب رو با عدد اولی که انتخاب کردی جمع کن
# جواب رو منهاب 2 کن
# جواب رو بر 3 تقسیم کن
# عدد اولی که انتخاب کرده بوی رو از جواب کم کن
# جواب رو در 4 ضرب کن
# جواب میشه8
# اولین پروژه
# تاریخ 1400/9/15

number=input('choose a number between 1 - 9:')
# y=int(number)
number=int(number)
number1=number
# x= y*2
number1*=2
# z=x+8
number1+=8
# e=z+y
number1+=number
# r=e-2
number1-=2
# h=r//3
number1//=3
# k=h-y
number1-=number
# l=k*4
number1*=4
# print(l)
print(number1)
