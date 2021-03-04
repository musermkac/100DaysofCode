import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


top_title = "Guess the state"
top_prompt = "Share a state's name if you know!"

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

score = 0
guess_list = []

while score < 50:

        answer = screen.textinput(title=top_title, prompt=top_prompt).title()
        print(answer)#Just for verification

        if answer in states_list:
            if answer not in guess_list:
                print(answer)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()

                state_row = states[states.state == answer]
                print(state_row) #Just for verification

                t.goto(int(state_row.x),int(state_row.y))
                t.write(answer)

                score += 1
                top_title = f"Your score is {score}/50"
                guess_list.append(answer)

turtle.mainloop()


