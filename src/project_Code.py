########################################## First Stage Start ##################################################

#First Stage: We take two boolean input value from user for using on logic gates

#We should say what he/she should do to user
print("Input 1 or 0 for logic gates")

#Use infinite while loop until user enter the right inputs
while True:
    #Taking user inputs as integer
    first_input = int(input("First input: "))
    second_input = int(input("Second input: "))
    
    #Break while loop if user enter the right inputs
    if ((first_input == 1 or first_input == 0) and (second_input == 1 or second_input == 0)):
        break
    
    #Print some warning message for wrong inputs
    else:
        print("You have to enter 1 or 0!")

#Logic gates information
print("1-AND Gate 2-OR Gate 3-XOR Gate 4-NAND Gate 5-NOT Gate")

#Taking input from user for what gate he/she want to work on
gate_information = int(input("What gate you want to work on: "))

#We use 4 nearly same print section. So we use simple function
def result(input_result):
    print(f"Result on selected gate: {input_result}")


#We should have third variable for result. That we call 'input_result'

#We make match-case using gate_information


match gate_information:
    case 1:
        input_result = first_input and second_input
        result(input_result)
    case 2:
        input_result = first_input or second_input
        result(input_result)
    case 3:
        input_result = int(first_input != second_input) #This section return True or False. We should turn to integer
        result(input_result)
    case 4:
        input_result = int(not (first_input and second_input)) #This section return True or False. We should turn to integer
        result(input_result)
    case 5: 
        input_result = int(not(first_input)) #This section return True or False. We should turn to integer
        print(f"Your first input {first_input} will be {input_result} on NOT gate.") 
        
        input_result2 = int(not(second_input)) #This section return True or False. We should turn to integer
        print(f"Your second input  {second_input} will be {input_result2} on NOT gate")
    case _:
        print("Undesired Choice!")

########################################## First Stage Finish ##################################################

########################################## Second Stage Start #############################################


