from calc_Operations import Operations
from calc_input import GetInput
ui=GetInput()
Op=Operations()
chosen_operation = ui.choose_operations()
operand_one=ui.input_number()
operand_two=ui.input_number()
Op.operations_proper(chosen_operation, operand_one, operand_two)
Op.loop()