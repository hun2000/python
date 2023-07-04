# str คือ ข้อความ ตัวอักษร
# number => int float
# boolean ได้ออกมาเป็น True False
#from turtle import st

print('Hun')
print(float(3.99))
print(-1+20)                 # + int, float คือ ถ้าเป็นตัวเลขจะเอามาบวกกัน
print(True)
print('1\n2\t3')             # \t คือ เว้นวรรค
print('HuN' + 'Ben')         # + ถ้าเป็น str เอา str มาต่อกัน


print('\nData Type & Variable')
# ชนิดข้อมูล เเละการสร้างตัวเเปล
# variable ชื่อตัวเเปร = ค่าที่เก็บในตัวเเปร
x = 20
y = True
print('ผลลัพธ์ ' + str(x))  # แปลงเป็น str ก่อน
print(y)
print(type(x))               # type คือ เช็คชนิดข้อมูล
print(type('Hun'))

a = 'PETER'
print(a.lower())          # แปลงให้เป็นตัวเล็กทั้งหมด


print('\nกฎการตั้งชื่อ')
# ตัวเลข ตัวอัษร เครื่องหมาย
# ห้ามขึ้นต้นด้วยตัวเลข เเละสัญลักษณ์พิเศษ ยกเว้น _
# ห้ามซ้ำกับ keyword(คำที่ถูกจำกัดเอาไว้) เช่น as if elif or not class
# case sensitive คือ จะคิดทั้งตัวพิมพ์เล็ก เเละตัวพิมพ์ใหญ่


print('\nเเถมตัวเอง')
str1 = 'Hello_world'
print(str1[1:6])
print(str1[0])
print(str1 + 'Hun')
print(str1 * 2)


print('\nType conversion')
# การแปลงชนิดข้อมูล
x = 10
y = 3.14
z = '20'
print(type(x))
print(type(y))
print(type(z))
print(x + y)
print(x + y + float(z))  # ต้องแปลงให้เป็นชนิดเดียวกันก่อน
print(str(x) + z)


print('\nfunction input')
# fn = input('Name : ')   # ร้บค่ามาจะเป็น str
# ln = input('Last name : ')
# print(fn, ln)
# print(type(fn), type(ln))
# x = int(input('X = '))
# y = int(input('Y = '))
# print(type(x), type(y))
# print('X + Y = ' + str(x + y))
# # print("what's your name")


