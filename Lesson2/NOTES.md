# Python Strings

## Table of content

- [Welcome to my crash course](#python-strings)
- [Table of content](#table-of-content)
- [Strings in  python](#string)
  - [Changing case with methods](#changing-case-with-methods)
  - [The title method](#1-the-title-method-it-capitalizes-every-first-letter-of-words-in-the-string)
  - [The upper method](#2-the-upper-method-it-changes-all-the-letters-to-upper-case)
  - [The lower method](#3-the-lower-method-it-changes-all-the-letters-to-lower-case)
  - [Inserting varibales into strings](#inserting-variables-into-strings)

## String

```python
name = "Afuh Flynn"
```

### Or

```python
name = 'Afuh Flynn'
```

## This flexibility in strings allows us to do

```python
name = "My name's Afuh Flynn" # Insert single qoute into double qoutes
print(name) # My name's Afuh Flynn
name = 'My quote: "My name is Afuh Flynn"' # Insert double qoutes into single qoutes
print(name) # My qoute: "My name is Afuh Flynn"
```

## Changing case with methods

### 1. The title() method. It capitalizes every first letter of words in the string

```python
name = "john dalton"
# A title has every first letter of every word capitalized
print(name.title()) # John Dalton
```

### 2. The upper() method. It changes all the letters to upper case

```python
print(name.upper()) # JOHN DALTON
```

### 3. The lower() method. It changes all the letters to lower case

```python
name = "TEMBENG MYLSE"
print(name.lower()) # tembeng mylse
```

## Inserting variables into strings

### 1. Using the formatted strings (f-strings) package

Here, we use the f-strings package inbuilt into python: (e.g f"Your string" or f'Your string')

```python
firstname = "Tembeng"
lastname = "Mylse"

fullname = f"{firstname} {lastname}"
print(fullname) # Tembeng Mylse
```

We can also use f-strings to compose a sentence an then assign it to a variable

```python
firstname = "Tembeng"
lastname = "Mylse"

fullname = f"{firstname} {lastname}"
message = f"Hello, {fullname}!"
print(message) # Hello, Tembeng Mylse!
```

## Stripping Whitespaces

### 1. Using the rstrip() method

This method removes the whitespaces on the right

```python
name = "Afuh Flynn "
print(name.rstrip()) # Afuh Flynn
```

### 2. Using the lstrip() method

This method removes the whitespaces on the left

```python
name = "Afuh Flynn "
print(name.lstrip()) # Afuh Flynn
```

### 3. Using the strip() method

This method removes the whitespaces on the left and right

```python
name = "Afuh Flynn "
print(name.strip()) # Afuh Flynn
```
