from Logic import b10_To_bn, bn_To_b10
import winsound


def debug(a1, a2, b1, b2, c, d):
    '''
    function i used to debug
    a1-a2 is the range of the numbers
    b1-b2 is the range of the bases
    c is how many numbers after the dot in the number
    d is how many numbers after the dot in the bace
    '''

    #adjust the ranges to the dot
    if a1 > 0:
        a2 = a2*10**c
    elif a2 < 0:
        a1 = a1*10**c

    if b1 > 0:
        b2 = b2*10**d
    elif b1 < 0:
        b1 * b1*10**d

    nb10_ = range(a1, a2)
    base_ = range(b1, b2)
    eror = 0 #to store the error rate for each time
    times = 0 #to store how many times did check
    maxerror = 0 # to store the max error rate

    for nb10b in nb10_:
        nb10 = nb10b*(10**-c)
        nb10 = round(nb10, 4)
        for base in base_:
            b = round(base*(10**-d), 3)
            if b == 1 or b == -1 or b == 0:
                continue
            times += 1
            #making try catch to get massage if any error happened
            try:
                b10ToBn = b10_To_bn(nb10, b) #convert the number to base b
                bnToB10 = bn_To_b10(b10ToBn, b) #convert the number back to base 10
                error_rate = round(1 - min(bnToB10 / nb10, nb10 / bnToB10), 7)*100 #calculate the error rate
                diff = abs(bnToB10 - nb10) #calculate the diffrence
                maxerror = max(error_rate, maxerror) #calculate the max error
            except:
                print("nb10 :", nb10)
                print("b :", b)
                print("convert to :", b10ToBn)
                print("convert back :", bnToB10)
                print(f"\033[30m\033[41mbig error rate : {error_rate}%\033[0m")
                print('=' * 35)
                eror += 1

            if error_rate >= 10**-3 and diff > nb10*10**-3: #print the info if some error is larger then 0.001 or diffrence is larger 0.001
                print("nb10 :", nb10)
                print("b :", b)
                print("convert to :", b10ToBn)
                print("convert back :", bnToB10)
                print(f"error rate :{error_rate}%")
                print('=' * 35)
                eror += 1


    totalError = round(eror/times, 7)*100 #to calculate how many errors occurred
    print(f"done with error rate of {totalError}% ({eror} out of {times}) and max error is {maxerror}%")

    winsound.Beep(5000, 500) #sometimes it takes a lot to finsih so added this sound to alert me when it is finshed



# here i tried all 16 possible cases that this program could ever work with
#for each case i put down the result below it
'''print("Case 1")
print("integer/posative base, integer/posative number")
print("number from 2 to 10000, base from 2 to 40")
print('='*60)
debug(2, 10000, 2, 40, 0, 0)
#done with error rate of 0.0% (0 out of 37992400) and max error is 0.0%

print("Case 2")
print("integer/posative base, integer/negative number")
print("number from -10000 to -2, base from 2 to 40")
print('='*60)
debug(-10000, -2, 2, 40, 0, 0)
#done with error rate of 0.0% (0 out of 37992400) and max error is 0.0%

print("Case 3")
print("integer/posative base, fraction/posative number")
print("number from 2 to 10000 (2 number after dot), base from 2 to 40")
print('='*60)
debug(2, 1000, 2, 40, 2, 0)
#done with error rate of 0.0% (0 out of 37992400) and max error is 0.0%

print("Case 4")
print("integer/posative base, fraction/negative number")
print("number from -1000 to -2 (2 number after dot), base from 2 to 40")
debug(-100, -2, 2, 40, 2, 0)
print('='*60)
#done with error rate of 0.0% (0 out of 37992400) and max error is 0.0%

print("Case 5")
print("integer/negative base, integer/posative number")
print("number from 2 to 10000, base from -40 to 2")
debug(2, 10000, -40, -2, 0, 0)
print('='*60)
#done with error rate of 0.0% (0 out of 379240) and max error is 0.0%

print("Case 6")
print("integer/negative base, integer/negative number")
print("number from -10000 to -2, base from -40 to 2")
debug(-1000, -2, -40, -2, 0, 0)
print('='*60)
#done with error rate of 0.0% (0 out of 379240) and max error is 0.0%

print("Case 7")
print("integer/negative base, fraction/posative number")
print("number from 2 to 1000, base from -40 to 2")
debug(2, 1000, -40, -2, 1, 0)
print('='*60)
#done with error rate of 0.0% (0 out of 379924) and max error is 0.0%

print("Case 8")
print("integer/negative base, fraction/negative number")
print("number from -1000 to -2 (1 number after dot), base from -40 to 2")
debug(-1000, -2, -40, -2, 2, 0)
print('='*60)
#done with error rate of 0.0% (0 out of 3799924) and max error is 0.0%

print("Case 9")
print("fraction/posative base, integer/posative number")
print("number from 2 to 10000, base from 2 to 40")
debug(2, 10000, 2, 40, 0, 1)
print('='*60)
#done with error rate of 0.0% (0 out of 3969206) and max error is 0.00%

print("Case 10")
print("fraction/posative base, integer/negative number")
print("number from -1000 to -2, base from 2 to 40 (1 number after the dot)")
debug(-1000, -2, 2, 40, 0, 1)
print('='*60)
#done with error rate of 0.00833% (33 out of 396206) and max error is 0.01714%

print("Case 11")
print("fraction/posative base, fraction/posative number")
print("number from 2 to 1000(1 dot after the number), base from 2 to 20 (1 number after the dot)")
debug(2, 500, 2, 20, 1, 1)
print('='*60)
#done with error rate of 0.0002% (2 out of 984606) and max error is 0.21429%

print("Case 12")
print("fraction/posative base, fraction/negative number")
print("number from -500 to -2(1 dot after the number), base from 2 to 20 (1 number after the dot)")
debug(-500, -2, 2, 20, 1, 1)
print('='*60)
#done with error rate of 0.03636% (358 out of 984606) and max error is 0.21429%

print("Case 13")
print("fraction/negative base, integer/posative number")
print("number from 2 to 1000, base from -40 to -0.2 (1 number after the dot)")
debug(2, 100, -400, -2, 0, 1)
print('='*60)
#done with error rate of 0.00771% (3 out of 38906) and max error is 0.28667%

print("Case 14")
print("fraction/negative base, integer/negative number")
print("number from -1000 to -2, base from -40 to -0.2 (1 number after the dot)")
debug(-100, -2, -400, -2, 0, 1)
print('='*60)
#done with error rate of 0.3547% (138 out of 38906) and max error is 0.20707%

print("Case 15")
print("fraction/negative base, fraction/posative number")
print("number from 2 to 1000 (1 number after the dot), base from -40 to -0.2 (1 number after the dot)")
debug(2, 100, -400, -2, 1, 1)
print('='*60)
#done with error rate of 0.00197% (78 out of 3969206) and max error is 2.0%

print("Case 16")
print("fraction/negative base, fraction/negative number")
print("number from 2 to 1000 (1 number after the dot), base from -40 to -0.2 (1 number after the dot)")
debug(-1000, -2, -400, -2, 1, 1)
print('='*60)
'''

#as you see in the cases where i use fracction as base there was some errors up to 2%
#that happened when you use smal bases like 1.1 or 0.9 and large numbers

