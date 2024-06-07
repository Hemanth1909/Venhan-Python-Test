def find_freq(s):
    freq = {}
    for letter in s:
        if letter in freq:
            freq[letter] += 1 
        else:
            freq[letter] = 1 
        
    for let, fr in freq.items():
        print(f"{let} : {fr}")

find_freq("Hemanth")