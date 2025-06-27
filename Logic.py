import math

def convert(nb, b1, b2):
    '''
    function to convert from any base to any other base
    nb is string represent the number in the original base
    b1 is the original base
    b2 is the wanted base
    the working principle is to convert the number to base 10 then convert it to the wanted base
    '''
    check, char = convert_digits_symbols(nb, b1, c=2)
    if not check:
        return f'you used the symbol {char} which is not allowed to use in this base'
    nb = str(nb) # in case we get integer
    nb10 = bn_To_b10(nb, b1) #convert to base 10
    nbnew = b10_To_bn(nb10, b2) #convert to new base

    return [nbnew, check]


def b10_To_bn(nb10, b):
    '''
    function to manage the convertion from base 10 to base n where n is any real number
    nb10 is an integer which represent the number in base 10
    b is an integer which represent the base we wish to convert to
    '''
    #first if the number is 1  or then it will be the sameno metter what base we use
    if nb10 == 1:
        nb = '1'
    elif nb10 == 0:
        nb = '0'
    elif nb10 == b:
        nb = '10'
    elif abs(b) == 1:
        nb = 'it is not possible to use 1 as a base'
    elif b > 0:
        # if the base is posative then we will be using the function b10_To_bn_posative to convert
        nb =  b10_To_bn_posative(nb10, b)
    elif b < 0 :
        # if the base is posative then we will be using the function b10_To_bn_negative to convert
        nb =  b10_To_bn_negative(nb10, b)
    else:
        # if b == 0
        nb =  "you can't use 0 as base"


    if len(nb) > 1:
        # some time ther might be some zeros on the right so we remove it
        for i in range(len(nb)):
            if nb[i] == '0' and nb[i+1] != '.':
                nb = nb[1:]
            else:
                break
        # the same with zeros on the left
        for i in range(len(nb)-1, 0, -1):
            if nb[i] == '0' and nb[i-1] != '.' and '.' in nb:
                nb = nb[:-1]
            else:
                break

    # nb is the final convert
    return nb

def b10_To_bn_posative(nb10, b):
    '''
this function convert from base 10 to base b where b is any posative number
    '''
    nb = ""  # here wi=e will store the number in b base
    rounding = 100

    nb10_ = nb10 < 0
    if nb10_:
        # if the number is negative then just add - sign and convert it like it is posative
        nb10 = -nb10
        nb += '-'

    b_1 = b < 1
    if b_1:
        #if base is between 0 and 1 then we use reciprocal of b and the result will be reversed later
        b = 1 / b

    digits = [] #store the digits
    power = math.floor(round(math.log(nb10, b), 8))  #equation to find how many digits are there in the converted number

    if power < 0:
        # if power is less then 0 then we need to add zeros and . to reach it
        digits.append(0)
        digits.append(-1) # -1 as digit represent dot
        for i in range(abs(power)-1):
            digits.append(0)

    while nb10 > 10 ** -rounding and power > -rounding:
        #as long as the number far from zero or the power is larg
        if power == -1:
            #if we each to power -1 that means we need to add dot '.' (which represented in -1 in the diigts)
            digits.append(-1)


        digit = math.floor(round(nb10 / b ** power % b, 4)) #rounding to prevent erorrs
        #to find the digit we devide what left of the number by b^power

        digits.append(digit)

        nb10 -= digit * (b ** power)
        nb10 = round(nb10, 7)#rouning to prevent errors
        power -= 1

    #we use the function convert_digits_symbols to convert the digits to symbols
    nb += convert_digits_symbols(digits, b)

    if power > -1:
        #if we get out of the while loop (so the numbers are equal) but the power is not -1 yet that means we need to add zeros of what left
        #example if we need to convert 8 to base 2 we will get 1*2^3 so just 1, we need to add additional 3 zeros
        nb += '0'* (power+1)


    if nb[0] == '.':
        nb = '0' + nb

    if b_1:
        #as we said if the base is between 0 and 1 then we use the reciprocal of b and here we will reverse it
        if '.' in nb:
            dot = nb.index('.')-1 # the place of the new dot is 1 place to the right
        else:
            dot = len(nb)-1

        nb = nb.replace('.', '')
        nb = nb[::-1]
        dot = len(nb)-dot # the place of the dot after reverse
        nb = nb[:dot] + '.' + nb[dot:]

    return nb

