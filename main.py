import pandas
nato_alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_nato_alpha_dict = {row.letter:row.code for (index, row) in nato_alpha_data.iterrows()}

user_data = input("Please enter a word or a name: ").upper()
user_nato_dict = {x:new_nato_alpha_dict[x] for x in user_data if x in new_nato_alpha_dict}
print (user_nato_dict)

