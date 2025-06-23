PLACEHOLDER = "[name]"

with open('./24.File Structure/input/invited_names.txt') as names_file:
    names = names_file.readlines()
    print(names)

with open('./24.File Structure/input/starting_letter.docx') as letter_file:
    letter = letter_file.read()
    print(letter)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"./24.File Structure/output/letter_for_{stripped_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)
            print(completed_letter)