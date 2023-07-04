# Read text file
print('\nRead Text File')
# สำคัญมากในการเปิดปิดไฟล์
file = open('scores')
print(file.read())
print(file.readline())      # readline() คือ จะอ่านทีละบรรทัด เเละจะข้ามไปบรรทัดใหม่ให้อัตโนมัติ
print(file.readline())      # readline() เเละ read() คือ จะไม่อ่านบรรทัดเดิมซ้ำ
file.close()

# นับคนสอบได้มากกว่า 50 คะเเนน
file = open('scores')
pass_count = 0
for score in file:
    score_int = int(score)   # มันเป็น str ต้องเเปลงให้เป็น int ก่อน
    if score_int >= 50:
        pass_count += 1
print('Student pass = ', str(pass_count))
file.close()

file1 = open('group_scores')
pass_count = 0
for group_scores in file1:
    group_scores_list = group_scores.split(' ')
    for score in group_scores_list:
        score_int = int(score)
        if score_int >= 50:
            pass_count += 1
print('Student pass = ', str(pass_count))
file1.close()


# Write text file
print('\nWrite text file')
# เอาไว้สำหรับเขียนข้อมูลลงไปใน file
file = open('test.txt', 'w')   # ไม่จำเป็นต้องมีชื่อนี้มาก่อน Python จะสร้างให้ ถ้าไม่มีชื่อนี้
                               # 'w' คือ โหมดการอ่าน open('test.txt', 'w') สำหรับการอ่าน
file.write('What is \n')
file.write('Your\n')
file.write('Name')
file.close()

# ลองอ่านไฟล์ เเล้วเขียนลงไปในไฟล์อีกไฟล์
file_read = open('group_scores')
file_write = open('test.txt', 'w')
for group_score in file_read:
    sum_score = 0
    group_scores_list = group_score.split(' ')
    for score in group_scores_list:
        score_int = int(score)
        sum_score += score_int

    average_score = sum_score/len(group_scores_list)
    file_write.write(str(average_score)+'\n')

file_read.close()
file_write.close()
