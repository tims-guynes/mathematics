from basic_operations import *

def main_fun():
    val_1 = float(input("Please choose your first value: "))
    
    operator = input("""Please select your operator:
                     +  for addition
                     -  for subtraction
                     *  for multiplication
                     /  for division 
                     ^  for exponent
                     -^ for root
                    : """)
    val_2 = float(input("Please choose your second value: "))
    
    match operator:
        case "+":
            result = addition(val_1, val_2)
        case "-":
            result = subtract(val_1, val_2)
        case "*":
            result = multiply(val_1, val_2)
        case "/":
            result = divide(val_1, val_2)
        case "^":
            result = exponent(val_1, val_2)
        case "-^":
            result = root_num(val_1, val_2)

    print(result)

if __name__ == "__main__":
    main_fun()
    