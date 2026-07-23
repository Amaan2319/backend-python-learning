def reverse_words_manual(sentence: str) -> str:
    result = ""
    i = len(sentence) - 1
    
    while i >= 0:
        # Step 1: Skip any trailing or multiple spaces
        while i >= 0 and sentence[i] == ' ':
            i -= 1
            
        if i < 0: 
            break
            
        # Step 2: Mark the end of the word
        word_end = i
        
        # Step 3: Move left to find the start of the word
        while i >= 0 and sentence[i] != ' ':
            i -= 1
            
        # Step 4: Manually extract the word from (i+1) to word_end
        # Add a space before appending the next word, if result isn't empty
        if result != "":
            result += " "
            
        for k in range(i + 1, word_end + 1):
            result += sentence[k]
            
    return result

sentence = "Chalo jantar mantar"
i = len(sentence) - 1
result_list = []

# Loop from the end of the string down to index 0
while i >= 0:
    # 1. Skip any trailing spaces
    while i >= 0 and sentence[i] == " ":
        i -= 1
        
    if i < 0:
        break
        
    # 2. Mark the end index of the current word
    word_end = i + 1
    
    # 3. Find the start index of the current word by looking for the next space
    while i >= 0 and sentence[i] != " ":
        i -= 1
        
    word_start = i + 1
    
    # 4. Extract the word using valid forward slicing and save it
    current_word = sentence[word_start:word_end]
    result_list.append(current_word)

# Join the extracted words back with spaces
result_sentence = " ".join(result_list)

print(result_sentence)
# Output: mantar jantar Chalo
