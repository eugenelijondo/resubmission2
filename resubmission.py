def solution(S):
    if not S:  
        return []  #Return an empty list if the input list is empty
    
    letter_positions = {}  # place for storing the place of  letters in strings
    for idx, string in enumerate(S):
        for pos, letter in enumerate(string):
            if letter in letter_positions:
                # Found a pair of strings with a common letter
                return [letter_positions[letter], idx, pos]  # Return the positions of the common letter
            else:
                letter_positions[letter] = idx  # Update the dictionary with the position of the letter
    return []  # Return an empty list if no common letter is found

# Tests
print(solution(["abc", "bca", "dbe"])) 
print(solution(["ferz", "fgtd"])) 
print(solution(["g r", "sd", "rg"])) 
print(solution(["bdafg", "ceagi"]))
