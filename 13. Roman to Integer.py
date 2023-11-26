# https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150

num1 = 'LVIII'
num2 = 'MCMXCIV'
num3 = 'III'
res = 58

romans = {
    'IV': '4',
    'IX': '9',
    'XL': '40',
    'XC': '90',
    'CD': '400',
    'CM': '900',
    'I': '1',
    'V': '5',
    'X': '10',
    'L': '50',
    'C': '100',
    'D': '500',
    'M': '1000',
}


def romanToInt(s: str) -> int:
    sum = 0
    for i in romans.keys():
        s = s.replace(i, f' {romans.get(i)}')
    s = s.split(' ')
    while '' in s:
        s.remove('')
    for i in s:
        sum = sum + int(i)
    return sum


print(romanToInt(num1))
print(romanToInt(num2))
print(romanToInt(num3))

# clever way
def romanToIntButchered(s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number

print(romanToIntButchered(num2))