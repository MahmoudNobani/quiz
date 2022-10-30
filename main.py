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
    for i in temp:
        print(i)


def quiz_verification(questions: dict) -> int:
    """this function aims to present the quiz question, take the answers, verify them and give an evaluation
            Args:
                questions: a list that represents the questions

            Returns:
                The return value is the overall evaluation/mark
    """
    mark = 0
    for i in questions.keys():
        choices = list(questions[i].keys())
        print(questions[i][choices[0]])
        print(questions[i][choices[1]])
        answer = input();
        if answer == questions[i][choices[2]]:
            mark += 1
            print("your answer was true")
        else:
            print("your answer was false, correct answer " + questions[i][choices[2]] + "\n")
    return mark


quiz = get_quiz_data()

fields = get_fields(quiz) #list of field (sports, math)

print("please choose on of the following fields")
print_list(fields)

field_choice = input() #sport or math

chosen_q = quiz["quiz"][field_choice] #list of questions
print(type(chosen_q))

mark = quiz_verification(chosen_q)

print("total mark:", mark)