print('\nตัวดำเนินการทางคณิตศาสตร์')
# A + B
# A, B => ตัวดำเนินการ Operand
# + => ตัวที่ถูกดำเนินการ Operrator
x = 5
y = 10
print(x+y, x-y, x*y, x/y)
print('หารปัดเศษลง =', x//y)
print('การหารเอาเศษ', x%y)


print('\nตัวดำเนินการเปรียบเทียบ')
# นำข้อมูลอย่างน้อย 2 ค่ามาเปรียบเทียบกัน ชนิดเดียวกัน(str int) ผลลัพธ์ จะออกมาเป็น boolean(True False)
x, y, z = 10, 5, 9
print('ค่า x มากกว่า y หรือไม่ ?', x>y)
print('ค่า x น้อยกว่า y หรือไม่ ?', x<y)
print('ค่า x เท่ากับ y หรือไม่ ?', x==y) # == เป็นตัวดำเนินการเปรียบเทียบ
print('ค่า x ไม่เท่ากับ y หรือไม่ ?', x!=y)
print('x > y > z หรือไม่ ?', x>y and y>z, x>y>z) # ใช้อันไหนก็ได้
print('x < y < z หรือไม่ ?', x<y and y<z, x<y<z) # ใช้อันไหนก็ได้


print('\nตัวดำเนินการทางตรรกศาสตร์')
# and or not ได้คำตอบออกมาเป็น boolean
t = True
f = False
tt = True
ff = False
x = 5>10
print('5>10 :', x)
print('เปรียบเทียบ', t and f)
print('เปรียบเทียบ', t and tt)
print('เปรียบเทียบ', f or t)
print('เปรียบเทียบ', ff and f)
print(not True)


print('\nCompound assignment ตัวดำเดินการเเก้ไข หรืออัพเดท ค่าของตัวแปร')
x = 10
print(x)
x += 5   # มีค่า x = x + 5
print(x)
x -= 15  # มีค่า x = x - 15
print(x)
y = 2
y **= 5  # y = y ** 5
print(y)
# x //= 2
# x %= 2


print('\nลำดับความสำคัญของตัวดำเนินการทางคณิตศาสตร์')
x = 5+2*10  # หลังตามคณิตศาสตร์เลย
print(x)
x = 6*2/3
print(x)
x = 6/3*2
print(x)


print('\nProgram BMI')
# BMI = kg/(m*m)
weight = 60 # int(input('mass(kg) : '))
height = 155 # int(input('height(cm) : '))
process = weight/(height**2)*10000
print('BMI', process)


print('\nโครงส้รางควบคุม Control structure พวก if elif else ,and or not')
# เเบบเลือก if
write = 'HunandBenz'
if 'Hun' in write :
    print("เเสดงว่ามีคำว่า 'Hun' อยู่ใน age")

age = 25 # int(input('อายุของคุณ'))
print('age =', age, 'ปี')
if age >= 15:
    print('คำนำหน้า นาย/นางสาว')
else:
    print('คำนำหน้าเป็น เด็กชาย/เด็กหญิง')
print('จบโปรเเกรม')

if age >= 30:
    print('วัยทำงาน')
elif age >= 20 and age <= 29:
    print('วัยผู้ใหญ่')
elif age >= 15 and age <= 20:
    print('วัยรุ่น')
else:
    print('วัยเด็ก')

z = 20
x = not age == z
y = age == z
if x:
    print('ผ่าน')
print('not', x)
print(y)
print('ไม่ทเ่ากับ != ', z != 2)

age = 14
if age >= 25:
    print('วัยรุ่น')
else:
    print('วัยเด็ก')
# ternary operator
# 'เงื่อนไขที่เป็นจริง' if expression else 'เงื่อนไขอื่นๆ'
print('วัยรุ่น') if age >= 25 else print('วันเด็ก')  # มีค่ากับข้างบน

age = 14 # int(input('age : '))
if age <= 15:
    if age ==15:
        print('ม.3')
    elif age ==14:
        print('ม.2')
    elif age ==13:
        print('ม.1')
    else:print('ประถมศึกษา')
else:
    print('ม.ปลาย')


print('\npass')
# เอาไว้วางโครงสร้างของโค้ดเเต่ยังไม่ระบุไว้ว่าจะให้ทำอะไร
# เราออกเเบบมาเเล้วเเต่ยังไม่รู้จะให้มันทำอะไรก็ใส่passไปก่อนเพื่อให้โค้ดทำงานต่อได้ เเล้วค่อยมาเเก้ทีหลังก็ได้
x = 15
if x <= 20:
    pass
else:pass


print('\nAssignment เปรียบเทียบค่า มาก/น้อย')
x = 10 #int(input('ตัวเลขที่ 1 '))
y = 50  #int(input('ตัวเลขที่ 2 '))
if x > y:
    print(x, '>', y)
else:
    print(x, '<', y)

# หาว่าเป็นเลข คู่/คี่
x = 21 #int(input('ป้อนตัวเลขของคุณ : '))
if x%2 == 0:
    print('เป็นเลขคู่')
else:
    print('เป็นเลขคี่')

print('\nAssignment เเยกเงินออกเป็นกลุ่มๆ')
money = 3200 # int(input('เงินที่ต้องการเเลก : '))
print('1000 => ', money//1000, 'ใบ')
money %= 1000
print('500 => ', money//500, 'ใบ')
money %= 500
print('100 => ', money//100, 'ใบ')

print('\nAssignment แปลง ค.ศ. พ.ศ.')
x = 2001 # int(input('ค.ศ. :'))
print('พ.ศ.', x + 543)

print('\nAssignment BMI')
weight = 68 # int(input('mass : '))
height = 183 # int(input('tall : '))
BMI = weight/(height*height/10000)
print('BMI', BMI)
if BMI < 18.5 :
    print('ต่ำกว่าเกณฑ์')
elif BMI >= 18.5 and BMI <=22.9:
    print('สมส่วน')
elif BMI >= 23 and BMI <=24.9:
    print('น้ำหนักเกิน')
else: print('โรคอ้วน')


print('\n\tเจาะลึก String')
name = 'Weeraphat Studio'  # index
print(name[0:3])  # ก่อนถึงจุดสุดท้าย
print(name[:3])   # มีค่าเท่ากับข้างบน
print(name[:11])  # ถ้ามีช่องว่าก็นับด้วย
print(name[-1])   # เอาเเค่ตัวที่-1
print(name[-6:])  # นับถอยหลังมา6ตัวเเล้วเอาทั้งหมด
print(len(name))  # เอาไว้นับ string นับช่องว่าด้วย
hun = ' h un '
print(hun.strip())   # strip เอาไว้ลบช่องว่างซ้ายเเละขวา
print(hun.lstrip())  # lstrip ลบช่อวงด้วยซ้าย
print(hun.rstrip())  # rstrip ลบช่องว่างด้านขวา

print(name.upper())       # upper ทำให้เป็นตัวใหญ่ทั้งหมด
print(name.lower())       # lower ทำให้เป็นตัวพิมพ์เล็กทั้งหมด
print(name.capitalize())  # capitalize ทำให้คัวเเรกเป็นตัวใหญ่ตัวเดียว
Hun = 'เกิดวันที่ 5 เดือน 5'
print(Hun.replace('5', '6', 1))  # replace เปลี่ยนข้อความใหม่ สารมารถระบุได้ว่าเปลี่ยนตำเเหน่งไหน
print('เดือน' in Hun)  # เอาไว้เช็ค จะคืนค่ากลับมาเป็น boolean
if 'เดือน' in Hun:
    Hun = Hun.replace('เดือน', 'ปี')
print(Hun)

x = 56
y = '5678'
print(x, y, sep='-') # เอาระหว่าง , มาต่อกันด้วย -

print('\tFormat')
fname = 'Weeraphat'
lname = 'Yian'
age = '20'
salary = 500.95555
x = 20
a = 5
print(f'ฉันอายุ {x+a}')
print('1 ชื่อต้น '+fname+'\tนามสกุล '+lname+'\tอายุ '+age)
print('2 ชื่อต้น {} นามสกุล {} อายุ {}'.format(fname,lname,age))
print('3 ชื่อต้น {0} นามสกุล {1} อายุ {2}'.format(fname,lname,age))
print('4 ชื่อต้น {3} นามสกุล {1} อายุ {2}'.format(fname,lname,age,'Programmer'))
print('5 ชื่อต้น {3} นามสกุล {1} อายุ {2} เงินเดือน {4:.2f}'.format(fname,lname,age,'Programmer',salary))
print('6 ชื่อต้น {one} นามสกุล {two} อายุ {three}'.format(one=fname,two=lname,three=age))

print('{0:.2f}'.format(BMI))   # สามารถกำหนดทศนิยมเเบบนี้ได้


fruit = 'ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด เเวะไปสวนทุเรียนด้วย'
print(fruit.count('ทุเรียน'))    # count เอาไว้นับคำที่ต้องการในประโยคว่ามีกี่ครั้งที่ใช้คำนั้น

name = 'นายกอไก่ ใจดี'
print(name.startswith('นาย'))  # startswith เอาไว้เช็คว่าขึ้นต้นด้วยคำที่ต้องการไหม

x = '1150'
print(x.endswith('0'))  # endswith เอาไว้เช็คว่าลงท้ายด้วยคำที่ต้องการไหม


print('\tAssignment ง่ายๆเกี่ยวกับ temp')
c = (f-32)*5/9
f = c*9/5+32
temp = '-4f' #input('ป้อนอุณหภูมิ : ')   # 45c
degree = temp[:-1]
unit = temp[-1].upper()
if unit == 'C':
    degree=int(degree)
    result1 = degree*9/5+32
    unit1 = 'F'

elif unit == 'F':
    degree=int(degree)
    result1 = (degree-32)*5/9
    unit1 = 'C'

print('{} {} = {} {}'.format(degree,unit,result1,unit1))


print('\n\twhile loop')
i = 1
while i <= 3:                     # ทำงานเมื่อเงื่อนไขที่เป็นจริง
    print('Hello world {}'.format(i))
    i+=1

i = 1
sum = 0
while i <= 5:
    sum+=i
    i+=1
print(sum)


print('\n\tfor loop')
for i in range(3):  #for i in range(start, limit, step)
    print('hello world {}'.format(i))

for i in range(2, 10, 3): # เริ่มที่ 2 เเล้วกระโดดทีละ 3 จนถึง 10
    print('รอบที่', i)

sum = 0
for i in range(-10, -1, 2):
    print('i =', i)
    sum += i
print('summation i =', sum)

i=1
while i<=3:
    j=1
    while j<=5:
        print('รอบที่ i', i,'ตำเเหน่งที่ j', j)
        j+=1
    i+=1

for i in range(1,4):
    print('รอบที่ i', i)
    for j in range(1,6):
        print('ตำเเหน่งที่ j', j)

print('\n\tAssignment calculator')
# number = int(input('เเม่สูตรคูณ : '))
start = 2
stop = 3
for i in range(start, stop+1):
    print('เเม่สูตรคูณเเม่ :', i)
    for x in range(1,13):
        print(i, 'X', x, '=', i*x)


print('\n\tbreak continue สำหรับ loop')
i=1
while i<=10:
    print(i)
    if i==5:
        break    # หยุดการทำงานของ loop นั้น
    i+=1

i = 1
while i <= 5:
    x = 1
    while x <= 5:
        print(i, x)
        if x == 4:
            # pass
            break
        x+=1
    i+=1

i=0
while i<=7:
    i += 1
    if i%2==1:
        continue   # จะ skip ไปรอบถัดไป
    print(i)

for i in range(1, 10):
    if i%2==0:
        continue
    print(i)

print('\n\tAssignment หาค่าเฉลี่ย')
# start, stop =1, 5
# sum = 0
# while start<=stop:
#     number = int(input('ตัวเลขของคุณ '))
#     sum +=number
#     start+=1
# print('ผลรวม =', sum)
#
# sum = 0
# A = 0
# while A!=100:
#     number = int(input('ป้อนตัวเลข : '))
#     sum+=number
#     A = number
# print('ผลรวม', sum)
#
# sum = 0
# while True:
#     number = int(input('ป้อนตัวเลข : '))
#     sum+=number
#     if sum>=100:
#         break
# print('ผลรวม', sum)

print('\tAssignment หาตัวเลข  มากสุด/น้อยสุด')
# max1, min1 =0, 9999
# while True:
#     number = int(input('ป้อนตัวเลข : '))
#     if number<=0:
#         break
#     if number>max1:
#         max1=number
#     if number<min1:
#         min1 = number
# print(min1, max1)
#
# A = []
# while True:
#     number = int(input('ป้อนตัวเลข : '))
#     if number <= 0:
#         break
#     A.append(number)
# print(A)
# print(min(A), max(A))

print('\tAssignment สร้างตัวเลขเเบบขั้นบันได')
last = 5 #int(input('ป้อนตัวเลข : '))
for x in range(1, last+1):
    A = ''
    H = ''
    for z in range(last, x, -1):
        H += ' '
    for y in range(1, x*2):
        A += str(y)
    print(H+A)

for x in range(1, last+1):
    for y in range(1, x+1):   # ************
        print(y, end='*')     # คำว่า end='คำที่ใช้เชื่อม' คือ เอาคำข้างหน้ามาต่อกับคำข้างหล้งด้วยคำเชื่อม โดยไม่ขึ้นบรรทัดใหม่
    print('/')                # เหมือนกับ str('A')+'B' => AB เเล้วถ้าเชื่อมเสร็จก็จะขึ้นบันทัดใหม่

print('\tAssignment สร้าง4เหลี่ยมจัตุรัส')
A = 5 #int(input('ป้อนตัวเลข : '))
for x in range(1, A+1):
    for y in range(1, A+1):
        print('*', end='')
    print(' ')


print('\n\tสร้างตารางหมากฮอส')
A = 8
for x in range(1, A+1):
    for y in range(1, A+1):
        if (x+y) % 2 == 0:
            print('O', end='')
        else:
            print('X', end='')
    print(' ')

# print('มันคือวิธีเดียวกัน เเต่เขียนให้สั้นลง')
# for x in range(1, A+1):
#     for y in range(1, A+1):
#         print('O', end='') if (x+y) % 2 == 0 else print('X', end='')
#     print(' ')

print(' ')
for x in range(1, A+1):
    for y in range(1, A+1):
        print('X', end='') if x == 1 or x == A or y == 1 or y == A else print(' ', end='')
    print(' ')


print('\n\tสร้างเกมทายลูกเต๋า class Random')
import random
myrandom = random.randrange(1, 7)
# print(random.randrange(1, 7)) # random ตั้งเเต่ 1-6
# print(random.randint(1, 6))  random ตั้งเเต่ 1-6
k = 1
correct = False
while k<=3:
    numbers = int(input('ป้อนคำตอบของคุณ : '))
    correct = myrandom == numbers
    if numbers == myrandom:
        print('ถูกต้อง')
        break
    print('สูงกว่านี้') if numbers < myrandom else print('ต่ำกว่านี้')
    k+=1
if not correct:
    print('เฉลย {}'.format(myrandom))