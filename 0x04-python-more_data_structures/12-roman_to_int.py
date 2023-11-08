#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_roman = 0
    for rom in range(len(roman_string)):
        if rom > 0 and roma[roman_string[rom]] > roma[roman_string[rom - 1]]:
            new_roman += roma[roman_string[rom]] - 2 * \
                        roma[roman_string[rom - 1]]
        else:
            new_roman += roma[roman_string[rom]]
    return new_roman
