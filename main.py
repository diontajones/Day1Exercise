name = input('Welcome to class! What is your name?: ')
print(name)

money = input('I will give you five dollars. How much do you have now and I will tell you the total?: ')
final = int(money) + 5
print(final)

flt_1 = input("Let's add .5 to a random number! Your number?: ")
flt_2 = float(flt_1) + 0.5
print(flt_2)

flt_1 = input('Give me a float: ')
flt_2 = input('Give me a second float: ')
final_flt = float(flt_1) + float(flt_2)
print(final_flt)

flt_3 = input('Give me a float: ')
flt_4 = input('Give me a second float: ')
final_flt2 = float(flt_3) * float(flt_4)
print('{:.2f}'.format(final_flt2))

num_one = input('Give me a random number: ')
num_two = input('Give me a second random number: ')
final_num = int(num_one) / int(num_two)
print(int(final_num))
print(final_num)

fact_1 = input('Are we done class right now? Enter True or False ')
print('You entered: ' + fact_1)
print(bool(False))
