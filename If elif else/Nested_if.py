
medical_cause = input("Do you have a medical cause? (Y/N): ").strip().upper()


if medical_cause == 'Y':
    print("You are allowed to take the test")
else:

     atten = int(input("Enter the attendance of the student: "))
     if atten >= 75: 
        print("You are allowed to take the test")
     else: 
        print("Your not allowed")