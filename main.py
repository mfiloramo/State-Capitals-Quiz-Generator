import os
import random


# Define the variable of the quiz dir.
cwd = 'C:\\Users\\sitedirector\\Desktop\\Quiz Directory'

# Create the directory for the quiz files
os.makedirs(cwd)

# Create the 35 blank quiz files.
for i in range(1, 36):
    open(f'{cwd}\\Quiz - {i}.txt', 'w')

# Define the dictionary of states and capitals.
capitals = {'Alabama': 'Montgomery',
            'Alaska': 'Juneau',
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock',
            'California': 'Sacramento',
            'Colorado':'Denver',
            'Connecticut': 'Hartford',
            'Delaware': 'Dover',
            'Florida': 'Tallahassee',
            'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu',
            'Idaho': 'Boise',
            'Illinois':'Springfield',
            'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines',
            'Kansas':'Topeka',
            'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta',
            'Maryland': 'Annapolis',
            'Massachusetts': 'Boston',
            'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City',
            'Montana': 'Helena',
            'Nebraska': 'Lincoln',
            'Nevada': 'Carson City',
            'New Hampshire': 'Concord',
            'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck',
            'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence',
            'South Carolina': 'Columbia',
            'South Dakota': 'Pierre',
            'Tennessee': 'Nashville',
            'Texas': 'Austin',
            'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier',
            'Virginia': 'Richmond',
            'Washington': 'Olympia',
            'West Virginia': 'Charleston',
            'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne',
            }

# Write 50 randomized multiple-choice questions to each created quiz document.
for i in range(1, (len(os.listdir(cwd))) + 1):
    states_list = list(capitals.keys())
    for num in range(1, 51):
        state = random.choice(states_list)

        # Randomize the choice possibilities.
        choices_dict = {
            1: capitals[state],
            2: random.choice(list(capitals.values())),
            3: random.choice(list(capitals.values())),
            4: random.choice(list(capitals.values())),
        }
        choices_seq = random.sample(range(1, 5), 4)

        # Create the questions with randomized choices (formatted).
        open(f'{cwd}\\Quiz - {i}.txt', 'a').write(f'''\
{num}. What is the capital of {state}?\n
    (A) {choices_dict[(choices_seq[0])]}
    (B) {choices_dict[(choices_seq[1])]}
    (C) {choices_dict[(choices_seq[2])]}
    (D) {choices_dict[(choices_seq[3])]}\n
''')
        # Answer key generator.
#         open(f'{cwd}\\Quiz - {i} Answer Key.txt', 'a').write(f'''\
# {num}. The correct answer to {state} is {capitals[state]}.\n
# ''')
        states_list.remove(state)

print('Your quizzes have been automatically generated!')