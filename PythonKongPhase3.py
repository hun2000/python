print('\t\tException ข้อผิดพลาดจากการเขียนเเล้วทำให้โปรเเกรมผิดพลาด')
# โปรเเกรมกำลังทำงานเเล้วมีข้อผิดพลาดขึ้นมาในการรันโปรเเกรม เเล้วโปรเเกรมไม่สามารถจัดการข้อผิดพลาดได้ จะเกิด => Exception
# เช่น ต้องการบวกเลข เเต่กรอกข้อความมาเเทน => Exception
# ไม่ใช่ error จากการเขียนโปรเเกรม
# x = 20+10
# print(x)
# z = int(input('ป้อนตัวเลข'))
# a = int(input('ป้อนตัวเลข'))
# y = z/a
# print(y)  # Exception ที่ทำให้ error เช่น ไม่กรอกตัวเลข หารด้วย0

print('\t\t try-Except')
try:
    x = 2  # int(input('ป้อนตัวเลข '))
    y = 3  # int(input('ป้อนตัวเลข '))
    print('{}/{} = {}'.format(x, y, x/y))
except:   # error อะไรก็ตามจาก try จะไปที่ Exception
    print('error')

print('\t\tจัดการณ์ Exception หลายเหตุการณ์  (ไม่ใช่ error จากการเขียนโปรเเกรมนะ)')
# case error กรณี Exception
    # ValueError   =>  ค่าที่ป้อนเข้ามาไม่ตรงกัน
    # ZeroDivisionError   =>  ไม่สามารถหารด้วย 0 ได้
    # TypeError  => เช่น int + str
    # NameError => ไม่มีข้อมูลเเล้วเอามาทำอะไรสักอย่าง เช่น x = a+20 เเต่ไม่ทราบข้อมูลของ a  a=?
try:
    x = 2   # int(input('ป้อนตัวเลข '))
    y = 20  # int(input('ป้อนตัวเลข '))
    print('{}/{} = {}'.format(x, y, x/y))
except ValueError:
    print('บอกว่าให้ป้อนตัวเลข')
except ZeroDivisionError:
    print('ไม่สามรถหารด้วย 0 ได้')
except TypeError:
    print('ชนิดข้อมูลไม่ตรงกัน')
except NameError:
    print('')

#  ***********************************************************************
try:
    x = 2   # int(input('ป้อนตัวเลข '))
    y = 0  # int(input('ป้อนตัวเลข '))
    print('{}/{} = {}'.format(x, y, x/y))
except Exception as E:  # Exception เป็น object คือ คลังเก็บรายชื่อ Exception ทั้งหมด
    print(E)

print('\t\ttry except else => ถ้าที่ try ไม่ Exception จะไปทำงานที่ else ต่อ')
try:                          # ไม่ใช่ error จากการเขียนโปรเเกรมนะ
    x = 20   # int(input('ป้อนตัวเลข '))
    y = 5    # int(input('ป้อนตัวเลข '))
    print('{}/{} = {}'.format(x, y, x/y))
except:
    print('Error')
else:  # เมื่อที่ try ไม่ error จะมาทำงานที่ else ต่อ  ไม่ใช่ error จากการเขียนโปรเเกรมนะ
    print('จบการทำงาน')

print('\t\ttry except finally => จะ error ไม่ error ที่ try ก็จะทำงาน finally')
try:
    x = 20   # int(input('ป้อนตัวเลข '))
    y = 0    # int(input('ป้อนตัวเลข '))
    print('{}/{} = {}'.format(x, y, x/y))
except:
    print('Error')
finally:  # จะ error ไม่ error ที่ try ก็จะทำงาน finally  **********************************************
    print('จะ error ไม่ error ที่ try ก็จะทำงาน finally (ไม่ใช่ error จากการเขียนโปรเเกรมนะ)')

