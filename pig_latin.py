#Create ending for pig latin words as a variable
pyg = 'ay'

#Take user input of word
original = input('Enter a word:')

#Check if user input is empty, only alphabetical characters
if len(original) > 0 and original.isalpha():
    #Return original variable as lowercase
	word = original.lower()
    #Hold first letter of user input
	first = word[0]
	#Take user input, minus first letter, plus other variables and print it
    new_word = word[1:len(word)] + first + pyg
    print(new_word)
else:
    print('empty')