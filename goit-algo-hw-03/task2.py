import turtle
import sys


def koch_curve(t, order, size):
    """
    recursively draws a Koch curve of a given order and size.

    Args:
        t: об'єкт turtle
        order: рівень рекурсії (глибина фракталу)
        size: довжина сегмента
    """
    if order == 0:
        # base case: just draw a straight line
        t.forward(size)
    else:
        # recursive case: divide the line into 3 segments and create the Koch pattern
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)


def koch_snowflake(t, order, size):
    """
    draws a Koch snowflake by drawing three Koch curves.

    Args:
        t: об'єкт turtle
        order: рівень рекурсії
        size: розмір сторони
    """
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main():
    """
    main function to set up the turtle environment and draw the Koch snowflake.
    """
    # get recursion order from command line or user input
    try:
        if len(sys.argv) > 1:
            order = int(sys.argv[1])
        else:
            order = int(input("Type the recursion order (1-5 recomended): "))

        if order < 0:
            print("Level must be a non-negative integer!")
            return

        if order > 7:
            print("High levels may take a long time to draw. Proceeding anyway...")

    except ValueError:
        print("put a valid integer number for the level!")
        return

    # setting up the turtle environment
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch Snowflake - Level {order}")

    # setting up the turtle
    t = turtle.Turtle()
    t.speed(0)  # max speed
    t.color("blue")
    t.pensize(1)

    # positioning the turtle
    size = 300
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # drawing the Koch snowflake
    print(f"Draw Koch snowlake with recarssion level {order}...")

    # speed up drawing for high recursion levels
    if order > 3:
        turtle.tracer(0, 0)

    koch_snowflake(t, order, size)

    # update the drawing if tracer was turned off
    if order > 3:
        turtle.update()

    print("Drawing complete!")

    # hide the turtle cursor
    t.hideturtle()

    # close the window on click
    window.exitonclick()


if __name__ == "__main__":
    main()
