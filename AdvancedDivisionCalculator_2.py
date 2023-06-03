from calc_Operations import Operations
class RemainderOnly(Operations):
    def remainder_only(self, chosen_operation, operand_one, operand_two):
        if chosen_operation=="D":
            remainder_only_result=operand_one%operand_two
            print("The remainder is " + str(remainder_only_result))
        else:
            pass