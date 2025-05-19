from capitals import capitals
import random

number_of_students = 1

for quiz_num in range(number_of_students):
  # Create the quiz and answer key files.
  quiz_file =  open(f'capitalquiz{quiz_num+1}.txt', 'w', encoding='utf-8')
  answer_file = open(f'capitalquiz_answer{quiz_num+1}.txt', 'w', encoding='utf-8')

  # Write out the header for the quiz.
  quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
  quiz_file.write(f'{" " * 20}State Capitals Quiz (Form {quiz_num+1}) ')
  quiz_file.write('\n\n') 

  # Shuffle the order of the states.
  states = list(capitals.keys())
  random.shuffle(states) 

  # Loop through all 50 states, make a question for each.
  for num in range(50):
    # Get right and wrong answers.
    correct_answer = capitals[states[num]]
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)

    # Write the question and answer options to the quiz file.
    quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
    for i in range(4):
      quiz_file.write(f"    { 'ABCD'[i]}. { answer_options[i]}\n")
    quiz_file.write('\n')

    # Write the answer key to a file.
    answer_file.write(f"{num + 1}.{'ABCD'[answer_options.index(correct_answer)]}")
  
  quiz_file.close()
  answer_file.close()