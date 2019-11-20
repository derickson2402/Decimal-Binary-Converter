#!/usr/bin/env python3

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
        if (("1" in(conv_type_in.lower())) or ("binary to decimal" in(conv_type_in.lower()))):
            return("Type Bin to Dec")
        elif (("2" in(conv_type_in)) or ("decimal to binary" in(conv_type_in.lower()))):
            return("Type Dec to Bin")
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

def Largest_Multiple(Input, Mult_of):
    iteration = 0
    while(Input/(Mult_of**iteration) >= 1):
        iteration += 1
    return(iteration-1)

def Convert_Number(Conversion_Value, Convert_type):
    Running_Sum = 0
    while(Conversion_Value != 0) and (Convert_type == "Type Dec to Bin"):
        Running_Sum += 10**(Largest_Multiple(Conversion_Value, 2))
        Conversion_Value -= 2**(Largest_Multiple(Conversion_Value, 2))
    while(Conversion_Value != 0) and (Convert_type == "Type Bin to Dec"):
        Running_Sum += 2**(Largest_Multiple(Conversion_Value, 10))
        Conversion_Value -= 10**(Largest_Multiple(Conversion_Value, 10))
    return(str(Running_Sum))

def Make_Output_Readable(Input, Input_type):
    Running_Output = ""
    iteration = 0
    length = int(len(Input))
    if (Input_type == "Type Dec to Bin"):
        while(length-(iteration*4) >= 4):
            Running_Output=Input[length-4-(iteration*4):length-(iteration*4)]+(""if(iteration==0)else" ")+Running_Output
            iteration += 1
        if(length-(iteration*4) > 0):
            Running_Output = "0"*(4-(length-(iteration*4))) + Input[0:length-(iteration*4)]+" "+Running_Output
    elif (Input_type == "Type Bin to Dec"):
        while(length-(iteration*3) >= 3):
            Running_Output=Input[length-3-(iteration*3):length-(iteration*3)]+(""if(iteration==0)else",")+Running_Output
            iteration+=1
        if((length-iteration*4)>0):
            Running_Output = Input[0:length-(iteration*3)]+","+Running_Output
    else:
        exit("There was an error recieving an input type for the Make_Output_Readable function")
    return(Running_Output)

print("\n"*100, "This program will take a Binary number and convert it to Decimal,")
print("or take a Decimal number and convert it to Binary", end="\n\n")
print("Please note that only integer values are accepted", end= "\n\n")

Program_Running = True
while(Program_Running == True):
    Convert_type = Collect_Conversion_Type(input("Would you like to convert 1) Binary to Decimal or 2) Decimal to Binary?\n\n"))
    Value_To_Convert = Collect_Number(input("\nPlease enter your number below:\n\n"))
    print("\nYour new value in ",("Binary" if Convert_type == "Type Bin to Dec" else "Decimal"),"is:",Make_Output_Readable(Convert_Number(Value_To_Convert,Convert_type),Convert_type),end='\n\n')
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
