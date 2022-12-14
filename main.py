import json
from logging import exception


def get_quiz_data() -> dict:
    """ the function aime to read the data from the input file

    Args:
        this function doesn't need any arguments

    Returns:
        The return value is a dictionary of the input data
    """
    with open('quiz.json') as f:
        quiz_temp = json.load(f)
    return quiz_temp


def get_fields(quiz_temp: dict) -> list:
    """this function aims to get the values of keys in the received dictionary
        Args:
            quiz_temp: represent the input data read from the quiz file as a dictionary

        Returns:
            The return value is the keys of quiz_temp as a list
    """
    return list(quiz_temp["quiz"].keys())


def print_list(temp: list):
    """this function aims print the values in the received list
            Args:
                temp: represents the received list

            Returns:
                there is no return value.
    """
    counter = 1
    for i in temp:
        print(counter, ") ", i)
        counter += 1


def quiz_verification(questions: dict) -> int:
    """this function aims to present the quiz question, take the answers, verify them and give an evaluation
            Args:
                questions: a list that represents the questions

            Returns:
                The return value is the overall evaluation/mark
    """
    mark = 0
    tries = 0
    for i in questions.keys():
        choices = list(questions[i].keys())

        while tries != 3:
            print(questions[i][choices[0]])  # question descrrption
            print_list(questions[i][choices[1]])  # question choices
            answer = input()

            try:
                if int(answer) < 1:
                    print("the entered value is wrong, please try again")
                    tries += 1
                    continue
                if questions[i][choices[1]][int(answer) - 1] == questions[i][choices[2]]:  # choosen ans=real ans
                    mark += 1
                    print("your answer was true")
                else:
                    print("your answer was false, correct answer " + questions[i][choices[2]] + "\n")
                break
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                tries += 1

    return mark


if __name__ == "__main__":
    print("do u want to take the quiz:")
    print("1 ) Yes" + "\n" + "2 ) No")
    first_choice = input()
    try:
        condition = int(first_choice) == 1
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    if not condition:
        print("the entered value is wrong, please try again")
        exit(1)

    quiz = get_quiz_data()
    fields = get_fields(quiz)  # list of field (sports, math)

    tries = 0
    while tries != 3:
        print("please choose one of the following fields")
        print_list(fields)
        print("3 )  exit")
        field_choice = input()  # sport or math

        try:
            questions = quiz["quiz"][fields[int(field_choice) - 1]]  # list of questions

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            tries += 1

        if int(field_choice) < 1:
            print("the entered value is wrong, please try again")
            tries += 1
            continue
        elif int(field_choice) == 3:
            exit()
        mark = quiz_verification(questions)
        print("total mark:", mark)
        tries = 3
