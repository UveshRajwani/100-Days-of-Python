# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
file = pandas.read_csv("nato_phonetic_alphabet.csv")
file1 = {row.letter: row.code for (index, row) in file.iterrows()}
print(file1)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("What is you name ").upper()
user = list(user)
answer = [file1[n] for n in user]
print(answer)