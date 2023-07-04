# set => {}
# มีค่าได้หลายค่อในตัวแปลเดียว ชนิดข้อมูลต่างกันได้ เเต่ไม่สามารถซ้ำกันได้
# กลุ่มข้อมูล
# list = [] , ชนิดข้อมูลต่างกัน, เเก้ไขสมาชิกได้, ข้อมูลซ้ำกันได้, แสดงผลจากซ้ายไปขวา
# tuple = () , ชนิดข้อมูลต่างกันได้, เเก้ไขข้อมูลไม่ได้, ข้อมูลซ้ำได้, แสดงผลจากซ้ายไปขวา
# set = {} , ชนิดข้อมูลต่างกันได้, เพิ่งข้อมูลได้เลื่อยๆ เเก้ไขข้อมูลไม่ได้ ไม่มี index ให้เข้าถึง นอกจากลบทิ้งเเล้วเพิ่มให้, ข้อมูลซ้ำไม่ได้, ลำดับแสดงผลไม่เเน่นอน จะทำงานได้เร็วกว่า list tuple

# ปกติ
x = {'banana', 'apple', 'watermelon', 5678, True}  # ลำดับการเเสดงผลไม่เเน่นอน หรือ random ในการแสดงผล
print(x, type(x))  # ลำดับการเข้าถึงไม่ชัดเจน เข้าถึงข้อมูลเเบบ index ไม่ได้
# constructor
y = set(['water', 'melon', 55678, False, 'water'])  # ต้องระบุใน [] เหมือนเเปลง list ให้เป็น set
print(y)                                            # จะไม่เเสดงข้อมูลที่ซ้ำออกมา

# การเพิ่มข้อมูลสมาชิก
print('\t\tการเพิ่มข้อมูลของ set => add() / update')
y = set(['water', 'melon', 55678, False, 'water'])
y.add(1)
y.add('banana')
print(y)
print('\t\tการเพิ่มสมาชิกครั้งละหลายๆตัว')
lis = ['water', 'Hun', 27, 'apple']
y.update(lis)  # การเพิ่มสมาชิกหลายตัวใน1ครั้ง  จะเป็น list, tuple ก็เอามาเพิ่มได้เหมือนกัน
print(y)

# loop
for i in y:
    print(i)

print('จำนวนสมาชิก =>', len(y))
print('เช็คข้อมูลใน set =>', 'Hun' in y)

print('\t\tการลบข้อมูลใน set => remove / discard')
set1 = set(lis)
print('ดั่งเดิม', set1)
set1.remove(27)
print('remove =>', set1)
# set1.remove(1)   ถ้าลบข้อมูลเเล้วไม่มีมันจะ error
# print(set1)
set1.discard('มะละกอ')  # ต่อให้มีมี มะละกอ ก็ไม่ error
print('discard =>', set1)
set1.discard('Hun')    # discard คือการลบข้อมูลเหมือน remove    ถ้ามีก็ลบ ถ้าไม่มีก็ ไม่error
print('discard =>', set1)

set1.clear()  # ล้างข้อมูลข้างใน เเต่ยังเหลือตัวแปลไว้อยู่
print(set1)
del set1      # คือการลบตัวเเปลนั้นทิ้งเลย
# print(set1)

print('\n\t\tSet Operation')  # ใช้หลังของคณิตศาสตร์เรื่อง set
# union
a = {'banana', 'apple'}
b = {'berry', 'watermelon'}
all = a.union(b)             # union ก็ตามชื่อเลย เอาหลายๆกลุ่มมาร่วมกัน เเละไม่เเสดงตัวที่ซ้ำกัน
print('union =>', all)                   # หรือใช้ update ก็ได้    x.update(y) เเล้ว print(x)

c = a.copy()  # ก็คือ copy นั่นเเหละ
print('   copy =>', c)

# difference
a = {'banana', 'apple', 'Hun'}
b = {'berry', 'watermelon', 'apple'}
c = a.difference(b)   # เหมือนเอา a - b เเล้วเหลืออะไรก็เอาไปเก็บไว้ที่ c
print('difference =>', c)
a.difference_update(b)  # difference เเล้วก็ update เอาไปเก็บไว้ที่ตัวแปล a เหมือนเดิม    ข้อมูล a ก็จะเปลี่ยนไป    ไม่ต้องสร้างตัวแปลเพิ่ม
print('   difference_update =>', a)

# intersection เอาตัวที่ซ้ำกัน
a = {'banana', 'apple', 'Hun'}
b = {'berry', 'watermelon', 'apple', 'banana'}
c = a.intersection(b)   # เอาตัวที่ซ้ำกัน
print('intersection =>', c)
a.intersection_update(b)  # intersection เเล้วก็ update เอาไปเก็บไว้ที่ตัวแปล a เหมือนเดิม    ข้อมูล a ก็จะเปลี่ยนไป    ไม่ต้องสร้างตัวแปลเพิ่ม
print('   intersection_update =>', a)

# superset
a = {'ไก่', 'นก', 'หมา', 'แมว'}
# subset
b = {'หมา'}
c = {'Hun', 'นก'}
print('\nissubset [b.issubset(a)] =>', b.issubset(a))   # b เป็น subset ของ a ไหม ค่าออกมาเป็น boolean
print('issubset [c.issubset(a)] =>', c.issubset(a))     # c เป็น subset ของ a ไหม ค่าออกมาเป็น boolean
print('issuperset [a.issuperset(b)] =>', a.issuperset(b))   # a เป็น superset ของ b ไหม ค่าออกมาเป็น boolean
print('issuperset [a.issuperset(c)] =>', a.issuperset(c))   # a เป็น superset ของ c ไหม ค่าออกมาเป็น boolean

number = {20, 50, -300, 8000}
print('min =>', min(number))
print('max =>', max(number))


print('\n\t\tfrozen ชอง set')
# ไม่สามารถเปลี่ยนแปลงสมาชิกได้เลย   เพิ่ม ลบ เเก้ไข ไม่ได้เลย   ทำได้อย่างเดียว คือ กำหนดสมาชิกเริ่มต้น ***************************
a = frozenset(['กล้วย', 'มะนาว', 'กล้วย'])
print(a, type(a))
