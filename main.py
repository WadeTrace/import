from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

datetime_ = datetime.datetime.now()
print(datetime_)


if __name__ == '__main__':
    calculate_salary()
    get_employees()