#    List   []
#    ใช้รวบรวมข้อมูลหลายๆอันมาเก็บไว้ในกลุ่มเดียวกัน เหมาะกับการจัดกลุ่ม
print('list []')    # list จะเล่นเกี่ยวกับตำเเหน่ง
quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']
print(quests[0])                   # สามารถเลือกตำเเหน่งได้โดย [ ] ตำเเหน่งตัวเเรกเริ่มจาก 0
quests[1] = 'ขูดมะพร้าว1'             # ที่เก็บข้อมูล[ตำเเหน่งที่ต้องการเปลี่ยน] คือ สามารถเปลี่ยนข้อมูลในเเต่ละตำเเหน่งได้
print(quests)
quests.append('ขูดมะพร้าว2')          # ที่ที่อยากจะเพิ่มเข้าไป.append(ข้อความที่ต้องการเพิ่มเข้าไปใน list) คือ การเพิ่มข้อมูลเข้าไปต่อท้ายที่ตำเเหน่งสุดท้ายใน list
print(quests)                                            # มี 2 พารามิเตอร์
quests.insert(2, 'ขูดมะพร้าว3')       # ที่ที่อยากจะเพิ่มเข้าไป.insert(ตำเเหน่ง, ข้อมูล) คือ การเพิ่มข้อมูลไปตำเเหน่งที่เราระบุ
print(quests)
quests.remove('ปลูกต้นมะม่วง')         # ที่ที่อยากจะลบออกไป.remove(ข้อมูลที่ต้องการลบ) คือ ใช้ในการลบข้อมูลออกจาก list
print(quests)

# tuple จะเป็นวงเล็บเล็ก ()  จะไม่สามรถเเก้ไขข้อมูลได้
# Tuple คือ list เเต่ไม่สามารถแก้ไขข้อมูลได้ เหมาะกับการเเสดงผลอย่างเดียว


print(' \nประยุกต์การใช้ list []')
quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']
print('หาจำนวนสมาชิก = '+str(len(quests)))      # len(list) คือ การนับจำนวนสมาชิก(list)  มีค่าออกมาเป็น int
max_quest = 5
if len(quests) <= max_quest :                 # len(list) คือ การนับจำนวนสมาชิก
    quests.append('จับปลาดุก')                  # ที่ที่อยากจะเพิ่มเข้าไป.append(ข้อความที่ต้องการเพิ่มเข้าไปใน list) คือการเพิ่มข้อมูลเข้าตัวสุดท้าย
    print(quests)

quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']
for quest in quests :           # for ... in list คือ สามารถเอา list ใส่เข้าไปได้
    print(quest)                      # quest จะเข้าไปรับค่าทีละค่าที่ละค่าเพื่อมาทำงาน
for i in range(len(quests)):    # สามารถทำได้2วิธี
    print(quests[i])

for i in range(len(quests)):
    print(str(i+1) + '. ' + str(quests[i]))


#   Dictionary    {}
#   จะคล้ายๆกับ list
# ใช้ list ในการเก็บข้อมูลจะลืมว่ามันอยู่ index ไหน
book_data = ['C++', 309, 414]
print(' \nการใช้ Dictionary {}')

book = {'name': 'C++', 'price': 309, 'page': 414}    # ที่เก็บข้อมูล{ชื่อข้อมูล:ข้อมูล} คือ ตำเเหน่งไม่ใช่ตัวเลขเหมือน list
print(book['name'])                                  # book[ชื่อข้อมูล] []ทำเหมือน list เเต่ list ใช้ตัวเลขบอกตำเเหน่ง  ได้ออกมาเป็น str
book['price'] = 500                                  # ที่เก็บข้อมูล[ชื่อข้อมูล] คือ การแก้ไขข้อมูล เช่น การเปลี่ยนราคา
print(book)
book['place'] = 'KKU'                                # ถ้าไม่มีชื่อข้อมูลชนิดนี้จะกลายเป็นเพิ่มข้อมูลเข้าไปเเทน
print(book)                                                 # การเเก้ไขข้อมูล กับการเพิ่มข้อมูลเข้าไป Dictionary ใช้คำสั่งเดียวกัน
book.pop('price')                                    # ที่ที่เก็บค่า.pop(ข้อมูลที่ต้องการลบออกจาก Dictionary) คือ การลบข้อมูลออกจาก Dictionary
print(book)
   # list เหมาะสมกับการเรียงลำดับเพราะว่าจะเข้ากับ loop ได้ดี   Dictionary เหมาะกับการใช้ข้อมูลกระจัดกระจาย จะเรียกใช้ข้อมูลตอนไหนก็ได้


