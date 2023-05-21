class Operations:
    def choose_operations(self):
        while True:
            operations_list=["A", "S", "M", "D"]
            global chosen_operation
            chosen_operation=input("Please input an operation to use. Type the letters indicated for each operation: A for Addition, M for multiplication, S for subtraction, D for division: ")
            chosen_operation=chosen_operation.upper()
            if chosen_operation in operations_list:
                print('You chose ' + chosen_operation)
                break
            else:
                print("Not a valid operation! Please try again.")

    def input_numbers(self):
        while True:
            global operand_one, operand_two
            try:
                operand_one=float(input("Please input your first number: "))
                break
            except ValueError:
                print("Operand must be a number! Please try again.")
        while True:
            try:
                operand_two=float(input("Please input your second number: "))
                break
            except ValueError:
                print("Operand must be a number! Please try again.")


    def operations_proper(self):
        global operand_one, operand_two
        if chosen_operation=="A":
            sum=operand_one + operand_two
            print("The sum of the operands is " + str(sum))
        if chosen_operation=="S":
            diff=operand_one-operand_two
            print("The difference of two operands is " + str(diff))
        if chosen_operation=="M":
            prod=operand_one*operand_two
            print("The product of the two operands is " + str(prod))
        if chosen_operation=="D":
            while True:
                try:
                    quot=operand_one/operand_two
                    print("The quotient of the two operands is " + str(quot))
                    break
                except ZeroDivisionError:
                        operand_two=float(input("Your second operand cannot be zero! Input another number: "))
    
    def loop(self):
        while True:
            loop_options=['Y','N']
            user_loop=input("Do you want to do another calculation? (Y/N)")
            user_loop=user_loop.upper()
            if user_loop=="Y":
                self.choose_operations()
                self.input_numbers()
                self.operations_proper()
                continue
            elif "N" in user_loop:
                break
            else:
                user_loop=input("Invalid input! Please reinput (Y/N)")