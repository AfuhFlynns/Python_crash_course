# Exercise 1
name = "Afuh Flynn"
print(f"Hello, {name} would you like to learn some python today?")

# Exercise 2
name = "Afuh Flynn"
# Lower case
print(name.lower())
# Upper case
print(name.upper())
# Title case
print(name.title())


# Exercise 3
print('A quote by Afuh Flynn: "Imagination is the DNA of all inventions"')


# Exercise 4
famous_person = "Afuh Flynn"
message = f'A quote by {famous_person}: "Imagination is the DNA of all inventions"'
print(message)

# Exercise 5
person_name = "\tTembeng Mylse\n" # \t creates a tab (horizontal space) and \n creates a new line
print(person_name)

# rstrip
print(person_name.rstrip())
# lstrip
print(person_name.lstrip())
# strip
print(person_name.strip())

# Exercise 6
filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))
print(filename.removesuffix(".txt").replace("_", "-"))
