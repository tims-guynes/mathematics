def pythagorean():
    value_message = """What sides do you have to calculate?
                1: sides a and b
                2: sides a and c
                3: sides b and c
                : """
    side_value = input(value_message)
    side_a = "Please enter the value of side 'a': "
    side_b = "Please enter the value of side 'b': "
    side_c = "Please enter the value of side 'c': "
    

    match side_value:
        case "1": #side a and b
            a = float(input(side_a))
            b = float(input(side_b))
            calc = (a**2 + b**2)**0.5
            print(calc)
            repeat()
            
        case "2": #side a and c
            a = float(input(side_a))
            c = float(input(side_c))
            calc = (c**2 - a**2)**0.5
            return calc
    
        case "3": #side b and c
            b = float(input(side_b))
            c = float(input(side_c))
            calc = (c**2 - b**2)**0.5
            return calc
        case _:
            print("Please select a valid response.")
            side_value = input(value_message)
            


def repeat():
    message = """Want to calculate another right triangle? 
                Yes (y) or No (n)?
                : """
    repeat_input = input(message).lower

    match repeat_input:
        case "y" | "yes":
            print("Excellent")
            pythagorean()
        case "n" | "no":
            print("Thank you for using my calculator, goodbye")
            return
        case _:
            print("Please select a valid response (eg: y or yes, n or now) ")
            repeat()
            pass

        
    print()
pythagorean()