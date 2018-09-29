import re
student_id = input("Enter Student Id:")
if(re.search(r"[a-z|A-Z]",student_id)):
    print("Invalid Student ID")
else:
    student_name = input("Enter Student Name:")
    if(re.search(r"[0-9]",student_name)):
        print("Invalid Name Entered")
    else:
        fees_amount = input("Enter Fees Amount:")
        dots = re.findall(r"\.",fees_amount)
        if(len(dots) > 1):
            print("Invalid Fees Amount")
        else:
            if(len(dots) == 1 and re.search(r"\.[0-9]{3}",fees_amount)):
                print("Invalid Fees Amount")
            else:
                email_id = student_name+"@"+"ABC.com"
                print("Studnet ID:",student_id)
                print("Student Name:",student_name)
                print("Fees Amount:",fees_amount)
                print("Email ID:",email_id)


# OUTPUT
# Enter Student Id:j232
# Invalid Student ID

# Enter Student Id:172
# Enter Student Name:H987s
# Invalid Name Entered

# Enter Student Id:172
# Enter Student Name:Harshal
# Enter Fees Amount:987.25.01
# Invalid Fees Amount

# Enter Student Id:172
# Enter Student Name:harshal
# Enter Fees Amount:983.256
# Invalid Fees Amount

# Enter Student Id:177
# Enter Student Name:harshal
# Enter Fees Amount:98723.21
# Studnet ID: 177
# Student Name: harshal
# Fees Amount: 98723.21
# Email ID: harshal@ABC.com