print('\n\tnon-primitive List []')
# primitive เก็บได้ 1-1 1ตัวแปรกับ1ข้อมูล
a = 1
b = 2
c = 3
# non-primitive 1ตัวแปร เก็บได้หลายข้อมูล
number1 = []
number = [1, 2, 3, 4, 5]
name = ['นาย A', 'นาย B', 'นาย C']
all = [12, -10.25, 'Hun', True]  # เก็บ type อะไรก็ได้
# constructor เป็นการประกาศประเภทของข้อมูลนั้นเลย
name1 = list(['นาย A', 'นาย B']) # อันนี้มีค่าเท่ากับบันทัดที่ 9 เเต่เขียแเบบนี้ก็ได้
print('type ของ all =>', type(all))
print(all)

print(' ')
print("'ถ้าเอา str เป็น list มันจะได้เเยกออกมาเลยเช่น 'hun' => ['h', 'u', 'n'] ")
AA = 'hun'
AAA = list(AA)
print(AAA)

print('\t\tการเข้าถึงของ list []')
print(all[1], type(all[1]))
print(all[2], type(all[2]))
print(all[-1], type(all[-1]))
print(all[1:3])    # [start : ก่อนถึง...]
print(all[-2:])
print(all[:3])
print(all[1] + number[1])

print('\t\tการเเก้ไขข้อมูลของ list []')
number = [1, 2, 3, 4, 5]
print('ก่อนเเก้ไข =>', number)
number[1:3] = 5678, 'Hun'
print(number)
number[4] = 'นายไข่'
print(number)

print('\t\tเเสดงผลด้วย loop')
for i in range(len(number)):
    print(number[i])
number = [1, 2, 3, 4, 5]
for i in number:  # ทำได้ 2 เเบบ
    print(i)
sum = 0
for i in number:
    sum += i
print('sumation =>', sum)

print('\t\tการเช็คข้อมูลใน list []')
fruit = ['มะม่วง', 'มะนาว', 'มะยม']
print('มะพร้าว' in fruit)

print('\t\tการนับสมาชิกใน list []')
number = [1, 2, 3, 4, 5]
print(len(number), type(len(number)))

print('\t\tการเพิ่มข้อมูล')
fruit = ['มะม่วง', 'มะนาว', 'มะยม']
print('ก่อนเพิ่ม =>', fruit)
fruit += ['Benz', 'ไก่']     # การเพิ่มข้อมูลเข้าไป
print(fruit)
fruit.append('Oreo')        # การเพิ่มข้อมูลเข้าไป  นำสมาชิกใหม่มาต่อท้ายเพื่อน
print(fruit)
# insert(index, สมาชิกที่จะเพิ่ม เเบบแทรก)
fruit.insert(1, 'กล้วย')
print('หลังใช้ insert =>', fruit)

print('\t\tการลบข้อมูล')
fruit = ['มะม่วง', 'กล้วย', 'มะนาว', 'มะยม', 'ไก่', 'Oreo']
print('ก่อนลบ =>', fruit)
fruit.remove('มะนาว')     # remove ข้อมูลที่อยากเอาออก
print('remove =>', fruit)
fruit.pop()               # remove ข้อมูลสุดท้ายออก
print('pop() =>', fruit)
del fruit[1]             # remove โดยใช้ index
print('del =>', fruit)
# หรือใช้ del fruit ก็จะลบ fruit ออกจากตัวแปรไปเลย เพื่อ clear หน่วยความจำของโปรเเกรม ****************
fruit.clear()            # clear เป็นการลบข้อมูลใน list ออกทั้งหมด เหลือเเต่ => []
print('clear =>', fruit)

print('\t\tการคัดลองข้อมูล')
fruit = ['มะม่วง', 'กล้วย', 'มะนาว', 'มะยม', 'ไก่', 'Oreo']
x = []
print('ก่อน copy =>', x)
x = fruit.copy()       # copy copy fruit ไปใส่ x
print('หลัง copy =>', x)

print('\t\tการรวมข้อมูล')
fruit = ['มะม่วง', 'กล้วย', 'มะนาว']
number = [1, 2, 3]
hun = ['Benz']
print(fruit + number + hun)   # + เอา list 2 หรือ3 หรือมากกว่า มารวมเข้าด้วยกัน เหมือน append

