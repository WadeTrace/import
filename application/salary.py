def calculate_salary():
    hours_worked = 50
    wage = 1000
    time = 40 * wage + (hours_worked - 40) * wage
    overtime = hours_worked * wage
    if hours_worked > 40:
        print(f'Ваша запралата: {time} тысяч рублей')
    else:
        print(f'Ваша запралата: {overtime} тысяч рублей')

if __name__ == '__main__':
    calculate_salary()

