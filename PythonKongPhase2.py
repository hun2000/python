print('\t\tfunction หลักการใช้งาน อะไรมีผลกับอะไร  def')
# โปรเเกรมย่อยที่อยู่ในโปรเเกรมหลัก
# สาเหตุที่ต้องเขียนฟังก์ชั่น => เเก้ปัญหาการใช้ซ้ำๆ จัดให้เป็นกลุ่มๆ

# การสร้างฟังก์ชั่น / เรียกฟังก์ชั่น
# def ชื่อฟังก์ชั่น():
#     statement
def sayhi():
    print('Hello')

def saythai():
    print('สวัสดี')

saythai()  # เรียกฟังก์ชั่น

def add(x, y):
    return x+y

# Global variable => ตัวแปลทำงานทั่วโปรเเกรม / Local variable => ตัวแปลทำงานในฟังก์ชั่นนั้นๆ
def displaynumber():
    # statement
    x = 10          # เป็นเเบบ local คือใช้ได้เฉพาะในฟังก์นั้นๆเท่านั้น   เมื่อจบการทำงาน มันจะไม่เอาไปรวมกับ Global ***********
    a = 50
    print('Hello', x+x, 'ใน')   # x Global มีผลใน def เเต่ว่ามันถูกทับซ้อนเข้าไปก่อนเลยออกมาเป็น 10 ******************
x = 20              # เป็นเเบบ Global ทุกที่สามารถเข้าถึงได้   ***********
displaynumber()
print('Hello', x, 'นอก')   # ตัวเแปลที่อยู่ใน def จะไม่สงผลต่อข้างนอก => Local variable จะไม่ออกมาข้างนอก ************
# print(a)   มันจะ error เพราะว่ามันหา a ไม่เจอ => a จะมีผลในเเค่ local เท่านั้น  ************************************
             # ตัวแปล a จะไม่่หลุดออกมาเป็นตัวแปลของ Global
             # ข้างนอกเอาไปใช้ในข้างในได้ เเต่ข้างในเอาไปใช้ในข้างนอกไม่ได้    *****************************************
             # Global variable => ตัวแปลทำงานทั่วโปรเเกรม / Local variable => ตัวแปลทำงานในฟังก์ชั่นนั้นๆ  **********

print('\t\tการรับค่าเข้ามาในฟังก์ชั่น')
def mydata(name, lname):
    print('first name =>', name, ', last name =>', lname)
x = 'Hun'
y = 5678
mydata(x, y)

# อธิบายความเเตกต่าง Arguments / Parameter
# Arguments => ค่าที่ส่งเข้าไปในฟังก์ชั่น ตอนเรียกใช้ฟังก์ชั่น => x, y
# Parameter => ค่าตัวแปลที่รับข้อมูลมาทำงานจาก Argument => name, lname
# อาส่ง-พารับ    **********

# ตัวอย่าง
def addition(a, b):
    print(a+b)
addition(5, 9)
# 5, 9 => aguments
# a, b => parameter

print('\t\tAssignment เลขคู่ / เลขคี่')
def searchnumber(x):
    print('เลขคู่') if x % 2 == 0 else print('เลขคี่')
searchnumber(10)
searchnumber(13)

print('\t\t*args')
# *agrs
def ad(*args):
    print(args)   # จะได้ออกมาเป็น tuple   เราจะสามารถเพิ่มเข้าได้ไปเลื่อยๆโดยไม่ต้องสร้าง พารามิเตอร์ มารับมัน
def add(*args):
    print(sum(args))
def add1(*args):   # มี่ค่าเท่ากับข้างบน
    total=0
    for i in args:
        total+=i
    print(total)

ad(50, 10, 20, 55)  # จะได้ออกมาเป็น tuple
add(50, 10, 20, 55)
add(10, 20, 20)

print('\t\tkeyword argument')
def display(fname, lname, city):
    print('ชื่อ', fname, 'นามสกุล', lname, 'ที่อยู่', city)