def b10_To_bn_negative (nb10, b):
    '''
this function convert from base 10 to base b where b is any negative number
    '''

    b_1 = abs(b) < 1
    if b_1:
        # if base is between 0 and -1 then we convert to the reciprocal of the base then we reverse it
        b = 1/b

    goal = nb10 #to store the number as the var nb10 going to change later
    digits = [] #to store the digits
    maxPower = findPower(nb10, b) # is the max power we need to use in this number
    maxPowerIDX = maxPower #this var will work as index to keep tracking of where are we
    maxDigit = math.ceil(abs(b)) - 1 # the maximum digit we are allowed to use in the base

    if maxPower < -1:
        # if the max power is larger then -1 then we need to add dot and 0's to reach it
        digits.append(0) #add zero
        digits.append(-1) #add dot
        for j in range(abs(maxPower)-1): #add zeros depeding of how much we need
            digits.append(0)

    while abs(nb10) > 10**-8 and maxPowerIDX > -50:
        x = nb10 > 0
        y = maxPowerIDX%2 == 0
        power = findPower(nb10, b) # we will find the max power to represnt what left of the number for each time we change it


        if maxPowerIDX == -1:
            digits.append(-1) #if we reach power -1 then we need to add dot

        if maxPowerIDX > power or isBitvalid(goal - nb10, b, maxPowerIDX-1, goal) or ((x and not y) or (y and not x)):
            digit = 0
            #print(maxPowerIDX, power, nb10, x, y)
            #if we are for example in power 3 as index but the max power needed to represent what left is just 1 then keep putting 0's until we reach power 1
            #also if it is still valid to get the number in less power then we don't need this digit
            #third condition is if that we need to add numbers and we got odd power(negative number) or the other way around

        else:
            digit = math.floor(abs(nb10/(b)**maxPowerIDX))
            if digit > maxDigit:
                #beacuse we use negative bases sometime the digit might result larger then what we are allowed to
                #if that happend we will use the digit abs(b) -1 instead
                digit = maxDigit

            nb10 -= digit * (b ** maxPowerIDX) #update the new value
            #to find the digit for the currrent power we use this equation
            if not isBitvalid(goal - nb10, b, power, goal):
                #sometime we needs to round the number up not in floor
                #so the function (isBitValid) will see this times and if it is then just use ceil
                nb10 += digit * (b ** maxPowerIDX) # return the old value
                digit = math.ceil(abs(nb10/(b)**maxPowerIDX))
                nb10 -= digit * (b ** maxPowerIDX) #update the value
            if digit > maxDigit:
                #beacuse we use negative bases sometime the digit might result larger then what we are allowed to
                #if that happend we will use the digit abs(b) -1 instead
                nb10 += digit * (b ** maxPowerIDX)  # return the old value
                digit = maxDigit
                nb10 -= digit * (b ** maxPowerIDX)  # update the value

            if digit == 0:
                #the digit can't be 0 unless it is coming from the condition in line 154
                #otherwise it is just 1
                nb10 += digit * (b ** maxPowerIDX)  # return the old value
                digit = 1
                nb10 -= digit * (b ** maxPowerIDX)  # update the value

            nb10 = round(nb10, 9) #to prevent errors

        digits.append(digit)
        maxPowerIDX -= 1


    if len(digits) < maxPower+1:
        for i in range(maxPower+1 - len(digits)):
            #if we reach the number before using all the powers till 0 then we add 0's
            digits.append(0)

    nb = convert_digits_symbols(digits, -b) #function to convert the digit to symbols

    if nb [0] == '.':
        #if the number is like .44 then just make it 0.44
        nb = '0' + nb

    if b_1:
        #in case of bases that is between 0 and -1 we need to reverse the result

        if '.' in nb:
            dot = nb.index('.')-1
        else:
            dot = len(nb)-1

        nb = nb.replace('.', '')
        nb = nb[::-1]
        dot = len(nb)-dot
        nb = nb[:dot] + '.' + nb[dot:]

    return nb