print('\t\tcount')
x = [1, 2, 3, 4, 5, 1, 2, 1, 2, 3]
print('มีเลข 1 count =>', x.count(1), type(x.count(1)))

x = [5, 4]
y = [1, 2]
x.extend(y) # เอาข้อมูลมาใส่สิ่งที่เราต้องการ เอา y ไปใส่ใน x
print(x)

print('\t\tAssignment การเรียงลำดับตัวเลข  .sort')
# number = []
# while True:
#     x = int(input('ป้อนตัวเลขของคุณ : '))
#     if x<0:
#         break
#     number.append(x)
#
number = [5, 8, 75, 1, -20]
print('ก่อน =>', number)
number.sort()             # sort คือการเรียงลำดับจากน้อยไปหามาก
print('หลังเรียง จากน้อยไปมาก=>', number)
number.reverse()            # reverse คือ เรียงสลับกันกับการเรียนล่าสุด
print('หลังจากใช้ reverse', number)

del sum
print('\t\tAssignment การหาค่า มากสุด/ต่ำสุด ผลรวม    max/min  sum')
number = [5, 8, 75, 1, -20]
print(number)
print('ค่ามากที่สุด =>', max(number))
print('ค่าน้อยที่สุด =>', min(number))
print('ผลรวม sum =>', sum(number))   # sum หาผลรวมทั้งหมดของ list

print('\t\tAssignment หากลุ่มเลขคู่/เลขคี่')
number = [5, 3, 2, 7, 8]
odd = []   # เลขคี่
even = []  # เลขคู่
while len(number)>0:
    x = number.pop()
    even.append(x) if x % 2 == 0 else odd.append(x)
number = [5, 3, 2, 7, 8]
print('เลขทั้งหมด =>', number)
print('เลขคู่ =>', even)
print('เลขคี่ =>', odd)

print('\t\tAssignment การเรียงตามดัวอักษร')
x = ['สมพร', 'แก้ว', 'Benz', 'ก้อง', 'ฮั่น', 'กล้า']
print('ก่อนเรียง =>', x)
x.sort()
print('หลังเรียง =>', x)
x.reverse()
print('reverse', x)

x = ['สมพร', 'แก้ว', 'Benz', 'ก้อง', 'ฮั่น', 'กล้า']
x = x[::-1]  # มีค่าเท่ากับ reverse
print('เหมือน reverse', x)

print('\t\tAssignment ยกกำลัง')
number = [1, 2, 3, 4, 5, 6]
# ปกติ
print(number)
for i in range(len(number)):
    number[i]= number[i]**2
print(number)

number = [1, 2, 3, 4, 5, 6]
x = []
for i in number:
    x.append(i*i)
print(x)

number = [1, 2, 3, 4, 5, 6]
# ลดรูป  *************************************************************************************
number = [i*i for i in number]
print(number)

print('\t\tจับคู่ list with list   zip')
fruit = ['มะม่วง', 'กล้วย', 'ฝรั่ง']
price = [20, 50, 30]

for x,y in zip(fruit, price[::-1]):
    print('สินค้า =', x, 'ราคา =', y)

print('\t\tAssignment เกี่ยวกับ zip')
# ปกติ  **************************************************************************************
greeting = ['Hi', 'Hello', 'Good morning']
people = ['Kong', 'Gam', 'Jo']
h = []
for x in greeting:
    for y in people:
        h.append(x+' '+y)
print(h)
# ลดรูป  *************************************************************************************
greeting = ['Hi', 'Hello', 'Good morning']
people = ['Kong', 'Gam', 'Jo']
h = [x+' '+y for x in greeting for y in people]
print(h)

print('\t\tAssignment การค้นหาเเละนับจำนวนตัวอักษรใน list')
message = ['aa', 'aba', 'ac', 'bbaaa', 'cca', 'abababa']
result = []
for x in message:
    counts = 0
    for i in range(len(x)):
        if x[i] == 'a':
            counts += 1
    result.append(counts)
print(result)

message = ['aa', 'aba', 'ac', 'bbaaa', 'cca', 'abababa']
result = []
for x in message:
    counts = 0
    for i in x:
        if i == 'a':
            counts += 1
    result.append(counts)
print(result)

message = ['aa', 'aba', 'ac', 'bbaaa', 'cca', 'abababa']
result = []
for x in message:
    result.append(x.count('a'))
print(result)