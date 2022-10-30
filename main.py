import json


def get_quiz_data():  # get all the data
    with open('quiz.json') as f:
        quiz_temp = json.load(f)
    return quiz_temp


def get_fields(quiz_temp):  # get all the fields
    return list(quiz_temp["quiz"].keys())


def print_choices(fields_temp):  # print all the choices
    print("please choose on of the following fields")
    for i in fields:
        print(i)


def quiz_verification(chosen_field_temp):
    mark = 0
    for i in chosen_field_temp.keys():
        choices = list(chosen_field_temp[i].keys())
        print(chosen_field_temp[i][choices[0]])
        print(chosen_field_temp[i][choices[1]])
        answer = input();
        if answer == chosen_field_temp[i][choices[2]]:
            mark += 1
            print("your answer was true")
        else:
            print("your answer was false, correct answer " + chosen_field_temp[i][choices[2]] + "\n")
    return mark


quiz = get_quiz_data()

fields = get_fields(quiz)

print_choices(fields)

field_choice = input()
chosen_field = quiz["quiz"][field_choice]

mark = quiz_verification(chosen_field)

print("total mark:", mark)
