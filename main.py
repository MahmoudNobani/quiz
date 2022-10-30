import json


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
    flagx = 0
    for i in questions.keys():
        choices = list(questions[i].keys())

        while flagx != 3:
            print(questions[i][choices[0]])  # question descrrption
            print_list(questions[i][choices[1]])  # question choices
            answer = input()
            try:
                if questions[i][choices[1]][int(answer) - 1] == questions[i][choices[2]]:
                    mark += 1
                    print("your answer was true")
                else:
                    print("your answer was false, correct answer " + questions[i][choices[2]] + "\n")
                break
            except:
                print("the entered value is out of the defined range, please try again")
                flagx += 1

    return mark


print("do u want to take the quiz:")
print("1 ) Yes" + "\n" + "2 ) No")
first_choice = input()
if int(first_choice) == 1:
    quiz = get_quiz_data()

    fields = get_fields(quiz)  # list of field (sports, math)

    flag = 0
    while flag != 3:
        print("please choose one of the following fields")
        print_list(fields)
        field_choice = input()  # sport or math
        try:
            chosen_q = quiz["quiz"][fields[int(field_choice) - 1]]  # list of questions
            mark = quiz_verification(chosen_q)
            print("total mark:", mark)
            flag = 3
        except:
            print("the entered value is wrong, please try again")
            flag += 1
else:
    exit()
