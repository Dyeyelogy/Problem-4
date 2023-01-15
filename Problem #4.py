while True:
    student_name = input("\nEnter Student Name: ")
    course_code = input("Enter Course Code (A = Engineering, B = Business Administration, C = Secretarial, D = Architecture): ")
    year_code = int(input("Enter Year Code: "))
    total_lecture_units = int(input("Enter Total Numbers of Lectured Units Enrolled: "))
    total_lab_units = int(input("Enter Total Numbers of Laboratory Units Enrolled: "))

    total_units = total_lecture_units + total_lab_units

    if course_code.upper() == "A":
        course_name = "Engineering"
    elif course_code.upper() == "B":
        course_name = "Business Administration"
    elif course_code.upper() == "C":
        course_name = "Secretarial"
    elif course_code.upper() == "D":
        course_name = "Architecture"

    if year_code == 1:
        lecture_rate = 345.75
        lab_rate = 420.45
    elif year_code == 2:
        lecture_rate = 320.45
        lab_rate = 400.50
    elif year_code == 3:
        lecture_rate = 298.75
        lab_rate = 389.75
    elif year_code == 4:
        lecture_rate = 275.85
        lab_rate = 360.65
    elif year_code == 5:
        lecture_rate = 275.85
        lab_rate = 360.65

    lecture_fee = total_lecture_units * lecture_rate
    lab_fee = total_lab_units * lab_rate
    tuition_fee = lecture_fee + lab_fee

    if 1 <= total_units <= 8:
        down_payment = 800.00
    elif 9 <= total_units <= 14:
        down_payment = 1000.00
    elif 15 <= total_units <= 18:
        down_payment = 1500.00
    elif total_units >= 19:
        down_payment = 1800.00

    balance = tuition_fee - down_payment

    print("\nStudent Name: ", student_name)
    print("Course Name: ", course_name)
    print("Tuition Fee: ", tuition_fee)
    print("Balance: ", balance)

    repeat = input("\nDo you want to repeat the transaction? (yes/no): ")
    if repeat.lower() == "no":
        break
    elif repeat.lower() == "yes":
        continue
