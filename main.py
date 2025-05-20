
def calculate(a,o,b):
    if o == "+":
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/' and a and b:
        return a / b
    elif o == '~' and a and b:
        return a % b
    else:
        return 'ERROR'
    
def isoperator(operator):
    return operator in ['+','-','*','/','~']

def get_decimal_input(text:str):
    var = ''
    while not var.isdecimal():
        var = input(text)
    return int(var)

def getnumeric(num: str) -> list[bool , type]:
    if not num: # input is empty
        return False, None
    if num.isdecimal(): # Input is an integer
        return True, int
    if num[0] == '-':
        if num[1:].isdecimal():
            return True, int
        else:
            splitted = num[1:].split('.')
            l = len(splitted)
            if l > 0 and l < 3: #check float 0.0 , .0 , 0.
                a, b = splitted
                return a.isdecimal() and b.isdecimal(), float
            else:
                return False, None
    else:
        splitted = num[1:].split('.')
        l = len(splitted)
        if l > 0 and l < 3: #check float 0.0 , .0 , 0.
            #check 
            a, b = splitted
            return a.isdecimal() and b.isdecimal(), float
        else:
            return False, None
                
def get_aob_input(text:str):
    var = ''
    aob = False
    while not aob:
        var = input(text)
        splitted = var.split(' ')
        if len(var.split(' ')) == 3:
            a, o, b = splitted
            # the c var is only for checking
            ca,ta = getnumeric(a) # the t var is for changing the value to int or float
            co = isoperator(o)
            cb,tb = getnumeric(b) # the t var is for changing the value to int or float
            
            aob = all([ca,co,cb])
    
    return ta(a),o,tb(b)
def main():
    print("""
    Welcome to the Python calculator!
    How many calculations do you want to do?
    """)

    for i in range(get_decimal_input('Ammount: ')):
        a,o,b = get_aob_input("What do you want to calculate?: ")
        result = calculate(a,o,b)
        print(f"{a} {o} {b} = {result}")
if __name__ == '__main__':
    main()
