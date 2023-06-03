import pyfiglet
class GetInput:
    def choose_operations(self):
        while True:
            operations_list=["A", "S", "M", "D"]
            print(pyfiglet.figlet_format("The calculator!", font="isometric2", justify="center"))
            chosen_operation=input("Please input an operation to use. Type the letters indicated for each operation: A for Addition, M for multiplication, S for subtraction, D for division: ")
            chosen_operation=chosen_operation.upper()
            if chosen_operation in operations_list:
                print('You chose ' + chosen_operation)
                return chosen_operation
            else:
                print("Not a valid operation! Please try again.")
    def input_number(self):
        integer=float(input("Kindly input a number:"))
        return integer
    
    def loop(self):
        while True:
            from calc_Operations import Operations
            from AdvancedDivisionCalculator import AdvancedDivisionCalculator
            from AdvancedDivisionCalculator_2 import RemainderOnly
            op=Operations()
            advanced=AdvancedDivisionCalculator()
            advanced_two=RemainderOnly()
            user_loop = input("Do you want to do another calculation? (Y/N)")
            user_loop = user_loop.upper()
            if user_loop == "Y":
                chosen_operation=self.choose_operations()
                operand_one=self.input_number()
                operand_two=self.input_number()
                op.operations_proper(chosen_operation, operand_one, operand_two)
                advanced.no_remainder(chosen_operation, operand_one, operand_two)
                advanced_two.remainder_only(chosen_operation, operand_one, operand_two)
                continue
            elif user_loop == "N":
                break
            else:
                print("Invalid input! Please reinput (Y/N)")