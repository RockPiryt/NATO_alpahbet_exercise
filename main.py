import pandas


# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_df = pandas.read_csv('nato_alphabet.csv')

# new_dict = {new_key:new_value for (index,row) in dict.iterrows() if test}
alphabet_dict = {row.letter: row.code for (index, row) in data_df.iterrows()}
print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#__________________________________GOOD SOLUTION__________________________
user_input = input("Please write your word: ").upper() #LEONEK - string.upper()
output = [alphabet_dict[letter] for letter in user_input]
print(output)

# #___________________NOT GOOD SOLUTION TO EXERCISE_________________
#change string to list of characters - list()method
# listed_word = list(user_input)
# print(listed_word)
# {'A': 'Alfa', 'C': 'Charlie', 'E': 'Echo', 'G': 'Golf', 'H': 'Hotel', 'K': 'Kilo', 'O': 'Oscar', 'R': 'Romeo', 'T': 'Tango', 'Z': 'Zulu'}

#change string to list of characters - string comprehension
# listed_word_compre = [letter for letter in user_input]
# print(listed_word_compre)



#search letter in alphabet dict_______________________________________

# # new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# nato_letter = {letter:code for (letter,code) in alphabet_dict.items() if letter in listed_word}
# print(nato_letter)
# # #{'A': 'Alfa', 'I': 'India', 'L': 'Lima', 'N': 'November', 'P': 'Papa', 'U': 'Uniform'} - letter with code in word 'Paulina'

# # new_dict={new_key:new_value for item in list if test}
# phonetic_word = {nato_letter[letter] for letter in listed_word if letter in nato_letter}
# print(phonetic_word)#only phonetic codes
# #{'Zulu', 'Golf', 'Echo', 'Kilo', 'Hotel', 'Oscar', 'Alfa', 'Tango', 'Charlie', 'Romeo'}


# #BAD
# # # new_dict={new_key:new_value for item in list if test}
# # phonetic_word = {nato_letter['code'] for letter in listed_word if letter in nato_letter}
# # print(phonetic_word)