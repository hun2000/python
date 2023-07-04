# Scope คือ ลำดับขั้นของตัวแปล
print('\nScope ')
human1 = 'จับฉ่าย'

def welcome():
    animal1 = 'กระต่าย'
    animal2 = 'กระรอก'
    print(human1 + ' เดินไปเจอ ' + animal1)
    print(human2 + ' เดินไปเจอ ' + animal2)

human2 = 'เเกงอ่อม'

welcome()   # ว่าลำดับการใช้ฟังชั่นของ welcome อยู่หลังสุดจะกลับไปเรียกก่อนหน้าได้

# Global scope คือ ขอบเขตครอบคลุมพื้นที่โค้ดทั้งหมด ตัวแปล ฟังชั่น คลาส สามารถนำไปใช้ต่อได้
# Global scope เช่น human1 and human2

# Local scope คือ ขอบเขตครอบคลุมพื้นที่โค้ดเเค่ในกรอบของมัน เช่น ตัวเเปลที่เกิดขึ้นในฟังชั่นก็ใช้ได้เเค่ในฟังชั่นนั้นเท่านั้น เช่น animal1, animal2

# username = input('Username = ')
username = 'qwer'
error_message = 'error'
if len(username) <= 4:
    error_message = 'น้อยไปจ้า'
print(error_message)    # ที่จะสื่อก็คือ ถ้าเงื่อนไข if ถูกต้อง ก็สามารถเอาสิ่งที่อยู่ใน if มาใช้งานได้


# lambda
# lambda คือ การสร้างฟังชั่นโดยไม่กี่บรรทัด
print('\nlambda')
def clean_text_1(text):
    return text.strip().capitalize()  # strip() ใช้ลบพื้นที่ว่างในข้อความ
                                      # capitalize() ให้ตัวอักษรตัวเเรกเป็นตัวใหญ่ ตัวที่เหลือเป็นตัวเล็ก

# def clean_text(text): return text.strip().capitalize()   # ทำได้โดยการเอามาบรรทัดเดียวเเบบตรงๆ

clean_text_2 = lambda text: text.strip().capitalize()  # lambda ฟังชั่นพารามิเตอร์(มีได้หลายตัว): คำสั่ง
# lambda สร้างฟังชั่นเเล้วเอาไปเก็บไว้ในตัวเเปล                      # มันจะ return ให้อัตโนมัติ
input_firstname = '     HUN'
output = clean_text_1(input_firstname)
output_firstname = clean_text_2(input_firstname)
print('เเบบ lambda --' + str(output_firstname))
print('เเบบ def --' + str(output))    # print('เเบบ def --'+str(clean_text_1(input_firstname)))

input_lastname = ' benz '
output_lastname = clean_text_2(input_lastname)
print(output_lastname)

# ยกตัวอย่างเช่น
clean = lambda name1, name2: str(name1).strip().capitalize()+' '+str(name2).strip().capitalize()
print(clean(name1='    HUN', name2='benz'))


# map filter zip
# 3 คำสั่ง(mapr-filter-zip)ที่ใช้ร่วมกับ list, tuple
print('\nmap-filter-zip')
question = [
    '    555    ',
    '  2 + 3 = ?  ',
    '  what do you want ?   ',
    'why you leave me ? '
]
# Map
# map มี 2 อย่างสำคัญ คือ ชุดข้อมูล เเละฟังชั่น --- มีชุดข้อมูลเป็นlist, tuple เเล้วจะเเปลไปเป็น map object
# map พูดง่ายๆก็คือ เอา list, tuple ไปใช้กับฟังชั่น เเล้วจะได้ output ออกมาเป็น map object เเล้วเเต่เราว่าจะเอาไปทำอะไรต่อ
# *** map(ฟังชั่น, ชุดข้อมูล) ***
cleaned_question = list(map(lambda q: q.strip().capitalize(), question))
# อธิบายโค้ดข้างบน คือ map จะเอา question มาที่ละตัวจากตัวเเรกไปตัวสุดท้าย เข้ามาทำงานในฟังชั่น lambda เเล้ว q เป็นตัวรับค่าเข้ามา เเล้วเอา q ไปทำงานตามฟังชั่นต่อ สิ่งที่ได้ออกมามันเป็น object เเล้วต้องเเปลเป็น list ก่อน
print(cleaned_question)                                                                            # q.strip().capitalize()
# list one line version
cleaned_question2 = [q.strip().capitalize() for q in question]  # เอาทีละตัวไปทำตามคำสั่งที่ต้องการ เเล้วมี [] เพื่อเเปลเป็น list
print(cleaned_question2)

