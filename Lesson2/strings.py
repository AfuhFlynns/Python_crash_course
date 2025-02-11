# Strings in python


# Author: Afuh Flyine Tembeng
# This is a collection or my work on explaining the concept of strings. (Each work here has it's own NOTES.md file)
## Contact:
# email: flyinnsafuh@gmail.com
# Github: https://github.com/AfuhFlynns
# Tel: +237675171796


# String
name = "Afuh Flynn" 
# Or
name = 'Afuh Flynn'

# This flexibility in strings allows us to do:
name = "My name's Afuh Flynn"
name = 'My quote: "My name is Afuh Flynn"'

print(name)

## Changing case with methods
# 1. The title() method. It capitalizes every first letter of words in the string
name = "john dalton"
print(name.title()) # A title has every first letter of every word capitalized

# 2. The upper() method. It changes all the letters to upper case
print(name.upper())

# 3. The lower() method. It changes all the letters to lower case
name = "TEMBENG MYLSE"
print(name.lower())

## Inserting variables into strings
## 1. Using the formatted strings (f-string) package
firstname = "Tembeng"
lastname = "Mylse"

fullname = f"{firstname} {lastname}"
print(fullname) # Tembeng Mylse

# Or
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
full_name.strip()
