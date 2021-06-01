string = input()
vowels = []
words = []
start_index = 0
for index in range(len(string)):
    if string[index].lower() in "aeiou":
        vowels.append(string[index])
        words.append(string[start_index:index])
        start_index = index+1
if string[start_index:] !="":
    words.append(string[start_index:])
words.reverse()
reverse_string = ""
for index in range(len(words)):
    if index < len(words):
        reverse_string += words[index]
    if index < len(vowels):
        reverse_string += vowels[index]

print(reverse_string)