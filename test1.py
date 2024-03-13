"""
def solution(S):
    indices = []
    for word in S:
        #my_list.index(item, start, end)
        indices.append(word.index('b'))

    return indices 

print(solution(['abc', 'bca', 'dbe']))


def solution(S):
    indices = []
    for word in range(len(S)):
        #my_list.index(item, start, end)
        if S[word] == "abc":
            indices.append(word)

    return indices 

print(solution(['abc', 'bca', 'dbe']))


def solution(S):
    result = []
    for word in S:
        for index, letter in enumerate(word):
            result.append((index, letter))
    return result

print(solution(['abc', 'bca', 'dbe']))



def solution(S):
    for word in S:
        for letter in word:
            print(letter)

solution(['abc', 'bca', 'dbe'])
"""

def solution(S):
    # Dictionary whose key= letter and value = [(index of word, index of letter)]
    letter_positions = {}  
    

    for index_word, word in enumerate(S):
        for index_letter, letter in enumerate(word):
            if letter not in letter_positions:
                letter_positions[letter] = [(index_word, index_letter)]
            else:
                letter_positions[letter].append((index_word, index_letter))

    #print(letter_positions)
    # {'a': [(0, 0), (1, 2)], 
    #  'b': [(0, 1), (1, 0), (2, 1)], 
    #  'c': [(0, 2), (1, 1)],
    #  'd': [(2, 0)], 
    #  'e': [(2, 2)]}

    # Go through the list of tuples. If any index[1] of any 2 tuples for a particular letter are similar, 
    # return index[0] of the first tuple, index[0] of the second tuple and index[1] of either of the tuples
                
    for position in letter_positions.values():
        for i in range(len(position)):
            for j in range(i+1, len(position)):
                if position[i][1] == position[j][1]:
                    return [position[i][0], position[j][0], position[i][1]]
             
    return []
            

    

# Test cases
print(solution(['abc', 'bca', 'dbe']))  # Output: [0, 2, 1]
print(solution(['zzzz', 'ferz', 'zdsr', 'fgtd']))  # Output: [0, 1, 3]/ [0, 2, 0] or [1, 3, 0]
print(solution(['gr', 'sd', 'rg']))  # Output: []
print(solution(['bdafg', 'ceagi']))  # Output: [0, 1, 2]