#Imports:
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

#Taking Inputs From The User:
print ("Please Enter The Text You Want To Tokenize ❤️")
x = input()
print ("Do You Want A Word Or A Sentence Tokenization ?")
dec = input()

#Assign The Compound Words That We Want To Deal With As One Word:
compound_text = ["Los Angelos","Abu Dhabi", "Great Cairo"]

#Replacing The Space (" ") Between It With An Undescore ("_") That The Machine Recognizes It As One Word:
for i in compound_text:
    x = x.replace(i,i.replace(" ","_"))

#Sentence Tokenization (IF CHOOSEN):
if dec == "Sentence" or dec == "sentence":
    print (sent_tokenize(x))

#Word Tokenization (IF CHOOSEN):
elif dec == "Word" or dec == "word":
    print (word_tokenize(x))

#If The User Entered A Wrong Value:
else :
    print ("Please type either (Sentence) or (Word) only")