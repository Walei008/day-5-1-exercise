# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  total_height=(0)
  num_of_students=0
  for student in student_heights:
    num_of_students+=1
    
for height in student_heights:
    total_height+=int(height)
    
  
average=total_height/num_of_students
print(average)
  
round=round(average)  

#Write your code below this row 👇




