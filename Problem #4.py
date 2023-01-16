while True:
    STUDNAME = input("Enter student name: ")
    KORSCODE = input("Enter course code: ")
    YERCODE = int(input("Enter year code: "))
    TOTALLEC = int(input("Enter total number of lecture units enrolled: "))
    TOTALLAB = int(input("Enter total number of laboratory units enrolled: "))

    if KORSCODE.upper() == "A":
        KORSNAME = "Engineering"
    elif KORSCODE.upper() == "B":
        KORSNAME = "Business Administration"
    elif KORSCODE.upper() == "C":
        KORSNAME = "Secretarial"
    elif KORSCODE.upper() == "D":
        KORSNAME = "Architecture"
    
    if YERCODE == 1:
        LECRATE = 345.75
        LABRATE = 420.45
    elif YERCODE == 2:
        LECRATE = 320.45
        LABRATE = 400.50
    elif YERCODE == 3:
        LECRATE = 298.75
        LABRATE = 389.75
    elif YERCODE == 4:
        LECRATE = 275.85
        LABRATE = 360.65
    elif YERCODE == 5:
        LECRATE = 275.85
        LABRATE = 360.65

    LECFEE = TOTALLEC * LECRATE
    LABFEE = TOTALLAB * LABRATE
    TUITION = LECFEE + LABFEE
    TOTALUNITS = TOTALLEC + TOTALLAB

    if TOTALUNITS >= 1 and TOTALUNITS <= 8:
        DOWN = 800.00
    elif TOTALUNITS >= 9 and TOTALUNITS <= 14:
        DOWN = 1000.00
    elif TOTALUNITS >= 15 and TOTALUNITS <= 18:
        DOWN = 1500.00
    elif TOTALUNITS >= 19:
        DOWN = 1800.00
    BALANSE = TUITION - DOWN

    print("Student Name: ", STUDNAME)
    print("Course Name: ", KORSNAME)
    print("Tuition Fee: ", TUITION)
    print("Balance: ", BALANSE)

    repeat = input("\nDo you want to repeat the transaction? (yes/no): ")
    if repeat.lower() == "no":
        break
    elif repeat.lower() == "yes":
        continue
