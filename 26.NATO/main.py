import pandas

data = pandas.read_csv('./26.NATO/nato.csv')
print(data.to_dict())
print(data)

phone_dict = {row.letter: row.code for(index, row) in data.iterrows()}
print(phone_dict)

word = input("Enter a word: ").upper()
output_list = [phone_dict[letter] for letter in word]
print(output_list)