print('\t\ttry except ทำงานร่วมกับ while')
while True:
    try:
        x = 0  #int(input('x = '))
        y = 0  #int(input('y = '))
        if x == 0 and y == 0:
            break    # เมื่อ x = 0 and y = 0 จะหลุดออกจาก while
        print('{}/{} = {}'.format(x, y, x / y))
    except:
        print('Error')

print('\t\tสร้าง Excrption ด้วย Raise')
try:
    name = 'Hun'  # input('ป้อนชื่อของคุณ : ')
    if name == 'Hun':
        raise Exception('ชื่อ Hun มีคนใช้เเล้ว')   # มันเจอคำสั่งนี้ก่อนเลยข้ามไปที่ Exception เลย
    x = -5  #int(input('x = '))
    y = -2  #int(input('y = '))
    print(x, y)
    if x < 0 or y < 0:
        raise Exception('ไม่สามารถป้อนค่าติดลบได้')
    print('{}/{} = {}'.format(x, y, x / y))
except Exception as E:
    print(E)

try:
    name = 'Hun'
    if name == 'Hun':
        raise Exception('ชื่อ Hun มีคนใช้เเล้ว')
except Exception as E:  # ถ้าไม่ as E เดี๋ยวตัวโปรเเกรมจะมองว่า Exception เป็น Object
    print(E)


print('\n\t\tAssignment โปรเเกรมบัญชีธนาคาร')
account = {'A':5000, 'B':0}
def getbalance():
    print('ยอดเงินคงเหลือในบัญชี ', account)
def deposit(money):  # สำหรับฝากเงิน
    if type(money) is str or type(money) is bool:
        raise Exception('ป้อนตัวเลขเท่านั้น')
    if money <= 0:
        raise Exception('ฝากเงินติดลบไม่ได้')
    print('ฝากเงินเข้าบัญชี A =>', money)
    account['A'] += money
    print('ยอดเงินคงเหลือในบัญชี ', account)
def withdraw(money):  # ถอนเงิน
    if type(money) is str or type(money) is bool:
        raise Exception('ป้อนตัวเลขเท่านั้น')
    if money <= 0:
        raise Exception('ถอนเงินติดลบไม่ได้')
    if money > account['A']:
        raise Exception('เงินในบัญชีไม่พอที่จะถอน')
    print('ถอนเงินเข้าบัญชี A =>', money)
    account['A'] -= money
    print('ยอดเงินคงเหลือในบัญชี ', account)
def transfer(money):  # โอนเงิน
    if type(money) is str or type(money) is bool:
        raise Exception('ป้อนตัวเลขเท่านั้น')
    if money <= 0:
        raise Exception('โอนเงินติดลบไม่ได้')
    if money > account['A']:
        raise Exception('เงินในบัญชีไม่พอที่จะโอน')
    print('โอนเงินจาก A ไป B =>', money)
    account['B'] += money
    account['A'] -= money
    print('ยอดเงินคงเหลือในบัญชี ', account)

try:
    getbalance()
    deposit(60000)
    transfer(-600)
    transfer('5687')
    transfer(True)
except Exception as E:
    print(E)


print('\n\t\tFile')
"""
open('ชื่อไฟล์', 'โหมด', 'ระบุก็ได้ ไม่ระบุก็ได้  =>  การเข้ารหัส')
โหมด(mode) => 'r' = read อ่านได้อย่างเดียว
           => 'w' = write เขียน ถ้าไม่มีไฟล์นี้ก็จะสร้างขึ้นมาใหม่ด้วย
           => 'a' = append  ต่อข้อความเข้าไปที่ไฟล์ .txt
           => 'x' = create  สร้างไฟล์เข้ามาใหม่
           => 't' = text file
           => 'b' = binary file ไฟล์ที่เก็บข้อมูลแบบเลขฐาน2
"""
fr = open('text.txt', 'r', encoding='utf-8')  # encoding='utf-8' => เพื่อจะให้อ่านภาษาไทยได้
print(fr.read(5))    # ถ้าจะให้เเสดงผลต้อง .read() จะอ่านทั้งหมดเลย
                     # ถ้าจะให้อ่านกี่ตัวก็ .read(จำนวนตัวที่จะให้อ่าน)
