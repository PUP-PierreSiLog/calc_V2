from calc_Operations import Operations
from AdvancedDivisionCalculator import AdvancedDivisionCalculator
from calc_input import GetInput
ui=GetInput()
no_remainder=AdvancedDivisionCalculator()
basic_calculations=Operations()
advanced_calculations=AdvancedDivisionCalculator()

chosen_operation = ui.choose_operations()
operand_one=ui.input_number()
operand_two=ui.input_number()
basic_calculations.operations_proper(chosen_operation, operand_one, operand_two)
no_remainder.no_remainder(chosen_operation, operand_one, operand_two)
advanced_calculations.remainder_only(chosen_operation, operand_one, operand_two)
ui.loop()