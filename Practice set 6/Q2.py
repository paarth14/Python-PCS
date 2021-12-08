# Write a Python Program to to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume there are 3 subjects and take input from user.

sub1 = int(input("Enter the marks of Maths: "))
sub2 = int(input("Enter the marks of English: "))
sub3 = int(input("Enter the marks of Science: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed because you scored less than 33% marks in the particular subject.")
elif(((sub1+sub2+sub3)/3)<40):
    print("Your are failed because your scored less than 40% as total percentage.")
else:
    print("Congratulations, You are Pass !!")
