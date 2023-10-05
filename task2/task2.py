import csv
from collections import defaultdict
from typing import List, Dict, Tuple


def read_data(filename: str) -> Dict[str, Dict[str, List[Tuple[str, float, float]]]]:
    """
    Читает данные из CSV-файла и возвращает словарь с информацией о сотрудниках.

    :param filename: Имя файла с данными.
    :return: Словарь с информацией о сотрудниках.
    """
    data = defaultdict(lambda: defaultdict(list))
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)  # пропускаем заголовок
        for row in reader:
            name, department, team, position, review, salary = row
            data[department][team].append((name, float(review), float(salary)))
    return data


def print_teams(data: Dict[str, Dict[str, List[Tuple[str, float, float]]]]):
    """
    Выводит иерархию команд на экран.

    :param data: Словарь с информацией о сотрудниках.
    """
    for department in data:
        print(department)
        for team in data[department]:
            print("  ", team)


def report(
    data: Dict[str, Dict[str, List[Tuple[str, float, float]]]]
) -> Dict[str, Tuple[int, float, float, float]]:
    """
    Создает отчет по департаментам.

    :param data: Словарь с информацией о сотрудниках.
    :return: Словарь с отчетом по департаментам.
    """
    report_data = {}
    for department in data:
        min_salary = float("inf")
        max_salary = 0
        total_salary = 0
        count = 0
        for team in data[department]:
            for name, review, salary in data[department][team]:
                min_salary = min(min_salary, salary)
                max_salary = max(max_salary, salary)
                total_salary += salary
                count += 1
        report_data[department] = (count, min_salary, max_salary, total_salary / count)
    return report_data


def print_report(report_data: Dict[str, Tuple[int, float, float, float]]):
    """
    Выводит отчет на экран.

    :param report_data: Словарь с отчетом по департаментам.
    """
    for department in report_data:
        count, min_salary, max_salary, avg_salary = report_data[department]
        print(
            f"{department}: {count} сотрудников; зарплата {min_salary}-{max_salary} (средняя {avg_salary})"
        )


def save_report(filename: str, report_data: Dict[str, Tuple[int, float, float, float]]):
    """
    Сохраняет отчет в виде CSV-файла.

    :param filename: Имя файла для сохранения отчета.
    :param report_data: Словарь с отчетом по департаментам.
    """
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "Департамент",
                "Численность",
                "Минимальная зарплата",
                "Максимальная зарплата",
                "Средняя зарплата",
            ]
        )
        for department in report_data:
            count, min_salary, max_salary, avg_salary = report_data[department]
            writer.writerow(
                [department, count, min_salary, max_salary, f"{avg_salary:.2f}"]
            )


def main():
    """
    Главная функция программы. Читает данные из файла,
    предоставляет пользователю меню для просмотра иерархии команд,
    просмотра сводного отчета по департаментам и сохранения этого отчета в виде CSV-файла.
    """
    data = read_data(r"Corp_Summary.csv")
    while True:
        print("1. Вывести иерархию команд")
        print("2. Вывести сводный отчёт по департаментам")
        print("3. Сохранить сводный отчёт в виде csv-файла")
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            print_teams(data)
        elif choice == "2":
            report_data = report(data)
            print_report(report_data)
        elif choice == "3":
            report_filename = input("Введите имя файла для сохранения отчёта: ")
            if not report_filename.endswith(".csv"):
                report_filename += ".csv"
            report_data = report(data)
            save_report(report_filename, report_data)


if __name__ == "__main__":
    main()
