def calculate(a,o,b):
    """ Return the calculated value of ``a`` ``operator`` ``b`` """
    if o == "+": return a + b
    elif o == '-': return a - b
    elif o == '*': return a * b
    elif o == '/' and a and b: return a / b
    elif o == '~' and a and b: return a % b
    
def isoperator(operator):
    return operator in ['+','-','*','/','~']

def get_decimal_input(text:str):
    """ Runs until user input is an integer """
    var = ''
    while not var.isdecimal():
        var = input(text)
    return int(var)  

def get_aob_input(text:str):
    """ Get Num A , Operator & Num B from User input """
    aob = False
    while not aob:
        var = input(text)
        if len(var) == 3:
            a, o, b = var
            aob = all([a.isdecimal(),isoperator(o),b.isdecimal()])
        else:
            print('Invalid input!')
    
    return int(a),o,int(b)

def main():
    print("Welcome to the Python calculator!\nHow many calculations do you want to do?")

    for i in range(get_decimal_input('Ammount: ')):
        a,o,b = get_aob_input("What do you want to calculate?: ")
        result = calculate(a,o,b)
        print(f"{a} {o} {b} = {result}")

if __name__ == '__main__':
    main()
