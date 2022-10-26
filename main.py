import json
f = open('quiz.json')

quiz = json.load(f)

fields = list(quiz["quiz"].keys())
print("please choose on of the following fields")
for i in fields:
    print(i)
field_choice = input();
chosen_field = quiz["quiz"][field_choice]

mark=0
print(chosen_field.keys())
for i in chosen_field.keys():
    choices = list(chosen_field[i].keys())
    print(chosen_field[i][choices[0]])
    print(chosen_field[i][choices[1]])
    answer = input();
    if answer ==  chosen_field[i][choices[2]]:
        mark+=1
        print("your answer was true")
    else:
        print("your answer was false, correct answer "+chosen_field[i][choices[2]]+"\n")

print("total mark:",mark)