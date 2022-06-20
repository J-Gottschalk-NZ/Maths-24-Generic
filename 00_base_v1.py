import random
import re

# adds * sign between numbers and brackets
# replaces x with *
def times_adder(expression):

    # replace 'x' and '×' with *
  expression = expression.replace('x', '*' )
  expression = expression.replace('×', '*')
  
  # RegEx from here...
  # https://stackoverflow.com/questions/53228036/insert-multiplication-sign-between-parenthesis
  return re.sub('(?<=\d|\))(\()', '*(', expression)

# decorates text

# Statement decorator
def statement_generator(statement, decoration, style):
  middle = decoration * 3 + " " + statement + " " + decoration * 3
  top_bottom = decoration * len(middle)

  print()

  # adds decoration to top and bottom
  if style == 3:
    print(top_bottom)
    print(middle)
    print(top_bottom)

  else:
    # adds decoration to line only
    print(middle)

  print()

  return ""

# ***** Main Routine Goes here *****

# Sets from http://mbamp.ucsc.edu/files/7915/4393/8152/Maths_24_-_cards.pdf

sets = [
  [2,2,8,6],
  [2,2,4,5],
  [2,4,4,8],
  [8,8,1,7],
  [4,4,8,5],
  [4,6,8,8],
  [8,8,4,4,],
  [6,5,1,1],
  
  
]

valid_symbols = ["+", "-", "*", "/", "(", ")", " "]
invalid_chars = "no"

# choose a random set of numbers from the list
numbers = random.choice(sets)

# change numbers to string
string_numbers = []
for item in numbers:
  string_numbers.append(str(item))

# add numbers to list
valid_chars = valid_symbols + string_numbers

# Ask user question
statement_generator("Welcome to the 24 Game", "-", 3)
print()

print("You are given the following numbers:")
for item in numbers:
  print(item, end = "\t")

print()
print("Can you use +, -, * and / to get the number 24? ")

ans_ok = False
while not ans_ok or invalid_chars == "yes":

  # list to check that all numbers are used...
  numbers_used = []
  raw_user_ans = input("Type your expression here: ").lower()

  # add multiply signs between brackets if needed
  user_ans = times_adder(raw_user_ans)
  
  for character in user_ans:
    
    if character not in valid_chars:
      statement_generator("Eek, you are using invalid characters", "#", 3)
      invalid_chars = "yes"
      break
    else:
      if character in string_numbers:
        numbers_used.append(character)
  
  if len(numbers_used) != 4:
    print("You need to use each number once, you have used {} numbers".format(len(numbers_used)))

  else:
    ans_ok = True


user_value = eval(user_ans)

if user_value == 24:
  print("well done!  You got it")
else:
  print("sorry that is not correct")
  print("{} = {}".format(raw_user_ans, user_value))
