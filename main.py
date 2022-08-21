# Raw METHOD:
# with open("Input/Letters/starting_letter.txt") as letter:
#     content = letter.read()
#     with open("Input/Names/invited_names.txt") as names:
#         names_list = names.readlines()
#         for name in names_list:
#             stripped_name = name.strip()
#             with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as ready_letter:
#                 new_content = content.replace("[name]", stripped_name)
#                 ready_letter.write(new_content)

# Optimized method:
PLACE_HOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = content.replace(PLACE_HOLDER, stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as ready_letter:
            ready_letter.write(new_letter)

