import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values
    pass


# Example #    
word_list = file_to_list("C:\\Users\\spsar\\Downloads\\Terminal-Wordle-main\\Terminal-Wordle-main\\sgb-words.txt") 
#print(word_list)
word_list = [element.upper() for element in word_list] 
