# string is a collection of IMMUTABLE characters
# string is a data type
# string is a sequence of characters
# we can perform various operations on string
# such as concatenation, indexing, slicing,
# repetition, membership,arithmetic operations.
# concatenation,len(str),str[0],str[-1],str[0:3],
# str[0:],str[:3],str[:]
# string is an immutable data type


str1 = "hello captain"
str2 = 'hello world'
str3 = """hello captain2"""
print(str)
print(type(str1))
print(len(str1))
# indexing
print(str1[3])  # for 3rd index
print(str2[-1])  # for last index

# slicing
print(str1[0:3])  # for 0th index to 3rd index
print(str1[0:])  # for 0th index to last index
print(str1[:3])  # for 0th index to 3rd index
print(str1[:])  # for 0th index to last index

# escape sequence
# \n, \t, \r, \b, \f, \a, \v


str4 = 'hello captain\nhow are you'  # for new line
print(str4)
str5 = 'hello captain\thow are you'  # for tab
print(str5)
str6 = 'hello captain\rhow are you'  # for carriage return
print(str6)
str7 = 'hello captain\bhow are you'  # for backspace
print(str7)
str8 = 'hello captain\fhow are you'  # for form feed
print(str8)
str9 = 'hello captain\ahow are you'  # for alert
print(str9)
str10 = 'hello captain\vhow are you'  # for vertical tab
print(str10)

# string functions

# string functions
print(str1.upper())  # converts string to upper case
print(str1.lower())  # converts string to lower case
print(str1.strip())  # removes leading and trailing whitespaces
print(str1.lstrip())  # removes leading whitespaces
print(str1.rstrip())  # removes trailing whitespaces
print(str1.split())  # splits string using whitespace as separator
print(str1.split('c'))  # splits string using 'c' as separator
print('-'.join(str1))  # joins elements of a list using '-' as separator
str1.endswith('captain')  # checks if string ends with 'captain'
str1.startswith('hello')  # checks if string starts with 'hello'
str1.isalpha()  # checks if string contains only alphabets
str1.isalnum()  # checks if string contains only alphabets and numbers
str1.isdigit()  # checks if string contains only digits
str1.islower()  # checks if string contains only lower case alphabets
str1.isupper()  # checks if string contains only upper case alphabets
str1.isspace()  # checks if string contains only whitespaces
str1.istitle()  # checks if string contains only words starting with upper case
str1.capitalize()  # converts first character of string to upper case
str12 = str1.replace('hello', 'hi')  # replaces old string with new string
print(str12)
print(str1.find('c'))  # returns index of first occurrence of 'c' in string

print(str1[-1:3:-1])