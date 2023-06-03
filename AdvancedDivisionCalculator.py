from calc_Operations import Operations
class AdvancedDivisionCalculator(Operations):
    def no_remainder(self, chosen_operation, operand_one, operand_two): 
        if chosen_operation=="D":
            no_remainder_result=operand_one//operand_two
            print("Quotient with no remainder is " +str(no_remainder_result))
        else:
            pass