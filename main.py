HELP = """ help - напечатать справку по программе.
 add - добавить задачу в список.
 show - напечатать все добавленные задачи.
 exit - выход из программы
 random - добавляет случайную задачу на сегодняшнюю дату"""
import random
RANDOM_TASKS = ["Записаться на курс", "Помыть машину", "Погладить одежду", "Погладить кошку"]
notes = {}
run = True
def add_todo(date, task):
     if date in notes:
         notes[date].append(task)
     else:
         notes[date] = []
         notes[date].append(task)
     print("Задача добавлена")
def count_letter(spisok, bykva):
    count = 0
    for i in range(len(spisok)):
        if bykva in spisok[i]:
            count += 1
    return count
print(HELP)
while (run):
    command = input("\nВведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in notes:
            for task in notes[date]:
                print(" - ", task)
        else:
            print("Такой даты нет(")
    elif command == "add":
        task = input("Введите задачу: ")
        date = input("Введите дату исполнения задачи: ")
        add_todo(date, task)

    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
    else:
        print("Неизвестная команда")
