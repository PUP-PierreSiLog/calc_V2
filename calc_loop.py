class UserLoop:
    def loop(self):
        while True:
            from calc_Operations import Operations
            from AdvancedDivisionCalculator import AdvancedDivisionCalculator
            from AdvancedDivisionCalculator_2 import RemainderOnly
            from calc_integer_input import IntegerInput
            from calc_input import GetInput
            int_input=IntegerInput()
            op=Operations()
            advanced=AdvancedDivisionCalculator()
            advanced_two=RemainderOnly()
            operation=GetInput()
            user_loop = input("Do you want to do another calculation? (Y/N)")
            user_loop = user_loop.upper()
            if user_loop == "Y":
                chosen_operation=operation.choose_operations()
                operand_one=int_input.input_number()
                operand_two=int_input.input_number()
                op.operations_proper(chosen_operation, operand_one, operand_two)
                advanced.no_remainder(chosen_operation, operand_one, operand_two)
                advanced_two.remainder_only(chosen_operation, operand_one, operand_two)
                continue
            elif user_loop == "N":
                break
            else:
                print("Invalid input! Please reinput (Y/N)")