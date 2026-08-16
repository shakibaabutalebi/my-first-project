num_students=""
scores=""
A=[]
num_Student=int (input("enter your number of programming students:"))
for i in range (num_Student):
   scores=float(input(f"enter your scours students{i+1}:"))
   A.append(scores)
average_class= sum (A) / num_Student
max_score=max(A)
num_passed=sum(1 for j in A if j >=10 )
print(A)
print(average_class) 
print(max_score ) 
print(num_passed)


