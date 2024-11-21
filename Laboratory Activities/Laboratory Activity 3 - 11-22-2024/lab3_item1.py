def roman_to_integer(roman):
    
    roman = roman.upper()
    total = 0
    last_value = 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }


    for char in reversed(roman):
        value = roman_values.get(char)
        
        if value is None:
            print(f"Invalid Roman numeral: {roman}")
            return None  
        
        if value < last_value:
            total -= value
        else:
            total += value
        last_value = value

    return total


def main():
    
    roman = input("Enter a Roman numeral: ")
    integer_value = roman_to_integer(roman)
    
    if integer_value is not None:
        print(f"The integer value of '{roman.upper()}' is: {integer_value}")


if __name__ == "__main__":
    main()
