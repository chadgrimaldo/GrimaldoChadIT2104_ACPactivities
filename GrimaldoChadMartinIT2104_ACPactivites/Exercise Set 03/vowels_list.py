string = input("Enter a string: ")
vowels = []
for char in string:
    if char.lower() in 'aeiou':
        vowels.append(char)
print(vowels)