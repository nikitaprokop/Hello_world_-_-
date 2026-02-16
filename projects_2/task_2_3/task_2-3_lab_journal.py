researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату проведения (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод по эксперименту: ")

with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"|{'Электронный лабораторный журнал':^50}|\n")
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"| ФИО исследователя : {researcher_name:<31}|\n")
    file.write(f"| Дата              : {experiment_date:<31}|\n")
    file.write(f"| Эксперимент       : {experiment_name:<31}|\n")
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"| {'Вывод:':<49}|\n")

    words = experiment_conclusion.split()
    current_line = "| "
    for word in words:
        if len(current_line) + len(word) + 1 <= 49:
            current_line += word + " "
        else:

            file.write(f"{current_line:<49}|\n")
            current_line = "| " + word + " "

    if len(current_line) > 2:
        file.write(f"{current_line:<49}|\n")


    file.write("+" + "-" * 50 + "+\n")

print(f"\nЗапись в электронный журнал успешно создана в файле journal.txt")

