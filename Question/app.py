from Question import Question

question_prompts = [
    "What color is banana?\na. Yellow\nb. Black\nc. Red\n",
    "What color is strawberry?\na. Magenta\nb. Red\nc. Green\n",
    "What color is apple?\na. Green\nb. Red\nc. Blue\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[0], "b")
]

def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score is " + str(score) + "/3")

ask_questions(questions)