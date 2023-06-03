from calc_Operations import Operations
from AdvancedDivisionCalculator import AdvancedDivisionCalculator
from AdvancedDivisionCalculator_2 import RemainderOnly
from calc_input import GetInput
from calc_integer_input import IntegerInput
from calc_loop import UserLoop
ui=GetInput()
no_remainder=AdvancedDivisionCalculator()
basic_calculations=Operations()
advanced_calculations=AdvancedDivisionCalculator()
advanced_calculations_2=RemainderOnly()
input_integer=IntegerInput()
user_loop=UserLoop()

chosen_operation = ui.choose_operations()
operand_one=input_integer.input_number()
operand_two=input_integer.input_number()
basic_calculations.operations_proper(chosen_operation, operand_one, operand_two)
advanced_calculations_2.remainder_only(chosen_operation, operand_one, operand_two)

user_loop.loop()