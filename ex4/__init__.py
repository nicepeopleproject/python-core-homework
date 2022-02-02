def cross_join(employees, departments):
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """
    return cross_join_generator(employees, departments)

def cross_join_generator(employees, departments):
    for employee in employees:
        for department in departments:
            yield (employee, department)

