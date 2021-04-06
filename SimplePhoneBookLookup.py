while True:    #This simulates a Do Loop
    found = False
    index = 0
    userName = ""
    people = [""] * (7)
    
    people[0] = "Greg"
    people[1] = "Derek"
    people[2] = "John"
    people[3] = "Jacob"
    people[4] = "Frank"
    people[5] = "Mike"
    people[6] = "Stevie"
    phoneNumbers = [""] * (7)
    
    phoneNumbers[0] = "(320)-867-5309"
    phoneNumbers[1] = "(763)-864-2916"
    phoneNumbers[2] = "(952)-345-8584"
    phoneNumbers[3] = "(763)-555-1234"
    phoneNumbers[4] = "(651)-478-6598"
    phoneNumbers[5] = "(218)-654-9821"
    phoneNumbers[6] = "(714)-800-5490"
    print("Enter in a name to search for the phone number associated with it: ")
    userName = input()
    while found == False and index <= 7 - 1:
        if people[index] == userName:
            found = True
            print(people[index] + " " + phoneNumbers[index])
        else:
            index = index + 1
    if found != True:
        print("No name could be found in the directory")
    print("Would you like to search for another person? (Y/N)")
    again = input()
    while again != "Y" and again != "y" and again != "N" and again != "n":
        print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
        again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
