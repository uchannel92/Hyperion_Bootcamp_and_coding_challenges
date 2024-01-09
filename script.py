filename = 'text.txt'

text_file_data = ''
data = []

with open(filename, 'r') as file_obj:
    content = file_obj.readlines()
    text_file_data = content

# print("".join(text_file_data))
for line in (text_file_data):
   print(line.split(" "))


# remove all the letters that are more than 5 characters
# add back into a string
# then write back into text file using 'w'