display('Hun', 'Benz', 'KKU')
display(city='BKK', fname='weeraphat', lname='Yian')

def ss(x,y,z=0):   # set default ในการเรียกใช้ฟังชั่นไม่ต้องใส่ค่า z ก็ได้ ถ้าไม่ใส่ก็จะมีค่า = 0 ตามที่ตั้งเอาไว้
    print(x+y+z)
ss(100, 100, 20)

def displayfruit(item):   # สามารถเอา list, tuple มาใช้กับ def ได้
    for i in range(len(item)):
        print(str(i+1)+'.', item[i])

fruit = ['banana', 'water', 'melon']
displayfruit(fruit)

print('\t\tfunction return')
def add1(a,b):
    return a+b
print(add1(5, 40))

# ไม่มีพารามิเตอร์ เเต่ส่งค่าออกไปได้
def show():
    return 500
print(show())

def ssx(x):
    print(x)
    return x**2
h = ssx(3)
print(h)
print(h)   # จะไม่ปริ้นซ้ำกันกับใน def     return เเล้วมันจะหลุดออกจาก loop ให้อัตโนมัติ
print(h)
result = 300-h
print(result)


print('\t\t*args')  # จะได้ออกมาเป็น tuple   เราจะสามารถเพิ่มเข้าได้ไปเลื่อยๆโดยไม่ต้องสร้าง พารามิเตอร์ มารับมัน
def addon(*n):      # ค่าในพารามิเตอร์มีได้หลายค่า ใส่เข้าได้เลื่อยๆ
    print(sum(n))
addon(50, 20, 30, 5)
addon(20, 10)
print('\t\t**kwargs')  # ได้ออกมาเป็น dictionary  เก็บชื่อเเล้วก็ข้อมูล   ได้เลื่อยๆ โดยไม่ต้องสร้างพารามิเตอร์มาลองรับมัน
def dis(**h):   # สร้างมาเพื่อการใช้กับ dictionary   มันสามารถใส่ข้อมูลเข้าไปได้หลสยรูปเเบบ ข้อมูลของเเต่ละคนสามารถใส่เเบบไม่เหมือนกันได้
    print(h)
    print(h['fname'])
dis(fname = 'Weeraphat', lanme='Yian', age = 25)
dis(fname='Hun', city='BKK')


print('\t\tฟังชั่น เรียก ฟังชั่น')
def compare(x, y):
    # return max([x, y])   มีค่าเหมือนกันกับข้างล่าง
    return x if x >= y else y

def equal(x, y, z):
    # return compare(compare(x, y), z)  มีค่าเหมือนกับข้างล่าง
    b = compare(x, y)
    a = compare(b, z)
    return a
print(compare(5, 10))
print(equal(70, 86, 20))

print('\t\tRecursive function การเรียกใช้ฟังก์ชั่นตัวเอง')
def A():   # คล้ายๆการทำ loop ในฟังก์ชั่น   ถ้าทำเเบบนี้มันจะเป็นเเบบไม่สิ้นสุด ต้องหาวิธีออกจากนี่ให้ได้
    print('A')
    A()
# A()   ปิดเอาไว้ไม่งั้นมันจะไม่สิ้นสุด

# *************************************************
# หาจุดวนซ้ำ
# จุดออกfunctionให้ได้(return)
# พารามิเตอร์
def a(number):   # ต้องการ 1-5 โดยไม่ใช้ loop
    print(number)
    if number==5:
        return     # return ใช้ได้กับหลายๆอย่าง    ส่วน break ใช้กับ loop
    number += 1    # return ใช้กับ def มั้ง
    a(number)
a(1)

def summation(x):
    if x==1:
        return x
    else:
        return x+summation(x-1)

print(summation(5))
"""
5 
5 + summation(5-1)
5 + 4 + summation(4-1)
5 + 4 + 3 + summation(3-1)
5 + 4 + 3 + 2 + summation(2-1)
5 + 4 + 3 + 2 + 1 => if 1==1 => True => return
"""

