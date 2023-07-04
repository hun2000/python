import shape

x = 5
print(x)

x = 6
y = 1
print(x+y)

# ตัวเลขจำนวนเต็ม Integer
# ตัวเลขเเบบทศนิยม Float     *int กับ float สามารถบวกกันได้
# ข้อความ String    *** ทุกครั้งที่มีข้อความต้องมี ' ' ***
# Boolean มีเเค่ True, False

# *** print ถ้าจะให้เเสดงผลพร้อมกับข้อความต้องมี , เช่น print('Point =', score,'A') ***

x = '5'       # มี ' ' เเสดงว่าเป็นข้อความ
y = '4'
print(x+y)    # ถ้าเป็นข้อความจะเอาข้อความมาต่อกัน
x = int('56')
y = float('0.5')
print(x+y)    # เเปลงข้อความเป็นตัวเลข ถ้าเป็นคนละชนิดกัน(ข้อความกับตัวเลข) ไม่สามารถบวกกันได้
x = '2'
y = str(5)    # แปลงเป็นข้อความ
z=x+y
print(x+y)

x = 5
y = 2
a1 = x + y    # 7
a2 = x - y    # 3
a3 = x * y    # 10
a4 = x / y    # 2.5
a5 = x % y    # 1 เศษที่ได้จากการหาร
a6 = x ** y   # 25 ยกกำลัง
a7 = x // y   # 2 หารเเล้วปัดเสษทิ้ง
print(a1, a2, a3, a4, a5, a6, a7)

x = 5
x += 3     # เขียนได้หลายเเบบมีค่าเท่ากับ x=x+3
           # มี += -= *= /= %= **= //= สามารถใช้ได้
print(x)

x = 8
y = 4
a1 = x > y    # true
a2 = x >= y   # true
a3 = x < y    # false
a4 = x <= y   # false
a5 = x == y   # false เท่ากันหรือไหม เปรียบเทียบใช้ ==
a6 = x != y   # true ไม่เท่ากับ
print(a1, a2, a3, a4, a5, a6)  # จะออกมาเป็นค่า Boolean มีเเค่ true, false

print(' ')
print('การใช้ and, or  บรรทัด 54')
if x > 0 and y > 0 :    # ต้องเป็นไปตามเงื่อนไขทั้ง2อย่าง
    print('1')
if x > 0 or y >10 :     # ต้องเป็นไปอย่างใดอย่างหนึ่ง
    print('2')


#   เงื่อนไข
print(' ')
print('การใช้เงื่อนไข   บรรทัด 62')
p = True
q = False
a1 = p and q  #False
a2 = p or q   #True
a3 = not p    #False

score = 50
if score >= 80:
    print('Grade A')   # ต้องมี Tap(หรือมีเว้นวรรคก็ได้) ให้มา ถ้าไม่มีเเสดงว่าไม่ได้อยู่ใน if
    print('อิอิ')        # *** ควรเป็น Tap มากกว่า เพราะกลัวมีหลายคำสั่ง ***
elif score >=70 :      # elif ..... : คือ มีค่าเท่ากับ else if เเต่ใช้ else if ไม่ได้ ให้ใช้ elif ..... : ต้องมีปิดทกครั้ง
    print('Grade B')
else:                  # *** สุดท้าย else : ***
    print('Grade F')


#   Loop
print(' ')
print('For Loop   บรรทัด 81')   # จะเว้นบรรทัดให้อัตโนมัติ
for i in range(1, 7, 1):  # for ... in range(ตัวเริ่มต้น, limit, โดดทีละเท่าไร) : คือ for ต้องมี ม้า จะวิ่งจากค่าหนึ่งไปอีกค่าหนึ่ง
    double = i*2          # **** ต้องมีตัวปิดด้วย
    print('loop ธรรมดา', double)       # *** range(ตัวเริ่มต้น, limit) จะวิ่งไปไม่ถึง limit ***
for i in range(1, 7, 1):
    if i % 3 == 0:
        continue          # *** ใช้ได้เฉพาะใน loop เท่านั้น ***  เมื่อมันเป็นไปตามเงื่อนไข เเล้วมันจะข้าม loop รอบนั้นไป(skip)
    print('ทดสอบการใช้ continue', i)
for i in range(1, 7, 1):
    if i % 3 == 0:
        break             # break เมื่อทำงานจะหลุดออกจาก loop ทันที
    print('ทดสอบการใช้ break', i)


