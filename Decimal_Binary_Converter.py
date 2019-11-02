#!/home/derickson/Projects/SpongeBob/Number\ to\ Binary\ Converter.py

def Contain_Characters(input_string):
    current_index = 0
    index_limit = len(input_string)
    characters_contained = False
    while (current_index != index_limit):
        foo = input_string[current_index]
        if(48 <= ord(foo) <= 57):
            current_index += 1
        else:
            characters_contained = True
            current_index = index_limit
    return(True if characters_contained else False)

def Collect_Conversion_Type(conv_type_in):
    Collecting = True
    while (Collecting == True):
        Collecting = False
        if ("1" in(conv_type_in.lower())):
            return("BtD")
        elif ("binary to decimal" in(conv_type_in.lower())):
            return("BtD")
        elif ("2" in(conv_type_in)):
            return("DtB")
        elif ("decimal to binary" in(conv_type_in.lower())):
            return("DtB")
        elif ("no" in(conv_type_in.lower())):
            exit("\nWow, fine then I guess\n")
        else:
            conv_type_in = input("\nA whoopsie occured. Try again.\n\n")
            Collecting = True
    print(end= '\n\n')

def Collect_Number(num_in):
    Collecting = True
    while (Collecting == True):
        if (num_in == "no"):
            exit("\nWow, alrighty then\n")
        elif (Contain_Characters(num_in) == True):
            num_in = input("\nPlease don't enter letters or special characters\nfor your number. Try again:\n\n")
        else:
            return(int(num_in))

def Biggest_Multiple_of_2(num_in):
    multiple = 0
    while(num_in/(2**multiple) >= 1):
        multiple += 1
    return(multiple-1)

def Biggest_Multiple_of_10(num_in):
    multiple = 0
    while(num_in/(10**multiple) >= 1):
        multiple += 1
    return(multiple-1)

def Convert_Dec_to_Bin(Dec_num):
    Running_Binary_Sum = 0
    while(Dec_num != 0):
        Running_Binary_Sum += 10**(Biggest_Multiple_of_2(Dec_num))
        Dec_num -= 2**(Biggest_Multiple_of_2(Dec_num))
    return(Running_Binary_Sum)

def Convert_Bin_to_Dec(Bin_num):
    Running_Decimal_Sum = 0
    while(Bin_num != 0):
        Running_Decimal_Sum += 2**(Biggest_Multiple_of_10(Bin_num))
        Bin_num -= 10**(Biggest_Multiple_of_10(Bin_num))
    return(Running_Decimal_Sum)

print("\n"*100, "This program will take a Binary number and convert it to Decimal,")
print("or take a Decimal number and convert it to Binary", end="\n\n")
print("Please note that only integer values are accepted", end= "\n\n")

Program_Running = True
while(Program_Running == True):
    Convert_type = Collect_Conversion_Type(input("Would you like to convert 1) Binary to Decimal or 2) Decimal to Binary?\n\n"))
    print(end="\n")
    Convert_number = Collect_Number(input("Please enter your number below:\n\n"))
    print(end="\n")
    if(Convert_type == "DtB"):
        print("Your number in binary is: ", Convert_Dec_to_Bin(Convert_number), end='\n\n')
    elif(Convert_type == "BtD"):
        print("Your number in decimal is: ", Convert_Bin_to_Dec(Convert_number), end='\n\n')
    foo = input("Would you like to convert another number? Yes or No?\n\n")
    print(end='\n')
    if("y" in(foo.lower())):
        Program_Running = True
    elif("n" in(foo.lower())):
        Program_Running = False
    else:
        print("There was an error, so the program assumes you are done")
        Program_Running = False

print("Thanks for using my program!", end='\n\n')