#   string  ชนิดข้อมูลเเบบข้อความ
print('\nstring ชนิดของข้อความ')
message = 'string'
result = len(message)            # len(ข้อความที่ต้องการนับ) ก็สามารถเอามานับตัวอักษรได้ ถ้าใช้กับ string
print(result)
message = 'อะไรน่ะ'                # len(ข้อความที่ต้องการนับ) ถ้าเป็นข้อความภาษาไทยจะนับวรรณยุกต์ด้วย
print(len(message))
print('อะไร' in message)          # สามารถเช็คข้อความย่อยในข้อความใหญ่ได้ จะคืนค่ากลับมาเป็น Boolean คือจะมีค่าเเค่ True เเละ False
print(message.isdigit())         # ข้อมูลที่ต้องการเช็คว่ามีตัวเลขไหม.isdigie() คือ เอาไว้เช็คว่ามีเฉพาะตัวเลขไหม จะคืนค่าออกมาเป็น Boolean

message = 'Just Python'
result = message.upper()              # ข้อความที่ต้องการให้เป็นตัวใหญ่.upper() คือ แปลงตัวอักษรให้เป็นตัวใหญ้ทั้งหมด
print(result)
result = message.replace('Python', 'Rabbit')      # ที่เก็บข้อมูล.replace(คำที่ต้องการเปลี่ยน, คำที่เข้าไปเเทนที่คำเดิม) คือ อยากเปลี่ยนคำในข้อความนั้นๆ
print(result)
message = 'กระต่าย, กระรอก, หมี'
animals = message.split(', ')         # ที่เก็บข้อมูล.split('ข้อความที่ต้องใช้เเบ่งข้อมูล') คือ คำสั่งสำหรับแปลงข้อความให้กลายเป็น list
print(animals)
new_message = '+'.join(animals)       # 'จะให้ต่อเเบบไหน'.join(list) คือ แปลง list ให้เป็นข้อความ
print(new_message)


#    class object มีตัว Medthod ด้วย
# ใช้สร้างสิ่งของขึ้นมาในโปรเเกรม
#  class คือ การสร้าง object ขึ้นมา      เเล้วค่อยเอา object ไปใช้ในโแรเเกรมต่อ     class สร้าง object เเล้วเอา object ไปใช้
print('\nClass Object เเถม Medthod ด้วย')
class Tank :         # class ชื่อclass : คือ การสร้าง class
    def __init__(self, name1, ammo1):               # __init__(self คือ แขกVIP,...) คือ คำสั่งสำหรับสร้าง object
        self.name = name1                           # self คือ เอาค่ามาเเล้วเอาคืนกลับ
        self.ammo = ammo1

    def add_ammo(self, ammo):
        if self.ammo + ammo <= 10:
            self.ammo += ammo
    def fire_ammo(self):
        if self.ammo > 0:
            self.ammo -= 1


first_tank = Tank('กรุ้มกริ่ม', 3)
first_tank.name = 'ก๊องเเก๊ง'                     # สามารถเปลี่ยนค่าได้
first_tank.add_ammo(2)
print(first_tank.name)                        # เวลาเรียกใช้ก็ตามนี้เลย
first_tank.ammo += 2
print(first_tank.ammo)

second_tank = Tank('รถถังคันที่ 2', 6)
second_tank.add_ammo(3)
second_tank.add_ammo(2)                 # เมื่อมันเกินค่าจะไม่มีการบวกเพิ่มเพราะว่าติด if
print(second_tank.name)
print(second_tank.ammo)

# จะจำลองดูการเล่นรถถังดู
import tank
print('/////จะจำลองการเล่นเกมรถถัง โดยการเซ็ดเป็น Module ด้วย/////')
first_tank = tank.Tank('กรุ้มกริ่ม', 3)
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(4)
print(first_tank.ammo)

# นานๆสาระ
print('ข้อคิดว่าทำไม Tk() มาได้')
import tank
import tkinter as t

# Tk ก็คือ class, มี Method ให้เรียกใช้เช่นกัน, Python สร้างมาให้
window1 = t.Tk()
window1.title('แอ๊บแอ้')
window1.minsize(width=400, height=300)

# Tank อันนี้คือ Class ที่เราเป็นคนสร้างเอง
first_tank = tank.Tank('รถถัง', 3)
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(4)
print(first_tank.ammo)


# Math
print('\nMath')
scores = [28, 19, 56, 45, 58]
min_score = min(scores)
max_score = max(scores)
print(min_score)
print(max_score)

import math
A = math.floor(32.5)    # floor คือ ปัดเศษลง
B = math.ceil(32.5)     # ceil คือ ปัดเศษขึ้น
print(A)
print(B)
a = 6
b = 8
c = math.sqrt(a**2+b**2)
print(c)


