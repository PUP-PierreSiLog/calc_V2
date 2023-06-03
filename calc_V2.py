from calc_Operations import Operations
from calc_input import Input
ui=Input()
Op=Operations()
ui.choose_operations()
Op.input_numbers()
Op.operations_proper()
Op.loop()