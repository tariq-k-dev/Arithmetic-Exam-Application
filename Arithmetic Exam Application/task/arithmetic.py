# write your code here
import random


count = 0
num_correct = 0
level = 0
levels = {1: 'simple operations with numbers 2-9', 2: 'integral squares of 11-29'}
level_prompt = f'Which level do you want? Enter a number:\n' \
                f'1 - {levels.get(1)}\n' \
                f'2 - {levels.get(2)}'
answer = None
math_question = None

# Let user set difficulty level
print(level_prompt)
while True:
    try:
        level = int(input())
        break
    except ValueError:
        print('Invalid selection!')

while count < 5:
    random.seed()
    if level == 1:
        first_number = random.randint(2, 9)
        second_number = random.randint(2, 9)
        operators = ['+', '-', '*']
        operator = random.choice(operators)

        if operator == '+':
            answer = first_number + second_number
        elif operator == '-':
            answer = first_number - second_number
        elif operator == '*':
            answer = first_number * second_number

        math_question = f"{str(first_number)} {operator} {str(second_number)}"
    elif level == 2:
        number = random.randint(11, 29)
        answer = number ** 2
        math_question = f"{str(number)}"

    while True:
        print(math_question)
        try:
            user_answer = int(input())

            if user_answer == answer:
                print("Right!")
                num_correct += 1
            else:
                print("Wrong!")

            break
        except ValueError:
            print("Incorrect format.")
            continue

    count += 1

print(f"Your mark is {num_correct}/5. Would you like to save the result? Enter yes or no.")
save_result = input()

if save_result in ['y', 'yes', 'Yes', 'Y', 'YES']:
    name = input('What is your name? ')
    result_text = f'{name}: {num_correct}/5 in level {level} ({levels.get(level)}).'
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(result_text + '\n')
    file.close()
    print('The results are saved in "results.txt".')
