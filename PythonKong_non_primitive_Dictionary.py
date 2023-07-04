# list
x = [12, 2.35, True, '5678']
print('การเข้าภึง list', x[1])
print('หาว่าอยู่ที่ index ที่เท่าไร', x.index('5678'))

# tuple
x = (12, 2.35, True, '5678')
print('การเข้าภึง tuple', x[3])

# dictionary => key(เข้าถึงข้อมูล):value(ข้อมูล) => str int boolean float
# ตัวแปล = {key:value, key:value, key:value}
# ปกติ
color = {'red': 'เเดง', 'yellow': 'เหลือง', 'green': 'เขียว'}
print(color['red'])
# constructor
animal = dict(cat='แมว', dog='หมา', duck='เป็ด')
print(animal['cat'])
print(animal.get('duck'))

# เปลี่ยนข้อมูล เพิ่มข้อมูล
print('\t\tการเพิ่มข้อมูล เเละการเปลี่ยนข้อมูล')
color = {'red': 'เเดง', 'yellow': 'เหลือง', 'green': 'เขียว'}
color['red'] = 'mango'  # แปลข้อมูล
color['5678'] = 'Hon'   # ถ้า key ไม่มี จะกลายเป็นเพิ่ม key เเละ value เข้ามาเเทน
color.update({'home':'บ้าน', 'mouse':'หนู'})  # หรือใช้คำสั่ง update ก็ได้
print(color)

# loop
print('\t\tloop')
color = {'red': 'เเดง', 'yellow': 'เหลือง', 'green': 'เขียว'}
print(color)
for i in color:
    print(i)    # ภ้าทำเเบบนี้จะได้ key ออกมา

for i in color.values():
    print('\t', i)    # ถ้าอยากได้ value ก็ .values

for i in color.keys():
    print(i)    # ถ้าอยากได้ key ก็ .keys

for i in color.items():
    print('\t', i)    # .items ก็จะได้ทั้ง key เเละ value ออกมาพร้อมกัน เป็น tuple

for k,v in color.items():  # หรือจะเอาเเยกก็ได้
    print('key =', k, 'value =', v)

for k,v in color.items():  # หรือจะเอาเเค่ value ก็ได้ เเค่ key ก็ได้
    print('value =', v)

print('\t\tการลบข้อมูล pop, popitem clear')
color = {'red': 'เเดง', 'yellow': 'เหลือง', 'green': 'เขียว'}
print(color)
color.pop('red')  # การลบสมาชิกโดยเจาะจง
print(color)
color.popitem()   # การลบสมาชิกหลังสุด
print(color)
color.clear()     # เป็นการล้างสมาชิก
print(color)
del color         # ลบตัวแปลทิ้งเลย เพื่อเคลียหน่วยความจำ

print('\t\tการคัดลอง copy')
color = {'red': 'เเดง', 'yellow': 'เหลือง', 'green': 'เขียว'}
x = color.copy()
print(color)
print(x)

print('\t\tdict ซ้อน dict หรือว่าจะซ้อน list tuple ก็ได้')
x = {'ป้าพร':'อาหารตามสั่ง', 'ร้านลุงป้อม':'ผลไม้', 'น่าใจ':'เครื่องดื่ม'}
print(x)
x = {'ป้าพร':
         {'name':'one',
          'menu':
              [
                  'ไก่', 'ไข่'
              ],
          'ราคา':
              (
                  10, 20, 30
              )
          },
     'ร้านลุงป้อม':
         {'name':'two',
          'menu':
              [
                  'หมา', 'กุ้ง'
              ],
          'zone':'ทิศเหนือ'
          },
     'น่าใจ':
         {'name':
             [
                 {
                     '1':1, '2':2
                 },
                 'chang'
             ],
             'zone':'ทิศเหนือ'
         }
     }
print(x)
print('\tการเข้าภึงข้อมูล')
print(x['ร้านลุงป้อม']['menu'][1])
print(x['ป้าพร']['ราคา'][2])
print(x['น่าใจ']['name'][0]['2'])
print(x['น่าใจ']['name'][0])
print(2 in x['น่าใจ']['name'][0])            # ถ้าเป็นเเบบนี้มันจะหมายถึง key ใช่รึป่าว
print(2 in x['น่าใจ']['name'][0].values())   # ต้อง .values() ให้มัน ถึงจะได้ค่า value ออกมา
print('เช็ค =>', 2 == x['น่าใจ']['name'][0]['2'])
print(2 in [1,2,3])