#  Random
print('\nRandom')
import random
damage = random.randint(50, 60)        # random.randint(ขอบล่าง, ขอบบน) คือ random ออกมาเป็นจำนวนจริง
print(damage)
percent = random.uniform(0, 100)       # random.uniform(ขอบล่าง, ขอบบน) คือ random ออกมาเป็นทศนิยม
print(percent)
if percent < 22.5 :
    damage *= 2
print(damage)

moneys = [0, 20, 100, 1000]
money = random.choice(moneys)        # random.choice(list) คือ random ค่าค่าหนุ่งออกมาจาก list
print(money)
random.shuffle(moneys)               # random.shuffle(list) คือ random สลับลำดับใน list ใหม่หมด เเละมันเเก้ไข list ใหม่เเล้ว return ไปเก็บไว้ที่เดิม
print(moneys)


#  Date
# เกี่ยวกับการทำปฎิทิน
print('\nปฎิทิม')
import datetime as dt                       # datetime คือ module เกี่ยวกับ วัน เวลา
date1 = dt.datetime.now()                   # datetime.datetime.now() คือ วันเวลาตอนนี้     datetime timedelta คือ class
print(date1)
date2 = dt.datetime(year=2020, month=2, day=14)     # datetime.datetime(...) คือ ใช้กำหนดวันเวลาเอง
print(date2)
days = dt.timedelta(days=25, hours=1)        # datetime.timedelta(...) คือ class ใช้สร้างระยะเวลา
day3 = date2 - days
print(day3)

date1 = dt.datetime(year=2020, month=2, day=14, hour=13, minute=30)
date2 = dt.datetime(year=2020, month=2, day=20, hour=16)
days = date2 - date1                    # ใช้หาว่า date2 กับ date1 มันมีระยะเวลาเท่าไร ออกมาเป็นวัน
print(days)
print(date1.strftime('%A %d, %B %Y'))   # strftime(text-เเต่ะละอันมีความหายของมันว่าเอาไว้ทำอะไร เว็บ w3school.com) คือ เอาไว้เปลี่ยนการเเสดงผล
                                        # %a Wed, %A Wednesday, %d(วันที่) 31, %b Dec, %B December, %m(เดือน) 12, %y 18, %Y 2018


#  try except
print('\ntry except')
#  เอาไว้กัน error จากข้อมูลที่เราใส่ไป ไม่ได้ error จากโค้ด    เอาไว้ป้องกันข้อมูลที่ผิดพลาดที่ใส่เข้ามา
try:                           # try คือ safe zone      # try จะมาคู่กับ except
    x = int(input('x = '))          # ถ้า try มีอะไรผิดพลาด(หมายถึงข้อมูลที่ใส่เข้าไป)ขึ้น มันจะรันที่ except
    y = int(input('y = '))          # ถ้า try ไม่มีข้อผิดพลาด(หมายถึงข้อมูลที่ใส่เข้าไป) จะไม่รัน except
    if x == 0 :
        raise Exception()      # raise Exception(ข้อความที่บอกว่าผิดอะไร) คือ โยนความผิดให้กับ try เพื่อให้มันไปรัน except
    z = x / y
    print(z)
except:                        # except คือ สายดิน
    print('ผิดที่ไว้ใจ')

# ทำเเม่สูตรคูณเเบบใช้งานได้จริงๆ โดยใส่ค่าที่ผิดพลาดเข้าไปได้
import tkinter as tk
def show_output():
    # number = 0
    try:
        number = int(entry.get())
        if number == 0 :
            raise Exception()
    except:
        output_lebel.configure(text='Error')
        return
    output = ' '
    for i in range(1, 13, 1):
        output += str(number) + ' x ' + str(i) + ' = ' + str(number * i) + '\n'   # \n คือ การขึ้นบรรทัดใหม่
    output_lebel.configure(text=output)

window = tk.Tk()
window.title('Python multiplication table')
window.minsize(width=400, height=500)
lebel = tk.Label(master=window, text='สูตรคูณเเม่')
lebel.pack(pady=20)                                   # pady คือ ระยะระหว่างเเกน Y
entry = tk.Entry(master=window, width=15)             # สามารถกำหนดขนาดของช่องได้
entry.pack()
button = tk.Button(master=window, text = 'OK', command=show_output, width=15, height=2)
button.pack()
output_lebel = tk.Label(master=window, text=' ')
output_lebel.pack(pady=20)
window.mainloop()
# ถ้าใส่ mainloop บรรทัดที่ 128-129 จะทำให้รันไปทีละโค้ด ถ้าไม่ได้ใส่มันจะรันพร้อมกันทุกอัน