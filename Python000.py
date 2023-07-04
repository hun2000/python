x = 5
print(x)
y = 10
print(x+y)
z = x + y
print(z)

x += 5
print(x)

score = 800
if score < 0:
    print('Error')
elif score >= 80:
    print('A')
else: print('F')

#x = int(input('x = '))
x = 23
score = 0
for i in range(1, x+1):
    if x % i == 0:
        score += 1
if score == 2 :
    print('จำนวนเฉพาะ')
else:print('ไม่ใช่จำนวนเฉพาะ')

x = 20
for i in range(1,x+1):
    if i % 2 == 0:
        continue
    if i == 15:
        break
    print(i)

def rule(x, y, z):
    h = x + y + z
    return h
def ttt(x):
    return x**x

print('อะไรก็ไม่รู้', str(rule(1,1,1)))
print(ttt(3))

import shape as s
print(s.what(4))

#import tkinter as t
# def tt():
#    qq = int(e.get())
#    ttt = ''
#    for i in range(1,13):
#        ttt += str(qq)+'*'+str(i)+'='+str(i*qq)+'\n'
#    ll.configure(text=ttt)
#w = t.Tk()
#w.title('Benz')
#w.minsize(400, 500)
#l = t.Label(text='ABCDEFGH', master=w)
#l.pack()
#e = t.Entry(master=w)
#e.pack()
#b = t.Button(master=w, text='OK', command=tt)
#b.pack()
#ll = t.Label(master=w)
#l.pack()
#w.mainloop()

print('\nList')
w = ['1', '2', '3', '20']
print(w[1])
w[3]='200'
w.append('4')
w.insert(1, '5')
w.remove('3')
print(w)
print(str('จำนวนของ list')+str(len(w)))
for list in w:
    print(list)
for i in range(len(w)):
    print(w[i])

dictionary = {'name': 'Weeraphat', 'last_name':'Yian', 'age':'20'}
dictionary['name']='Benz'
dictionary['w']='Benzzzz'
dictionary.pop('last_name')
print(dictionary)
print(dictionary['name'])


print('\nstring')
message = 'string'
print(message.upper())
print(len(message))
message = '1,2,3,4,5,6,7,8,9'
messages = message.split(',')
print(message.split(','))
print('1' in message)
print('+'.join(messages))


print('\nClass')
class Gun:
    def __init__(self, name1, ammo1):
        self.name = name1
        self.ammo = ammo1
    def add(self,ammo2):
        self.ammo += ammo2
    def fire(self):
        self.ammo -= 5

Gun1 = Gun(name1='Benz', ammo1=20)
print(Gun1.name)
Gun1.add(20)
print(Gun1.ammo)
Gun1.fire()
print(Gun1.ammo)

class Gun():
    def __init__(self, name1, ammo1):
        self.name = name1
        self.ammo = ammo1
    def add(self, ammo2):
        self.ammo += ammo2
    def fire(self, ammo3):
        self.ammo = self.ammo-ammo3

gun1 = Gun(name1='Benz', ammo1=30)
gun1.add(50)
gun1.fire(33)
print(gun1.ammo)


print('\nMath')
import math
print(math.sqrt(25))
print(math.cos(math.pi/180*60))
A = [1,2,3,4,5,6,7,8,9]
B = [11,22,33,44,55,66]
print(max(A))
print(min(B))


print('\nRandom')
import random
A = [1,2,3,4,5,6,7,8,9]
print(random.choice(A))
print(random.randint(1, 100))  # เเบบจำนวนเต็ม
print(random.uniform(1,100))   # มีทศนิยม
random.shuffle(A)              # สลับใน list
print(A)


print('\nDatetime')
import datetime as date
print(date.datetime.now())
A = date.datetime(year=2001, month=1, day=27)
B = date.datetime.now()
C = B-A
print(C)


print('\nTry Except')
#try:
#    x = int(input('X = '))
#    y = int(input('Y = '))
#    if x < 0 or y < 0:
#        raise Exception
#    print(x/y)
#except:
#    print('กรุณากรอกตัวเลขครับ')


print('\nเครื่องคำเลข')
import tkinter as t
def do():
    test =''
    try:
        int1 = int(e.get())
        for i in range(1,13):
            test += str(int1)+'*'+str(i)+'='+str(i*int1)+'\n'
        l.configure(text=test)
    except:
        l.configure(text='อะไรก็ไม่รู้')


w = t.Tk()
w.minsize(300, 400)
w.title('เครื่องคิดเลข')
e = t.Entry(master=w)
e.pack()
b = t.Button(master=w, text='OK', command=do)
b.pack()
l = t.Label(master=w)
l.pack()
w.mainloop()

