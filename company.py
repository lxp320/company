"""

Внизу есть функция для запуска проверки
Тестов нет)

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

from typing import Any

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
# Функция для составления списка налогов
def tax_names(tax_list: list = taxes) -> list:
    tax_name_list = []
    for tax in tax_list:
        tax_name_list.append(tax["name"])
    return tax_name_list

# Функция для печати в терминал
def need_print(value: Any, text: str = 'Вывод:', printing: int = 0) -> None:
    if printing == 1:
        print()
        print(text)
        if type(value) is int:
            print(value)
        else:
            for var in value:
                print(f"- {var}")
        print()

# Функция для преобразования исходных данных. Отдел добавлен в словарь пользователя.
def employers_data(departments: list, tax_list: list = taxes) -> list:
    # Список для хранения имен сотрудников
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        # Проход по сотрудникам в отделе
        for user in department["employers"]:
            # Запись в словарь к каждому сотруднику его отдел
            user['department'] = department['title'].lower()
            # Запись в словарь каждого сотрудника его налоги
            for tax in tax_list:
                if tax['department'] is None:
                    user[tax["name"]] = tax["value_percents"]
                elif tax['department'].lower() == user['department']:
                    user[tax["name"]] = tax["value_percents"]
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

# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
# Функция для создания списка с зарплатами в отделе
def user_salary(department: list, gender: str = 'all') -> list:
    user_salary = []
    user_female = ["Michelle", "Nicole", "Christina", "Caitlin"]
    # Проход по сотрудникам в отделе
    for user in department["employers"]:
        # Фидбьр по гендеру
        if gender == 'all':
            # Составляем список с зарплатами
            user_salary.append(user["salary_rub"])
        elif gender == 'female':
            if user["first_name"] in user_female:
                # Составляем список с зарплатами
                user_salary.append(user["salary_rub"])
        elif gender == 'male':
            if user["first_name"] not in user_female:
                # Составляем список с зарплатами
                user_salary.append(user["salary_rub"])
        else:
            print("Не верно указан пол")
    return user_salary
# Функция для определения минимальной зарплаты в отделе
def departments_min_salary(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        # Вычисляем минимальную зарплату
        min_money = min(user_salary(department))    
        user_data.append(f"Минимальная зарплата в отделе {department['title']} равна {min_money}")
    need_print(user_data, 'Отчет по минимальной зарплате по отделам:', printing)
    return user_data
    
# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
def departments_salary(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        # Вычисляем зарплату
        salary = user_salary(department)
        min_money = min(salary) 
        max_money = max(salary) 
        mean_money = int(sum(salary)/len(salary))
        user_data.append(f"""В отделе {department['title']}: 
                         Минимальная зарплата: {min_money} 
                         Средняя зарплата: {mean_money}
                         Максимальная зарплата: {max_money}""")
    need_print(user_data, 'Отчет по зарплате по отделам:', printing)
    return user_data

# 9. Вывести среднюю зарплату по всей компании.
def mean_company_salery(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        # Записываем зарплаты в отделе
        salary = user_salary(department)
        user_data += salary
    # Вычисляем среднюю зарплату по компании
    mean_salary = int(sum(user_data)/len(user_data))
    need_print(mean_salary, 'Средняя зарплата в компании:', printing)
    return mean_salary

# 10. Вывести названия должностей, которые получают больше 90к без повторений.
def high_salary_position(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    position_max_salary = {}
    # Проход по списку со словарями
    for department in departments:
        # Добавляем должность в словарь, если ее еще там нет
        for user in department["employers"]:
            if position_max_salary.get(user["position"]) is None:
                position_max_salary[user["position"]] = 0
            # Записываем максимальную ЗП для каждой должности
            if user["salary_rub"] > position_max_salary.get(user["position"]):
                position_max_salary[user["position"]] = user["salary_rub"]
    # Формируем данные для вывода
    for employer_position, salary in position_max_salary.items():
        if salary > 90000:
            user_data.append(employer_position)
    need_print(user_data, 'Должности с зарплатой выше 90000 руб.::', printing)
    return user_data

# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
def mean_female_company_salery(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    # Проход по списку со словарями
    for department in departments:
        # Вычисляем зарплату в отделе
        salary = user_salary(department, 'female')
        user_data += salary
    # Вычисляем зарплату по компании
    mean_salary = int(sum(user_data)/len(user_data))
    need_print(mean_salary, 'Средняя зарплата в компании среди женщин:', printing)
    return mean_salary

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
def last_name_sorted(departments: list, printing: int = 0) -> list:
    # Список для хранения вывода
    user_data = []
    vowels_letter = ["a", "e", "i", "o", "u", "y"]
    # Проход по списку со словарями
    for department in departments:
        for user in department["employers"]:
            if user["last_name"][-1] in vowels_letter:
                if user["first_name"] not in user_data:
                    user_data.append(user["first_name"])
    need_print(user_data, 'Сотрудники с фамилией, заканчивающейся на гласную:', printing)
    return user_data        

# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.
# Функция для расчета налогов сотрудников в конкретном отделе
def department_quantity_users(departments: list, dep_name: str) -> int:
    quantity_users = 0
    for department in departments:
        if department['title'].lower() == dep_name.lower():
            quantity_users = len(department["employers"])
    return quantity_users

def departments_tax(departments: list, printing: int = 0) -> list:
    # Получаем список со словарями с данными по каждому сотруднику
    users = employers_data(departments)
    # Получаем список какие налог бывают
    tax_name = tax_names()
    # Список для сохранения данных по пользователям
    user_data = []
    # Список для вывода результата
    out_data = []
    # Рассчитаем налог для каждого пользователя
    for user in users:
        user_tax = 0
        # Перебираем все имена налога
        for tax in tax_name:
            # Если этот налог есть у пользователя в словаре, то считаем его
            if user.get(tax) is not None:
                user_tax += int(user["salary_rub"] * user[tax] / 100)
        # Создаем каждому пользователю новую пару в словаре с расчитаным налогом
        user["tax"] = user_tax
        # Записываем все в список
        user_data.append(user)
    # Словарь для сохранения суммарного налога по отделам
    department_tax_data = {}
    # Расчет суммарного налога для каждого из отделов
    for user in user_data:
        department_name = user["department"]
        if department_tax_data.get(department_name) is None:
            department_tax_data[department_name] = 0
        else:
            department_tax_data[department_name] += user["tax"]
    # Расчет среднего налога в отделе
    for data, tax in department_tax_data.items():
        quantity_users = department_quantity_users(departments, data)
        department_tax = int(tax / quantity_users)
        # Запись результатов в список
        out_data.append(f"Средний налог в отделе {data.upper()} равен: {department_tax}")
    need_print(out_data, 'Отчет по среднему налогу по отделам:', printing)
    return out_data

# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
def user_salary_info(departments: list, printing: int = 0) -> list:
    # Списки для хранения данных
    user_data = []
    name = []
    salary = []
    salary_tax = []
    # Получаем список со словарями с данными по каждому сотруднику
    users = employers_data(departments)
    # Берем все необходимое из данных, подготовленных ранее написанной функцией)
    for user in users:
        name = str(f"{user['first_name']} {user['last_name']}").ljust(20)
        salary = str(f"{user['salary_rub']-user['tax']}").ljust(15)
        salary_tax = str(f"{user['salary_rub']}").ljust(10)
        user_data.append(f"{name} {salary} {salary_tax}")
    need_print(user_data, 'Сотрудник              ЗП на руки      ЗП до вычета налогов', printing)
    return user_data

# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
def departments_sorted_tax(departments: list, printing: int = 0) -> list:
    # Получаем список со словарями с данными по каждому сотруднику
    users = employers_data(departments)
    # Получаем список какие налог бывают
    tax_name = tax_names()
    # Список для сохранения данных по пользователям
    user_data = []
    # Список для вывода результата
    out_data = []
    # Рассчитаем налог для каждого пользователя
    for user in users:
        user_tax = 0
        # Перебираем все имена налога
        for tax in tax_name:
            # Если этот налог есть у пользователя в словаре, то считаем его
            if user.get(tax) is not None:
                user_tax += int(user["salary_rub"] * user[tax] / 100)
        # Создаем каждому пользователю новую пару в словаре с расчитаным налогом
        user["tax"] = user_tax
        # Записываем все в список
        user_data.append(user)
    # Словарь для сохранения суммарного налога по отделам
    department_tax_data = {}
    # Расчет суммарного налога для каждого из отделов
    for user in user_data:
        department_name = user["department"]
        if department_tax_data.get(department_name) is None:
            department_tax_data[department_name] = 0
        else:
            department_tax_data[department_name] += user["tax"]
    # Сортируем ключи словаря по их значениям
    department_sorted_tax_list = sorted(department_tax_data, key = department_tax_data.get)
    # Расчет среднего налога в отделе
    # Проходим по названиям отделов в ранее полученном списке
    for data in department_sorted_tax_list:
        quantity_users = department_quantity_users(departments, data)
        department_tax = int(department_tax_data[data] / quantity_users)
        # Запись результатов в список
        out_data.append(f"Средний сортированный налог в отделе {data.upper()} равен: {department_tax}")
    need_print(out_data, 'Отчет по среднему налогу по отделам:', printing)
    return out_data

# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
def most_tax_emploers(departments: list, printing: int = 0) -> list:
    # Получаем список со словарями с данными по каждому сотруднику
    users = employers_data(departments)
    # Список для хранения данных
    user_data = []
    # Берем все необходимое из данных, подготовленных ранее написанной функцией)
    for user in users:
        name = str(f"{user['first_name']} {user['last_name']}").ljust(20)
        # Расчет налога за год
        year_tax = user['tax'] * 12
        if year_tax > 100000:
            user_data.append(f"{name} {year_tax}")
    need_print(user_data, 'Сотрудник              Налог за год', printing)
    return user_data

# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
def most_tax_emploers(departments: list, printing: int = 0) -> list:
    # Получаем список со словарями с данными по каждому сотруднику
    users = employers_data(departments)
    tax_dict = {}
    # Список для хранения данных
    user_data = []
    # Берем все необходимое из данных, подготовленных ранее написанной функцией)
    for user in users:
        name = str(f"{user['first_name']} {user['last_name']}")
        tax = user['tax']
        # Наполняем словарь пользователями с их налогами
        tax_dict[name] = tax
    # Ищем имя с минимальным налогом
    min_tax_key = min(tax_dict, key = tax_dict.get)
    # Готовим данные к выводу
    user_data.append(f"{min_tax_key} {tax_dict[min_tax_key]}")
    need_print(user_data, 'Меньше всего налогов платится за:', printing)
    return user_data


# Для удобной проверки
def run_function(number: int) -> Any:
    try:
        number = int(number)
        if number == 1:
            print('Задание № 1. Вывести названия всех отделов')
            take_departments(departments, 1)
        elif number == 2:
            print('Задание № 2. Вывести имена всех сотрудников компании.')
            employers_names(departments, 1)
        elif number == 3:
            print('Задание № 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.')
            user_list_vs_department(departments, 1)
        elif number == 4:
            print('Задание № 4. Вывести имена всех сотрудников компании, которые получают больше 100к.')
            employers_filter(departments, 100000, 1, 'more')
        elif number == 5:
            print('Задание № 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).')
            position_filter(departments, 80000, 1, 'less')
        elif number == 6:
            print('Задание № 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела')
            departments_expenses(departments, 1)
        elif number == 7:
            print('Задание № 7. Вывести названия отделов с указанием минимальной зарплаты в нём.')
            departments_min_salary(departments, 1)
        elif number == 8:
            print('Задание № 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.')
            departments_salary(departments, 1)
        elif number == 9:
            print('Задание № 9. Вывести среднюю зарплату по всей компании.')
            mean_company_salery(departments, 1)
        elif number == 10:
            print('Задание № 10. Вывести названия должностей, которые получают больше 90к без повторений.')
            high_salary_position(departments, 1)
        elif number == 11:
            print('Задание № 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).')
            mean_female_company_salery(departments, 1)
        elif number == 12:
            print('Задание № 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.')
            last_name_sorted(departments, 1)
        elif number == 13:
            print('Задание № 13. Вывести список отделов со средним налогом на сотрудников этого отдела.')
            departments_tax(departments, 1)
        elif number == 14:
            print('Задание № 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.')
            user_salary_info(departments, 1)
        elif number == 15:
            print('Задание № 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.')
            departments_sorted_tax(departments, 1)
        elif number == 16:
            print('Задание № 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.')
            most_tax_emploers(departments, 1)
        elif number == 17:
            print('Задание № 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.')
            most_tax_emploers(departments, 1)
        else:
            print('\nУкажите номер из доступных\n')
    except ValueError:
        print(f'Некорректный ввод: {number}')
        return None

# Функция для запуска
def main():
    while 1:
        number = input(f"""Для остановки введите exit\nДоступные номера задач: 1-17\nВведите номер проверяемой задачи:""")
        if number == 'exit':
            break
        run_function(number)
    

if __name__ == "__main__":
    main()