# Filter
# filter(ฟังชั่นที่เอาไว้ตรวจสอบเเล้วคืนค่ากลับมาเป็น boolean, ชุดข้อมูล) คือ เอาไว้คัดกรองข้อมูล ถ้าอันไหนผ่านก็เอาไปเก็บที่ filter object
filered_question = list(filter(lambda q: len(q) >= 6, cleaned_question2))
print(filered_question)
# filter one line version
filered_question2 = [Q for Q in cleaned_question2 if len(Q) >= 6]  # ทำ for Q in cleaned_question2 if len(Q) >= 6 เเล้วเอาไปเก็บไว้ที่ Q
print(filered_question2)

# Zip
# zip คือ การผูกข้อมูลที่ตำเเหน่ง index เดียวกันมาเข้ากัน เช่น ตำเเหน่งที่ 0 รวมกันกับ ตำเเหน่งที่ 0 ของอีกชุดข้อมูล(list)  เเล้วได้ออกมาเป็น zip object
questionn = [
    ' 5 * 5 = ? ',
    ' 2 + 3 = ? '
]
answerr = [
    '25',
    '5'
]
q_and_a = list(zip(questionn, answerr))   # ได้ออกมาเเล้วเป็น tuple เเล้วเอาไปซ้อน list อีกที
print(q_and_a)


# args kwargs
print('\nargs kwargs')
# เอาไว้อานวยความสะดวกส่งพารามิเตอร์กี่ตัวก็ได้
# *ชื่ออะไรก็ได้ คือ arguments เเค่ * อันเดียว เเล้วตามด้วยชื่อตัวแปล     # การรับพารามิเตอร์เเบบไม่ตั้งชื่อ มากี่ตัวก็ได้
def average(*scores):
    print(scores)    # มันจะแปลงเป็นเเบบ tuple
    sum_score = sum(scores)
    average_score = sum_score/len(scores)
    return average_score

print(average(60, 65, 70))

# ** kwargs คือ keyword argument เหมือนกันเลย เเค่ตั้งชื่อได้        # การรับพารามิเตอร์เเบบตั้งชื่อมากี่อันก็ได้
def check_passed(**scores):
    math1 = scores.get('math')           # มันจะแปลงเป็นเเบบ dictionary
    physics1 = scores.get('physics')     # คำสั่ง get('ชื่อข้อมูล') ใช้ดึงข้อมูลออกมาจาก Dictionary
    english1 = scores.get('english')                       # ถ้าไม่มีข้อมูล จะได้มาเป็นค่า None (ปลอดภัยกว่าใช้ [])
    if math1 is not None and math1 >= 50:
        print('สอบคณิตผ่าน')
    if physics1 is not None and physics1 >= 50:
        print('สอบฟิสิกส์ผ่าน')
    if english1 is not None and english1 >= 50:
        print('สอบอังกฤษผ่าน')

check_passed(math=80, physics=35, english=70)

print('          ทำอีกเเบบ')
def check(math1, physics1, english1):
    if math1 is not None and math1 >= 50:
        print('สอบคณิตผ่าน')
    if physics1 is not None and physics1 >= 50:
        print('สอบฟิสิกส์ผ่าน')
    if english1 is not None and english1 >= 50:
        print('สอบอังกฤษผ่าน')
check(math1=80, physics1=35, english1=70)
# เเถม
print('เเถม')
A = [1, 2, 3, 4, 5]
print(sum(A))        # สามารถเอามารวมกันได้เลย sum กับ list


# Decorator                                                    สูตรสำเร็จ
print('\nDecorator')   # เหมือนเอารถไปอัพเกรดเเล้วดีขึ้น เเรงขึ้น    # def A(function):
# @ เอาไว้ตกเเต่งฟังชั่นหนึ่งให้มีการทำงานมากขึ้น                      #    def B():
def capsule(function):                                  #       function
    def new_function():                                 #    return B
        print('เกราะเหัว เกราะแขน เกราะอก')
        function()
        print('เกราะขา')

    return new_function

@capsule
def megaman():
    print('Megaman')    # ก็เอา def megaman() ใส่ลงไปใน @capsule เเล้วไปที่ def capsule(function)
                        # เเล้ว function จะมารับค่า @capsule เเล้ว function ก็เข้าไปอยู่ใน new_function
                        # เเล้วมันก็ return new_funtion กลับมาเป็นค่าใหม่ให้
@capsule
def zero():
    print('Zero')

megaman()
zero()

print('คำนวณพื้นที่ เเบบจำกัดทศนิยม')
import math
def pretty_number(function):
    def new_function(*args, **kwargs):
        number = function(*args, **kwargs)
        return '{:.2f}'.format(number)
    return new_function

@pretty_number
def circle_area(radius):
    return math.pi * (radius ** 2)

@pretty_number
def ellipse_area(width, height):
    return math.pi / 4 * width * height

print(circle_area(5))
print(ellipse_area(10, 5))


print('\npipenv')
