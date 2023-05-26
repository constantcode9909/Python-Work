# the code asks the user for a text to process and makes sure it is not empty and strips the text of any unnecessary whitespaces
subject_text_one = input("please provide the initial text (the text must not be empty): ")
while len(subject_text_one) == 0 :
    subject_text_one = input("you have provided an empty word : ")
subject_text_two = subject_text_one.strip()



# this code asks the user to give the words he wants to replace , it makes sure that the words given are not repeated
list_of_words = []
while True:
    word_to_replace = input('please provide words to replace (or write done if you are finished to proceed)')
    while word_to_replace in list_of_words:
        word_to_replace = input("this word has been already saved , please enter another one or write done if you are finished")
    if word_to_replace.lower() == "done" :
        break
    list_of_words.append(word_to_replace)


# this code asks the user for the word replacements and makes sure the numbers of words to replace and their replacements are even
list_of_replacements = []
while True:
    replacement = input('please provide your replacements (please provide the same number of words as you did in the words you want to replace)')
    list_of_replacements.append(replacement)
    if len(list_of_words) == len(list_of_replacements) :
        break


# here I use a list to make sure i get the full changed word because words in python are immutable which means they cannot be changed
# the problem that the replace method returns a new word every time it is used
index = 0
results_list = []
while index <= len(list_of_replacements) - 1:
    new_string_content = ""
    if index == 0:
            new_string_content = subject_text_two.replace(list_of_words[index] , list_of_replacements[0])
            results_list.append(new_string_content)
    else:
            new_string_content = results_list[index - 1].replace(list_of_words[index] , list_of_replacements[index])
            results_list.append(new_string_content)
    index += 1

final_result = results_list[len(results_list) - 1]
print("here is the final result : " , final_result)
