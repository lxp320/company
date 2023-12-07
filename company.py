""" 
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# Функция для печати в терминал
def need_print(value: list, text: str = 'Вывод:', printing: int = 0) -> None:
    if printing == 1:
        print()
        print(text)
        for var in value:
            print(f"- {var}")
        print()

# Функция для преобразования исходных данных. Отдел добавлен в словарь пользователя.
def employers_data(departments: list) -> list:
    # Список для хранения имен сотрудников
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        # Проход по сотрудникам в отделе
        for user in department["employers"]:
            # Запись в словарь к каждому сотруднику его отдел
            user['department'] = department['title']
            user_data.append(user)
    return user_data

# 1. Вывести названия всех отделов
def take_departments(departments: list, printing: int = 0) -> list:
    # Список для хранения названий найденных отделов
    departments_list = []
    # Проход по списку со словарями
    for department in departments:
        # Названия отделов записываем в отдельный список
        departments_list.append(department['title'])
    # Управление выводом в терминал
    need_print(departments_list, 'Список отделов:', printing)
    return departments_list
take_departments(departments, 1)

# 2. Вывести имена всех сотрудников компании.
def employers_names(departments: list, printing: int = 0) -> list:
    input_list = employers_data(departments)
    # Составление списка для вывода
    out_list = []
    for user in input_list:
        data = str(f"{user['first_name']} {user['last_name']}")
        out_list.append(data)
    # Управление выводом в терминал
    need_print(out_list, 'Список сотрудников:', printing)
    return out_list
employers_names(departments, 1)

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
def user_list_vs_department(departments: list, printing: int = 0) -> list:
    input_list = employers_data(departments)
    # Составление списка для вывода
    out_list = []
    for user in input_list:
        user_name = str(f"{user['first_name']} {user['last_name']}")
        data = str(f"Сотрудник: {user_name.ljust(20)} Отдел: {user['department']}")
        out_list.append(data)
    # Управление выводом в терминал
    need_print(out_list, 'Список сотрудников с указание отдела:', printing)
    return out_list
user_list_vs_department(departments, 1)

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
def employers_filter(departments: list, salary: int, printing: int = 0, more_less: str = 'more') -> list:
    # Берем подготовленные данные
    input_list = employers_data(departments)
    # Будущий список для вывода
    out_list = []
    # Перебор пользователей
    for user in input_list:
        # Критерии фильтрации
        if more_less == 'more':
            sign = '>'
            if user['salary_rub'] > salary:
                user_name = str(f"{user['first_name']} {user['last_name']}")
                data = str(f"Сотрудник: {user_name.ljust(20)} Отдел: {user['department']}")
                out_list.append(data)
        elif more_less == 'less':
            sign = '<'
            if user['salary_rub'] < salary:
                user_name = str(f"{user['first_name']} {user['last_name']}")
                data = str(f"Сотрудник: {user_name.ljust(20)} Отдел: {user['department']}")
                out_list.append(data)
        else:
            print('Неправильно задан параметр more')
            break
    # Управление выводом в терминал
    need_print(out_list, f'Список сотрудников с зарплатой {sign} {salary} рублей:', printing)
    return out_list
employers_filter(departments, 100000, 1, 'more')

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
def position_filter(departments: list, salary: int, printing: int = 0, more_less: str = 'more') -> list:
    # Берем подготовленные данные
    input_list = employers_data(departments)
    # Будущий список для вывода
    out_list = []
    # Перебор пользователей
    for user in input_list:
        # Критерии фильтрации
        if more_less == 'more':
            sign = '>'
            if user['salary_rub'] > salary:
                position_name = str(user['position'])
                data = str(f"Должность: {position_name.ljust(20)} Отдел: {user['department']}")
                out_list.append(data)
        elif more_less == 'less':
            sign = '<'
            if user['salary_rub'] < salary:
                position_name = str(user['position'])
                data = str(f"Должность: {position_name.ljust(20)} Отдел: {user['department']}")
                out_list.append(data)
        else:
            print('Неправильно задан параметр more')
            break
    # Управление выводом в терминал
    need_print(out_list, f'Список должностей с зарплатой {sign} {salary} рублей:', printing)
    return out_list
position_filter(departments, 80000, 1, 'less')

# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
def departments_expenses(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        money = 0
        # Проход по сотрудникам в отделе
        for user in department["employers"]:
            money += user['salary_rub']     
        user_data.append(f"Отдел {department['title']} расходует {money} рублей в месяц")
    need_print(user_data, 'Отчет по расходам:', printing)
    return user_data
departments_expenses(departments, 1)

# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.

# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.

# 9. Вывести среднюю зарплату по всей компании.

# 10. Вывести названия должностей, которые получают больше 90к без повторений.

# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.

# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.

# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.

# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.