def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

def validate(numR):
    # reverse the credit card number
    num = str(numR)
    
    num = num[::-1]
    # convert to integer list
    num = [int(x) for x in num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0

for i in range(0, 999999):
    num = (543210000000 + i) * 10000 + 1234

    if(num % 123457 == 0):
        print(str(validate(num))+ " " + str(num))
