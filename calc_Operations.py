from calc_input import Input
class Operations:
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
        input=Input()
        chosen_operation=input.choose_operations
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
            #If division, asks the user if they want to see the whole number only or the remainder only
            division_choices_list=["M", "NR"]
            while True:
                division_choices=input("To know the remainder of your equation, type M. If you want to know the result without any remainder, type NR.")
                division_choices=division_choices.upper()
                if division_choices in division_choices_list:
                    break
                else:
                    print("Invalid answer! Please try again.")
            if "M" in division_choices:
                result=operand_one%operand_two
                print(result)
            if "NR" in division_choices:
                result=operand_one//operand_two
                print(result)
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
                print("Invalid input! Please reinput (Y/N)")