def findPower (nb10, b):
    '''
    function to find the maxumim power needed to represent some number in base b where b is negative number
    the way this funtion work is
    if we have posative number then add (maxDigit * b^2i) from i=-20 to the max
    and wherever we reacht the sum of the wanted number we return that 2i is the needed power
    for negative numbers it is the same but this time we use 2i+1 to make it odd number(therfore negative)
    '''

    test = 0
    #print(abs(nb10), abs(b), 'dd')
    maxpower = abs(math.ceil(math.log(abs(nb10), abs(b)))) + 1 #the max power we could ever need
    maxdigit = math.ceil(abs(b)) - 1 #the max digit we are allowed to use
    r = range(-20, maxpower) #the range of searc, i choosed -20 as mid number(not too large to make it less accurate and not too samll to make it slower or not representable)

    if nb10 > 0:
        for i in r:
            test += maxdigit * b**(2*i)
            if test >= nb10:
                return 2*i


    if nb10 < 0:
        for i in r:
            test += maxdigit * b**(2*i+1)
            if test <= nb10:
                return 2*i+1

def convert_digits_symbols(digits, b, t=1, c=0):
    '''
    this function convert the digit to symbols and the other way arond
    if t=1 (default) it will convert any given digits to symbols
    if t=-1 it will convert any givin symbols to digits
    i used 402 symbols and put everthing i can think of
    the variable c for count/check
    if c=1 then return all the possible symbols (used in calculator)
    if c=2 then check if the given chars fit into base b
    '''


    # Define the ranges for the symbols
    numbers = ''.join(chr(i) for i in range(48, 58)) #we start with numbers (0-9)
    uppercase_letters = ''.join(chr(i) for i in range(65, 91)) #then the letter(A-Z)
    lowercase_letters = ''.join(chr(i) for i in range(97, 123)) #also (a-z)

    # Latin letters with diacritics
    latin_diacritics = (
        'ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ'
        'àáâãäåçèéêëìíîïñòóôõöùúûüýÿ'
        'ĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚě'
        'ĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķ'
        'ĹĺĻļĽľĿŀŁłŃńŅņŇňŉŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲų'
        'ŴŵŶŷŸŹźŻżŽžſ'
    )

    # Greek uppercase letters
    greek_uppercase = ''.join(chr(i) for i in range(0x0391, 0x03A9 + 1) if i != 0x03A2)
    # Greek lowercase letters
    greek_lowercase = ''.join(chr(i) for i in range(0x03B1, 0x03C9 + 1))

    # Cyrillic uppercase letters (including Russian alphabet)
    cyrillic_uppercase = ''.join(chr(i) for i in range(0x0410, 0x042F + 1))
    # Cyrillic lowercase letters (including Russian alphabet)
    cyrillic_lowercase = ''.join(chr(i) for i in range(0x0430, 0x044F + 1))

    # Special symbols
    special_symbols = "!@#$%&;:()[]{}<>?/~\\|+=*^%√π∫€£¥₹¢§¶©®™±×÷←↑→↓∞∑∏"

    # Combine all parts into one string
    symbols = (
            numbers +
            uppercase_letters +
            lowercase_letters +
            latin_diacritics +
            greek_uppercase +
            greek_lowercase +
            cyrillic_uppercase +
            cyrillic_lowercase +
            special_symbols)

    #converting digits to symbols

    if c != 0: #if c have value other then it's default(0)
        #finding the maxDigit
        if abs(b) > 1:
            maxDigit = math.ceil(abs(b))-1
        else:
            maxDigit = math.ceil(abs(1/b)) - 1

        possibleSymbols = symbols[:maxDigit+1] #the symbols that we are allowed to use in this base

        if c == 1:
            return possibleSymbols

        if c == 2:
            chars = digits
            for c in chars:
                if c not in possibleSymbols and c!= '.' and c!= '-': # if there is any symbols in the nb that is not allowed in this base
                    print(c not in possibleSymbols, possibleSymbols)
                    return [False, c]
            return [True, '']

    if t == 1:
        chars = ''
        if b <= len(symbols):
            for d in digits:
                if d == -1:
                    chars += '.'
                else:
                    chars += symbols[int(d)]
        else:
            print(f"you are using a base that is too large that we don't even have enough symbols to represent")
            print(f"we currently have {len(symbols)} symbols , please provide additional {b - len(symbols)} symbol to continue")

        return chars

    #convert symbols to digits
    elif t == -1:
        chars = digits
        digits = []
        for c in chars:
            if c == '.':
                digits.append(-1)
            else:
                digits.append(symbols.index(c))

        return digits

