print("Enter The Marks Obtained In 5 Subjects Respectivly.")
eng = int(input("English:"))
mat = int(input("Maths:"))
sci = int(input("Science:"))
tamil = int(input("Tamil:"))
ict = int(input("ICT:"))

sum = eng+mat+sci+tamil+ict
print("The sum of all the subjects marks",sum)

perc = (sum/500)*100

print(end = "Marks by Percentage =")
print(perc)