#   Functions
print(' ')
print('def(การสร้างฟังชั่น)   บรรทัด 97')
def get_box_area(width, length, height):        # def ชื่อฟังชั่น(พารา1, พารา2, พรารา3) :   *** จะมีกี่ตัวก็ได้ หรือไม่มีก็ได้ ***
    if width < 0 or length < 0 or height < 0:   # ... คำสั่งที่จะให้ทำ
        return 0                                # return คือการคืนค่าข้อมูลกลับไปที่มีการเรียกใช้คำสั่งนั้น
    box_area = width * length * height          # เมื่อเจอคำสั่ง return จะหยุดการทำงานของฟังชั่นนั้นทันที
    return box_area                             # return เป็นข้อความก็ได้ (' ')  *** ต้องมี return ทุกครั้ง ***
#   print(box_area)
box1 = get_box_area(4, 4, 2)
box2 = get_box_area(1, 1, 1)
get_box_area(length=1, height=2, width=3)       # สามารถกำหนดตัวแปรลงไปได้เลย
print(get_box_area(4, 4, 2))
print(box1)


#   Modules               ***  คือการสร้างฟังชั่นเเล้วไปเก็บไว้ไฟล์เเยก  ***
        # def get_circle_area(radius):            ก็สร้างไฟล์เเยก เเล้วใส่คำสั่งลงไป จะเหรียกใช้ คือ ชื่อไฟล์.คำสั่งที่ต้องการ
        #     return 22/7 * (radius ** 2)
        # def get_triangle_area(width, height):
        #     return 1/2 * width * height
        # def get_recrtangle_area(width, height):
        #     return width * height
print(' ')
print('การสร้าง modules')
print('ทดสอบต้อง import ก่อน', shape.get_circle_area(10))
import shape as s                       # ต้องมี import ด้วย    ถ้าอยากย่อให้มันสั้นลงก็ใช้คำสั่ง as เเล้วตามด้วยชื่อฟังชั่น
circle = s.get_circle_area(10)          # as ใช้กับ import เท่านั้น
print('พื้นที่วงกลม', circle)
triangle = s.get_triangle_area(10, 6)
print('พื้นที่สามเหลี่ยม', triangle)
print(s.what(3))
print(shape.what(3))
print('ทดสอบ 1', shape.what(3))
print('ทดสอบ 2', s.what(3))
print('ทดสอบ 3', shape.what(3))
circle1 = shape.get_circle_area(10)
print('ทดสอบการไม่ใช้ตัวย่อ', circle1, 'เเต่ต้องมี import ก่อน')

#   Gui basic  การสร้าง desktop application
#   ต้องมี library ก่อนถึงจะทำได้
#   tkinter คือ library สำหรับสร้าง GUI(destop App)
#   เหมือนจะเอาไว้เเสสดงผลบนหน้าจอเว็บมั้ง
def set_message():
    text = text_input.get()    # ดึงค่าจาก Entry มาเก็บไว้ที่ Text ก่อน     get คือคำสั่งที่ดึงข้อความที่กรอกมาใช้งาน
    title_label.configure(text=text)    # configure คือ เปลี่ยนพารามิเตอร์
import tkinter as tk                    # ถ้าจะทำไรที่นอกเหนือจากฟังชันทั่วไปต้อง import เข้ามา เหมือน Modules
window = tk.Tk()                        # Tk() เอาไว้สร้าง หน้าต่าง
window.title('Python01')                # title('ชื่อ App') คำสั่งเอาไว้ต้องชื่อ App
window.minsize(width=400, height=400)   # minsize(width, height) เอาไว้กำหนดขนาดหน้าต่าง
#  ***  UI ใส่หลังจากสร้าง window.minsize เสร็จ เเละก่อนใช้ window.mainloop  ***

title_label = tk.Label(master=window, text='เมื่อรักฉันเกิด')   # ui Label(...) เป็น ui 'ข้อความ' , master คือ label นี้จะไปใส่ลงที่ไหน
title_label.pack()   # pack() จะเป็นคำสั่งให้ .....pack ทำงาน(เเสดงผล)                    #       text คือข้อความที่ต้องการใส่

text_input = tk.Entry(master=window)             # Entry(...) คือ UI สร้างช่องกรอกข้อความ
text_input.pack()    # pack() จะเป็นคำสั่งให้ .....pack ทำงาน(เเสดงผล)
                                                # ถ้าไม่ใส่เล็บ command=...() เมื่อกดปุ่มให้ทำคำสั่งนี้ ถ้าใส่อาจจะรันก่อนกดปุ่ม
ok_button = tk.Button(master=window, text='ok', command=set_message)   # Button(...) คือ UI เอาไว้สร้างปุ่ม
ok_button.pack()     # pack() จะเป็นคำสั่งให้ .....pack ทำงาน(เเสดงผล)            command เมื่อกดใช้งานที่หน้าต่างจะมีฟังชั่นทำงาน
window.mainloop()                       # mainloop เป็นคำสั่งเอาไว้ start application


#    Exercise
#    ทำเเม่สูตรคูณ
import tkinter as tk
def show_output():
    number = int(entry.get())
    if number == 0:
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
