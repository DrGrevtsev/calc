#take two number from the user
#dict = {"key" : "values"}
"""
history = {
    "addition" : [],
    "substarcion" : [],
    "multiply" : [],
    "division" : []
}
try:
    while(True):
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
        except ValueError:
            print("numbers only!!!!")
            continue
        #ask the user what is the mathematical operator (+-*/)
        operator = input("opertor (+,-,*,/): ")
        #print the user a nice answer
        if operator == "+":
            print(f"{num1} + {num2} = {num1+num2}")
            history["addition"].append(f"{num1} + {num2} = {num1+num2}")
        elif operator == "-":
            print(f"{num1} - {num2} = {num1-num2}")
            history["substarcion"].append(f"{num1} - {num2} = {num1-num2}")
        elif operator == "/":
            try:
                print(f"{num1} / {num2} = {num1/num2}")
                history["division"].append(f"{num1} / {num2} = {num1/num2}")
            except ZeroDivisionError:
                print("kjdfjk;daf 0 lo tov")
        elif operator == "*":
            print(f"{num1} * {num2} = {num1*num2}")
            history["multiply"].append(f"{num1} * {num2} = {num1*num2}")
        else:
            print("error lo baroor behlalll")

        asd = input("exit? (y/n) history(h) ")
        if asd == "y":
            print("bye..")
            break
        elif asd == "n":
            print("again..")
        elif asd == "h":
            for key, value_list in history.items():
                print(f"{key}:")
                for index, value in enumerate(value_list):
                    print(f"\t{index+1}). {value}")
        else:
            print("bsdflkjbsadkjfbl ....")
except KeyboardInterrupt:
    print("\nbye...")
"""


def take_user_input() -> list:
    try:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
    except ValueError:
        print("numbers only!!!!")
    operator = input("opertor (+,-,*,/): ")
    return [num1, num2, operator]


def calculate_numbers(user_data_list: list) -> tuple:
    try:
        result = eval(f"{str(user_data_list[0])} {user_data_list[-1]} {str(user_data_list[1])}")
        print(f"{str(user_data_list[0])} {user_data_list[-1]} {str(user_data_list[1])} = {result}")
        math_problem = f"{str(user_data_list[0])} {user_data_list[-1]} {str(user_data_list[1])} = {result}"
        return user_data_list[-1] , math_problem
    except ZeroDivisionError as e :
        return e
    except SyntaxError as e:
        return e
        

def update_history_dict(operator: str, math_problem:str):
    if operator == "+":
        history["addition"].append(math_problem)
    elif operator == "-":
        history["substarcion"].append(math_problem)
    elif operator == "*":
        history["multiply"].append(math_problem)
    else:
        history["division"].append(math_problem)


def loop_control() -> bool:
    answer = input("exit? (y/n) ")
    if answer == "y":
        print("bye..")
        return True
    elif answer == "n":
        print("again..")
        return False
    else:
        print("bsdflkjbsadkjfbl ....")
        return False


def main():
    global history
    history = {
    "addition" : [],
    "substarcion" : [],
    "multiply" : [],
    "division" : []
    }
    while True:
        user_data_list = take_user_input()
        try:
            operator, math_problem = calculate_numbers(user_data_list)
        except TypeError:
            print("kjdfjk;daf 0 lo tov")
            continue
        update_history_dict(operator, math_problem)
        if loop_control():
            break
        answer = input("history? (h) ")
        if answer == "h":
            for key, value_list in history.items():
                print(f"{key}:")
                for index, value in enumerate(value_list):
                    print(f"\t{index+1}). {value}")
        
try:    
    main()
except KeyboardInterrupt:
    print("\nBye...")










"""
history:
    additon:
        1. 1+2=3
        2. ..
        3. ..
    substraction:
        1. 2-1=1
        2...
        3....
"""