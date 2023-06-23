#perform sentinment analysis on text (good for exposition text)
#remove intext (good for academics)
#text to speech (open AI API)
#referencing using Adelaide Uni's standard (from input, you get the output)
#can make UI for this 


#function which removes the intext referencing from the given text 
#if there is a year in the intext, then the brackets will be removed 
def remove_intext(cur_text): 
    for index, letter in enumerate(cur_text):
        if letter == '(':
            #get end of index 
            #make substring 
            #remove from cur_text 
            cur_index = index
            
            cur_text = cur_text[cur_index:]

def word_count(cur_text):  
    words = 0  
    for letter in cur_text:
        if 
        words = words + 1
    return words
    
        

def main():
        main_text = print('Enter your text:')
        old_wordcount = word_count(main_text)
        print(old_wordcount)


        
    