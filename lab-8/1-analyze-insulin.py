import os


#open file in read mode
file = open("./lab-8/preproinsulin-seq.txt", "r")

#read the content of file
data = file.read()
out = open("./lab-8/preproinsulin-seq-clean.txt", "wt")
char_to_replace = {" " : "", "//": "", "1":'',"2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","0":""}


for key, value in char_to_replace.items():
    # Replace key character with value character in string
    
    data=data.replace(key, value)

    

print(data)
out.write(data)
number_of_characters = len(data)
""" number_of_characters_2 = len(out) """

print('Number of characters in text file :', number_of_characters)


data.close()
out.close()







