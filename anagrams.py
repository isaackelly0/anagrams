#load digital dictionary file as a list of words
from load_dictionary import load

word_list = load('./lang/2of4brif.txt')
#accept a word from user
name = 'Foster'
print('Input name = {}'.format(name))
name = name.lower()
print('Using name = {}'.format(name))

#create an empty list to hold anagrams
anagram_list = []
#sort the user word
name_sorted = sorted(name)
#loop through each word in the word list:
for word in word_list:
    word = word.lower()
    if word != name:
    #sort the word
        #if word sorted is equal to user word:
        if sorted(word) == name_sorted:
            #append word to anagrams word list
            anagram_list.append(word)
#print anagrams list
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name")
else:
    print("Anagrams =", *anagram_list, sep="\n")