print('\t\tfactorial')
# 5! = 5*4*3*2*1 =120
def factorial(x):
    if x==1:
        return x
    else:
        return x*factorial(x-1)
print(factorial(3))
"""
3!
3 * factorial(3-1)
3 * 2 * factorial(2-1)
3 * 2 * 1 => if 1==1 => True => return
"""

# def f(a):     มีค่าเหมือนกับข้างบนเเต่ใช้ loop
#     x = 1
#     for i in range(1, a+1):
#         x*=i
#     return x
# print(f(5))

print('\t\tfibonacci')
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...
def fibonacci(number):
    if number<=1:
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)
for i in range(5): # 0-4
    print(fibonacci(i))
"""
range(5)
i=1 => 0
i=2 => 0, 1
i=3 => 0, 1, fibonacci(2-1)+fibonacci(2-2) => 0+1 => 1
i=4 => 0, 1, 1, fibonacci(3-1)+fibonacci(3-2) => 1+1 => 2
i=5 => 0, 1, 1, 2, fibonacci(4-1)+fibonacci(4-2) => 2+1 => 3
"""

def fi(a):
    x = [0, 1]
    for i in range(2, a):
        x.append(x[i-1]+x[i-2])
    print(x)
fi(5)

print('\t\tpass')   # เอาไว้ตอนที่ยังไม่รู้จะทำยังไง เเต่ให้โปรเเกรมดำเนินต่อไปได้โดยไม่ error
def getname():
    pass            # เอาไว้ใส่ตรง statement
getname()

print('\t\tlambda function  สร้างขึ้นมาโดยไม่อยากสร้างชื่อให้กับฟังก์ชั่น')
# lambda ก็เหมือนกับ def เเต่ว่า lambda ไม่จำเป็นต้องใส่ชื่อมัน
# lambda argument : statement    statement เป็นการ return เเบบออโต้
# lambda argument : expression
x = lambda name : name

summation1 = lambda x,y : x+y
print(x('Hun'))
print(summation1(34, 5))
multi = lambda a,b:a*b
print(multi(5,10))

def mymulti(x):
    return lambda a:x**a
y = mymulti(5)  # => y = lambda a:5**a
result11 = y(2) # => y(2)
print(result11)


print('\t\tAssignment ฟังก์ชั่นหาผลรวมของตัวเลข เเละค่าเฉลี่ย')
def summationAs(number):
    t = 0
    for i in number:
        t += i
    avg = t/len(number)
    return t, avg
x = [1,2,3,4,5,6,7,8,9,10]
a,b=summationAs(x)
print(a)  # a => เก็บตัวเเปล t => t คือ ผลรวม
print(b)  # b => เก็บตัวแปล avg => avg คือ ค่าเฉลี่ย
print(summationAs(x))

print('\t\tAssignment หาจำนวน ตัวพิมพ์เล็ก/พิมพ์ใหญ่')
def check(message):
    result = {'UPPER':0, "LOWER":0}
    for i in message:
        if i.isupper():
            result['UPPER']+=1
        else:
            result['LOWER']+=1
    print(result)
check('ABcDef')

print('\t\tAssignment เบอร์โทรศัพท์')
data = {'Benz':123456789, 'Hun':634070525, '5678':56789}
def search(message):
    for key,value in data.items():
        print(value) if key == message else print('ไม่เจอ')
search('Benz')

print('telephone number', data['Hun'])

print('\t\tAssignment Tower of hanoi')
# n => จำนวนจาน   เสา => a, b, c   x1 > x2 > x3
def hanoi(n, a, b ,c):
    if n==0:
        return
    hanoi(n-1, a, c, b)  # ย้ายจาน เล็ก,กลาง จากเสา a ไป b
    print('จานที่ {} จากเสา {} ไปเสา {}'.format(n,a,c))
    hanoi(n-1, b, a, c)

hanoi(3, 'A', 'B', 'C')

#
# s = 3
# def Hun(s):
#     return s**2
# if __name__ == '__main__':
#     print('568')
#     print(s**s)
