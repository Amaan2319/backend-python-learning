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

# easy method
def reverse_words_(s):
    # result = ""
    words = s.split()
    reversed_ = words[::-1]
    reversed_sentence = " ".join(reversed_)
    print(reversed_sentence)
    return reversed_sentence

print(reverse_words_("Amaan is cool "))

sentence = "Chalo jantar mantar"
reversed_sentence = sentence[::-1]
i = len(sentence)-1
result_list=[]
while i >0:
    if i >0 and sentence[i]!=" ":
        reversed_Word=sentence[-1:i]
        print(reversed_Word)
    if sentence[i]==" ":
        i-=1
    i-=1
    result_list.append(reversed_Word)

result_sentence = " ".join(result_list)