def isBitvalid(nb10, b, bit, n):
    '''
    in this function we check if it is possible to reach some goal number (n) if we have number(nb10) in base(b) and got (bit) powers left
    nb10 is the number we are at now
    b is the negative base
    bit is the power that we are in now
    n is the number that we are checking to reach it
    '''

    a1 = nb10 #a1 will be the min we can reach
    a2 = nb10 #a2 will be the max we can reach

    for i in range(-15, bit):
        if abs(i)%2 == 0:
            #if the base is even then it is posative so add it a2
            a2 += (math.ceil(abs(b))-1) * b**i
        else:
            #other then that if the base is odd then it is negative so add to a1
            a1 += (math.ceil(abs(b))-1) * b**i

    #rounded to prevent errrors
    a2 = round(a2, 5)
    a1 = round(a1, 5)

    #return if n is in the range of (a1 - a2)
    return n <= a2 and n >= a1


def bn_To_b10(nb, b):
    '''
    function used to convert any number from base b to base 10 where b is any real number
    '''

    nb = str(nb) #if we got integer convert it to str first

    nb_ = '-' in nb
    if nb_:
        #if the number is negative then remove the minus sign and add it later
        nb = nb.replace('-', '')

    nb10 = 0 #here we are storing the number in base 10
    digits = convert_digits_symbols(nb, b, -1) #first we convert the symbols to digits using convert_digits_symbols function

    if -1 in digits :
        #if there is dot(-1) in the digits then the max power is the index -1
        #for example if we have 12.5 the index is 2 and the max power is 1
        dot = digits.index(-1)
        power = dot-1
    else:
        #otherwise then the power is just the length of digits -1
        power = len(digits) - 1


    for digit in digits:
        if digit != -1:
            #other then -1 all the digits will be multiplied by thier power
            nb10 += digit*(b**power)
            power -= 1

    nb10 = round(nb10, 4) #rounding to prevent errorrs

    if nb_:
        #if the number is negative here we add the sign
        nb10 = -nb10

    return nb10


def calculate(expression, base):
    '''
    function to do calculation in diffrent bases
    expression is the equation written in the defined base
    first we defone all the variables and the symbols
    convert all varibles to base 10
    do the math
    convert it again to the original base
    '''

    expression = expression.replace(' ', '') #remove spaces
    list_of_symbols = ['+', '-', '*', '/', '^', '%'] #list of the arithmetic operation that is allowed

    var = '' # temporary store the variable
    symbols = [] #store the arithmetic operation
    vars = [] #store the variables

    for i in range(len(expression)):

        if expression[i] not in list_of_symbols:
            var += expression[i] #if it is not in symbols then it is a variable
        else:
            #if it is in the symbols then we reach the end of varible and we will add it now
            if var == '':
                #in case of variable is empty (such as - sign in the begining) then just add '0' as variable
                vars.append('0')
            else:
                #otherwise add the var we found above
                vars.append(var)
                check, c = convert_digits_symbols(var, base, c=2)
                if not check:
                    return f'you used the symbol {c} which is not allowed to use in this base'


            symbols.append(expression[i]) #also add the current symbols to the symbols list
            var = '' #reset the var to empty to get the next var

    vars.append(var) #for the next var it will not be added to the list in the loop so we add it here

    for i in range(len(vars)):
        vars[i] = str(bn_To_b10(vars[i], base)) #convert all variables to base 10

    newExpression = '' # to store the new expression in base 10

    for i in range(len(vars)):
        newExpression += vars[i] #add the varible

        try:
            newExpression += symbols[i] #if possible (if we didn't reach the end of the equation) add the symbol
        except:
            pass

    res = eval(newExpression) #function eval is built-in function to evaluate string to answer

    return b10_To_bn(res, base) #return it to original base


#Github : murtadha203/InfiniteBaseCalc
