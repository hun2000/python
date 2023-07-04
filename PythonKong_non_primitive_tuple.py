print('\t\tเจาะลึก tuple ()')
print('# คุณสมบัติคล้ายๆ list เเต่ไม่สามารถเปลี่ยนเเปรงข้อมูลได้')
tup = ('Hun', 5678, 3.11, -20, True)
tups = tuple(('Hun', 5678, 3.11, -20, True))
print('tuple =>', type(tup), tup)
lis = ['Hun', 5678, 3.11, -20, True]
print('list =>', lis)
print('tuple ไม่สามารถเปลี่ยนข้อมูลได้')
print("constructor ก็คือระบุไปเลย เช่น x = tuple((5678, 'Hun', True))")

print('\t\tการเข้าถึงข้อมูล')
tup = ('Hun', 5678, 3.11, -20, True)
print(tup[0:3])  # เวลาเข้าถึงข้อมูลให้เข้าเหมือน list โดยใช้ [] เหมือนกัน  และ [0:3] คือ เริ่มเเละก่อนถึง index ที่ 3
print(tup[0])
print(tup[-3:])
print(tup[1:3])
print(tup[:-3])

print('\t\tการเเก้ไขข้อมูล')
print('เเปรงให้กลายเป็น list ก่อนเเล้วค่อยแปรงกลับ')
tup = ('Hun', 5678, 3.11, -20, True)
print(tup)
# แปลงข้อมูลจาก tuple เป็น list
lis = list(tup)
lis[0] = 'Bangkok'
tup = tuple(lis)
print(tup)
# print(lis)

print('\t\tการเเสดงผลด้วย loop')
tup = ('Hun', 5678, 3.11, -20, True)
for i in tup:
    print(i)

print('\t\tการตรวจสอบข้อมูล')
tup = ('Hun', 5678, 3.11, -20, True)
print('Hun' in tup)
print('ทุเรียน' in tup)
print(True in tup)

print('\t\tการนับสมาชิก len')
tup = ('Hun', 5678, 3.11, -20, True)
# index 0-4
# len 5
print(len(tup))

for i in range(len(tup)):  # เป็นการเข้าถึงโดยใช้ index  0ถึงก่อน5
    print(tup[i])

print('\t\tการสร้าง tuple โดยมี 1 index เเละเพิ่มข้อมูล join')
x = ('Hun') # ถ้าข้อมูลมีตัวเดียวจะกลายเป็น str, int ยกเว้นระบุ constructor
print(x, type(x))
x = ('Hun', )  # ต้องมี , มันถึงจะมองว่าเป็น tuple
print(x, type(x))
x = tuple('Hun')
print(x)   # ถ้าเขียนเเบบนี้มันจะเอา str มาเเตกเป็น tuple

x = ('Hun', 'Benz')
y = ('Nut', )   # y = 'Nut'  =>  x = x + (y,)
x = x + y  # tuple + tuple ได้  จะเรียกเเบบนี้ว่าเป็นการ join tuple
print(x)
# x = ['qewr', 'qwe'] ไม่มีอะไรเเค่เตือนความจำเฉยๆ
# y = '+'.join(x)
# z = y.split('+')
# print(z)

print('\t\tทำงานร่วมกับ list')
tup = ('Hun', 5678, 3.11, -20, True)
lis = list(tup)
lis[0] = 'กรุงเทพ'
tup = tuple(lis)
print(tup)
# อีกกรณี
tup = ('Hun', 5678, 3.11, -20, True)
city = ['ศรีสะเกษ', 'อุบล']
tup = tup + tuple(city)  # ไม่สามารถเอา list + tuple ได้   ต้องแปลงให้เป็น tuple ก่อน
print(tup)

print('\t\tการลบตัวเเปลโดยใช้ del ใช้เเบบ list')
x = (5678, 'qwer')   # เพื่อไม่เปลืองพื้นที่ในหน่อบความจำ
del x
x = (5678, 'HUn', True, -20.5)
lis = list(x)
lis.pop()            # เอาท้ายสุดออกไป
lis.remove(5678)     # เอาข้อมูลที่ต้องการเอาออก เอาออกไป
x = tuple(lis)
print(x)

print('\t\tการนับจำนวน count')
x = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
y = x.count(4)
print(y)

print('\t\tการค้นหาสมาชิกด้วย index')
x = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
y = x.index(2)
print(y)

print('\t\tการเรียงลำดับข้อมูล sorted')
x = ('Korn', 'Pete', 'ข้าวเจ้า', 'John', 'Hun','Anek')
print('before =>', x)
y = sorted(x)
print('after sorted() by tuple =>', y)

x = ('Korn', 'Pete', 'ข้าวเจ้า', 'John', 'Hun','Anek')
y = list(x)
y.sort()
print('after .sort by list =>', y)
y.reverse()
print('reverse =>', y)

print('\t\tAssignment การนำ tuple มาใส่ในตัวแปร')
a, b, c = 10, 12, 15
tup = (a, b, c)
print(tup, type(tup))
tup = (10, 20, 30)
x, y, z = tup
print(x, type(x))
print('{0} + {1} ='.format(x, y), x + y)

print('\t\tAssignment การสลับ tuple')
x = (50, 60)
y = (80, 90)
print('before =>', x, y)
x, y = y, x
print('after =>', x, y)

print('\t\tAssignment tuple => string   join')
x = ('H', 'u', 'n')
y = ''.join(x)  # อยากให้ต่อกันด้วยอะไรก็ใส่ลงไปหน้า join
print(y)

print('\t\tAssignment reverse by tuple')
x = (568, 'Hun')
y = tuple(reversed(x))  # ต้องกำหนดตัวแปลเพิ่ม เเละจะได้ out put ออกมาเป็น object เเล้วมาแปลงเป็น tuple or list ก็ได้
print(y)

print('\t\tAssignment string => tuple')
x = 'Hun_5678'
y = tuple(reversed(x))  # ถ้าใส้ tuple เข้ากับ str ตรงๆตัวเดียว มันจะเเยกออกเป็นทีละตัว
print(y)