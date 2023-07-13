# try:
#     # get input net sales
#     print('Enter the net sales for')

#     previous = float(input('- Prior period:'))
#     current = float(input('- Current period:'))

#     # calculate the change in percentage
#     change = (current - previous) * 100 / previous


# # show the result
#     if change > 0:
#         result = f'Sales increase {abs(change)}%'
#     else:
#         result = f'Sales decrease {abs(change)}%'

#     print(result)
# except ValueError:

#     print('Error! Please enter a number for net sales.')

# except ZeroDivisionError:
#     print('Error! The prior net sales cannot be zero.')
#
a=10
b=0
c=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("zerodivision error=",c)    
finally:
    print("final block ones time will be excute")    
  
################################################## 

def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2


def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'


def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print(error)
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')

main()   



#find the name of student.

