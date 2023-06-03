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