""" Module to determine user career """

# Store career options in a list or in variables

career_options = ['medicine', 'journalism', 'technology',]

career_advices = ['Seek internship opportunities',
                  'Grow your skills and knowledge',
                  'Keep your skills up-to-date']

career_questions = ['What is your favourite area of study? \
Sciences, Languages, Technology: ', 'Do you prefer to work onsite or offsite?: ']

answer = []
for quest in career_questions: 
  answer.append(input(quest))



if answer[0].lower() == 'languages':
  print('Your career option is: Journalism')

elif answer[0].lower() == 'sciences' and answer[1].lower() == 'onsite':
  print('Your career option is: Medicine')

elif answer[0].lower() == 'sciences' and answer[1].lower == 'offsite':
  print('Your career option is: Farming')

elif answer[0].lower() == 'technology':
  print('Your career option is: Technology')

else:
  print('ERROR! Choose from the available options')
