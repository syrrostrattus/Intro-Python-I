x = 10
y = 2.24552
z = "I like turtles!"

f_string= f"x is {x}, y is {y}, and z is '{z}'"

string_form = "x is {num1}, y is {num2}, and z is '{proclamation}'".format(num1 = x, 
                     num2 = y, proclamation = z)

operation = "x is %d, y is %f, and z is '%s'" % (x, y, z)

print(operation)

print(string_form)

print(f_string)
