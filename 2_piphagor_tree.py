import turtle

def draw_pythagoras_tree(t, length, level):
    """
    Рекурсивно малює фрактальне дерево.
    :param t: об'єкт Turtle
    :param length: довжина гілки
    :param level: рівень рекурсії
    """
    if level > 0:
        # Встановити колір: стовбур коричневий, листя зелене
        if level > 4:
            t.pencolor("green")
        else:
            t.pencolor("brown")

        t.forward(length)

        angle = 30  # кут відхилення гілок

        # Рекурсивно намалювати ліве піддерево
        t.left(angle)
        draw_pythagoras_tree(t, length * 0.7, level - 1)

        # Рекурсивно намалювати праве піддерево
        t.right(2 * angle)
        draw_pythagoras_tree(t, length * 0.7, level - 1)

        # Повернутися до початкової точки гілки
        t.left(angle)
        t.backward(length)

def main():
    """
    Основна функція для налаштування та запуску малювання.
    """
    try:
        # Запитати у користувача рівень рекурсії
        level_str = turtle.textinput("Дерево Піфагора", "Введіть рівень рекурсії (1-10):")
        if level_str is None:
             print("Скасовано користувачем. Використовується рівень за замовчуванням 5.")
             level = 5
        else:
            level = int(level_str)
        if not 1 <= level <= 12:
            print("Некоректний рівень. Встановлено рівень 5.")
            level = 5
    except (ValueError, TypeError):
        print("Некоректний ввід. Використовується рівень за замовчуванням 5.")
        level = 5

    # Налаштування вікна
    window = turtle.Screen()
    window.bgcolor("white")
    window.tracer(0)  # Вимкнути анімацію
    
    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  # найвища швидкість
    t.hideturtle()
    
    # Початкова позиція
    t.penup()
    t.goto(0, -250)
    t.left(90)  # направити вгору
    t.pendown()

    # Почати малювання
    draw_pythagoras_tree(t, 100, level)

    window.update()  # Оновити екран, щоб показати результат
    # Завершити
    window.mainloop()

if __name__ == "__main__":
    main()
