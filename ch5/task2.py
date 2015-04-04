__author__ = 'm'

НЕ РАБОТАЕТ!!!
ПОТОМУ ЧТО НЕ ПРОДУМАНА ЛОГИКА!!!

################################################
# "Генератор персонажей"                       #
# Необходимо расположить 30 пунктов по скилам: #
#   Сила                                       #
#   Здоровье                                   #
#   Мудрость                                   #
#   Ловкость                                   #
################################################

choice = None
pool = 30
skills = [
    ["Сила    " , 0],
    ["Здоровье" , 0],
    ["Мудрость" , 0],
    ["Ловкость" , 0]
]

while choice != 0:
    print("""
    У вас имеется " + str(pool) + " пунктов.
    Ваши умения:
    """)
    for skill in skills:
        print(skills.index(skill) + 1, end=". ")
        print(skill[0], end=" : ")
        print(skill[1])
    choice = int(input("Выберите навык, который хотите изменить:"))
    if choice == 0:
        print("Пока!")
    elif choice < len(skills):
        skill_index = choice
        choice = input("""
        Выберите действие:
            1 - Увеличить
            2 - Уменьшить
            0 - венуться в пердыдущее меню
        """)
        if choice in [1, 2]:
            if choice == 1:
                delta_points = 1
            else:
                delta_points = -1
            delta_points *= int(input("Введите на сколько хотите изменить навык: "))
            while pool + delta_points < 0:
                if choice == 1:
                    delta_points = 1
                else:
                    delta_points = -1
                delta_points *= int(input("У вас не столько поинтов: "))
