def roman_to_decimal(x):
    ROMAN_NUMBERS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    for i,char in enumerate(x):
        number = ROMAN_NUMBERS[char]
        if x.endswith(char) or number >= ROMAN_NUMBERS[x[i+1]]:
            total += number
        else:
            total -= number
    return total

def decimal_to_roman(num):
    ROMAN_NUMBERS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    out = ''
    ordered_roman = ['M','D','C','L','X','V','I']
    for i,digit in enumerate(ordered_roman):
        equal_numbers = num//ROMAN_NUMBERS[digit]
        if equal_numbers <= 3:
                out += digit*(equal_numbers)
                num = num%ROMAN_NUMBERS[digit]
        else:
            out += digit + ordered_roman[i-1]
            num = num%ROMAN_NUMBERS[digit]
    return out
