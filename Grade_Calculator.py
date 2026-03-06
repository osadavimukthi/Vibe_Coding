while True:
    name = input("\nEnter the student's name (or type 'exit' to quit): ")
    
    if name.lower() == 'exit':
        break

    # Collecting marks for 3 subjects
    try:
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))

        # Calculating the average
        average = (mark1 + mark2 + mark3) / 3

        print("-" * 30)
        print(f"Name : {name}")
        print(f"Average: {average:.1f}")

        # Determining Grade
        if average >= 75:
            print("Grade : A")
        elif average >= 60:
            print("Grade : B")
        elif average >= 40:
            print("Grade : C")
        else:
            print("Result: Fail")
        print("-" * 30)

    except ValueError:
        print("Invalid input. Please enter numerical values for marks.")

input("\nPress Enter to exit...")
