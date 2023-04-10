name = input()  # прочитаме името на ученика
grade_sum = 0  # тук ще сумираме оценките му
exclusions = 0  # тук ще броим колко пъти е бил изключван
current_grade = float(input())  # прочитаме първата годишна оценка

while exclusions < 2:  # докато не е бил изключен повече от два пъти
    if current_grade >= 4.00:  # ако е минал класа
        grade_sum += current_grade  # добавяме оценката му към сумата
        current_grade = float(input())  # прочитаме следващата оценка
    else:
        exclusions += 1  # увеличаваме броя на изключванията
        if exclusions == 2:  # ако е бил изключен два пъти
            print(f"{name} has been excluded at {grade} grade")
        else:  # ако не е бил изключен два пъти, значи е бил скъсан
            grade = 1 + exclusions  # пресмятаме в кой клас е бил скъсан
            print(f"{name} has been excluded at {grade} grade")
            break  # прекъсваме цикъла, защото няма смисъл да продължаваме

if exclusions < 2:  # ако не е бил изключен два пъти
    avg_grade = grade_sum / 12  # пресмятаме средната оценка
    print(f"{name} graduated. Average grade: {avg_grade:.2f}")