print(fr.read())     # ถ้าอ่านไฟล์ซ้ำมันจะอ่านต่ออันก่อนหน้า

try:
    x = 'Hun.txt'
    f = open('{}'.format(x), 'r')
    print(f.read())
except FileNotFoundError:  # FileNotFoundError => หาไฟล์ชื่อ ... ไม่เจอ
    print('หาไฟล์ {} ไม่เจอ'.format(x))

try:                           # encoding='utf-8' => เพื่อจะให้เขียนภาษาไทยได้
    fw = open('score.txt', 'w', encoding='utf-8')  # สร้างขึ้นมาใหม่พร้อมกับเขียนลงไปได้
    fw.write('Hello Hun\n')
    fw.write('5678\n')
    fw.writelines('สวัสดี')   # .writelines เขียนทีละบรรทัด
    fw.close()  # เปิดแล้วก็ปิดด้วย

    print('\tไฟล์อ่าน')
    fr = open('score.txt', 'r', encoding='utf-8')
    line = fr.readlines()  # .readlines() เก็บข้อมูลเเต่ละบรรทัดเป็น list ถ้าใช้ร่วมกับ loop จะเป็นการดึงมาทีละบรรทัด
                           # .readline() ถ้าใช้ร่วมกับ loop จะเป็นการดึงมาทีละตัว
    print(line)
    print('อ่านไฟล์ได้ว่า ==>', fr.readline())  # .readline() อ่านข้อมูลทีละบรรทัด
    for i in line:
        print(' =>', i)    # อ่านต่อจากบรรทัดเดิม
    fr.close()

    fa = open('score.txt', 'a', encoding='utf-8')  # append เพิ่มข้อมูลเข้าไปจากเดิม
    fa.write('\nสวัสดีวันจันทร์')
    fa.close()
except:
    print('error')

print('\t\tการลบไฟล์ text')
# import os   # os เป็นตัวจัดการไฟล์ โฟเดอร์
# try:
#     if os.path.exists('score.txt'): # เช็กว่ามีไฟล์นี้อยู่ในโปรเเจ็คของเราไหม
#         os.remove('score.txt')
#         print('ลบเเล้ว')
#     else:
#         print('หาไฟล์นี้ไม่เจอครับ')
# except:
#     print('error')


print('Assignment โปรเเกรมคำนวนเกรด')
try:
    # ป้อนข้อมูลเเละคะเเนน
    # fw = open('scores.txt', 'w',encoding='utf-8')
    # while True:
    #     studentid = input('ป้อนรหัสนักเรียน : ')
    #     if studentid == 'exit':
    #         break
    #     score = input('คะเเนนสอบ : ')
    #     fw.writelines(studentid+' '+score+'\n')
    # fw.close()

    # ตัดเกรด
    fr = open('scores.txt', 'r', encoding='utf-8')
    fw = open('grade.txt', 'w', encoding='utf-8')
    # grade = None/
    for line in fr.readlines():  # fr.readlines() เป็น list
        score = int(line[2:].strip()) #=> คะเเนน       # ลบช่อวงว่างออก
        studentid = line[:1]    #=> รหัส
        if score >= 80:
            grade = 'A'
        elif score >= 70:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        elif score >= 50:
            grade = 'D'
        else:
            grade = 'F'
        print('รหัส', studentid, 'คะเเนน', score, 'grade', grade)
        fw.writelines(studentid + ' คะเเนน ' + str(score) + ' เกรด ' + grade + '\n')
    fw.close()
    fr.close()
except Exception as E:
    print(E)


# fr = open('scores.txt', 'r', encoding='utf-8')
# x = []
# for line in fr.readlines():
#     y = line.split(' ')
# print(y)
# fr.close()
#
# h = []
# x = 'qwer qwer qwer qwer qwer qwer'
# y = x.split(' ')
# h.append(y)
# print(h)
fr = open('scores.txt', 'r', encoding='utf-8')
print(fr.readlines())
