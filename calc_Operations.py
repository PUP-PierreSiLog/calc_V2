from calc_input import GetInput
class Operations:
    def input_number(self):
        integer=float(input("Kindly input a number:"))
        return integer

    def operations_proper(self, chosen_operation, operand_one, operand_two):
        if chosen_operation == "A":
            sum_result = operand_one + operand_two
            print("The sum of two operands is " + str(sum_result))
        elif chosen_operation == "S":
            diff_result = operand_one - operand_two
            print("The difference of two operands is " + str(diff_result))
        elif chosen_operation == "M":
            prod_result = operand_one * operand_two
            print("The product of the two operands is " + str(prod_result))
        elif chosen_operation == "D":
            while True:
                try:
                    quot_result = operand_one / operand_two
                    print("The quotient of the two operands is " + str(quot_result))
                    break
                except ZeroDivisionError:
                    operand_two = float(input("Your second operand cannot be zero! Input another number: "))

            # If division, asks the user if they want to see the whole number only or the remainder only
            division_choices_list = ["M", "NR"]
            while True:
                division_choices = input(
                    "To know the remainder of your equation, type M. If you want to know the result without any remainder, type NR.")
                division_choices = division_choices.upper()
                if division_choices in division_choices_list:
                    break
                else:
                    print("Invalid answer! Please try again.")

            if "M" in division_choices:
                result = operand_one % operand_two
                print(result)
            if "NR" in division_choices:
                result = operand_one // operand_two
                print(result)

    
    def loop(self):
        while True:
            get_input=GetInput()
            user_loop = input("Do you want to do another calculation? (Y/N)")
            user_loop = user_loop.upper()
            if user_loop == "Y":
                chosen_operation=get_input.choose_operations()
                operand_one=self.input_number()
                operand_two=self.input_number()
                self.operations_proper(chosen_operation, operand_one, operand_two)
                continue
            elif user_loop == "N":
                break
            else:
                print("Invalid input! Please reinput (Y/N)")

