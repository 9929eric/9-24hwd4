user_entry = input('What calculation would you like to do? (add, sub, mult, div)')
number1 = int(input( 'What is the first number?'))
number2 = int(input( 'What is the second number?'))
if user_entry == "add":
  print("Your result is ",(number1+number2),". Calc U later!", sep ='')
elif user_entry == "sub":
  print("Your result is ",(number1-number2),". Calc U later!", sep ='')
elif user_entry == "mult":
  print("Your result is ",(number1*number2),". Calc U later!", sep ='')
elif user_entry == "div":
  print("Your result is ",(number1/number2),". Calc U later!", sep ='')
