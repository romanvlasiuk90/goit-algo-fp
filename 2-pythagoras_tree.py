import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    # Малюємо поточну гілку
    t.forward(branch_length)
    
    # Зберігаємо поточну позицію та кут
    x, y = t.position()
    angle = t.heading()

    # Малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    
    # Повертаємося до збереженої позиції та кута
    t.penup()
    t.setposition(x, y)
    t.setheading(angle)
    t.pendown()

    # Малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

# Основна функція для малювання дерева Піфагора
def main():
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")

    # Користувач вказує рівень рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Почати з вертикальної лінії

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()

if __name__ == "__main__":
    main()