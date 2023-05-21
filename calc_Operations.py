class Operations:
    def choose_operations(self):
        while True:
            operations_list=["A", "S", "M", "D"]
            global user_operation
            user_operation=input("Please input an operation to use. Type the letters indicated for each operation: A for Addition, M for multiplication, S for subtraction, D for division: ")
            user_operation=user_operation.upper()
            if user_operation in operations_list:
                print('You chose ' + user_operation)
                break
            else:
                print("Not a valid operation! Please try again.")

    def input_numbers(self):
        while True:
            global operand_one
            try:
                operand_one=float(input("Please input your first number: "))
                break
            except ValueError:
                print("Operand must be a number! Please try again.")
        while True:
            global operand_two
            try:
                operand_two=float(input("Please input your second number: "))
                break
            except ValueError:
                print("Operand must be a number! Please try again.")

    def operations_proper(self):
        chosen_operation=user_operation
        if chosen_operation=="A":
            sum=operand_one+operand_two
            print("The sum of the operands is " + str(sum))
        if chosen_operation=="S":
            diff=operand_one-operand_two
            print("The difference of two operands is " + str(diff))
        if chosen_operation=="M":
            prod=operand_one*operand_two
            print("The product of the two operands is " + str(prod))
        if chosen_operation=="D":
            try:
                quot=operand_one/operand_two
            except ZeroDivisionError:
                while True:
                    operand_two=float(input("Your second operand cannot be zero! Input another number"))
                    break
