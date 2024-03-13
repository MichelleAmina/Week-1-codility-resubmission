"""
You are given an array S consisting of N strings. Every string is of the same length M. 
Your task is to find a pair of strings in array S, such that there exsts a position in which
both of these strings have the same letter. Both the index in array S and the positions in the strings 
are numbered from zero. 

For example, given S = ['abc', 'bca', 'dbe'] string 0('abc') and string 2 ('dbe') have the same letter 'b'
in position 1. On the other hand, for strings 'abc' and 'bca' there does not exist a position in which they 
have the same letter.

Write a function 
    def solution(S)

that given a zero-indexed array S of N strings, returns an array describing a pair of strings from S which 
share a common letter at the same index. If there is not such pair, the function should return an empty array.
If there is more than one correct answer, the function can return any of them.

The result should be represented as an array containing three integers. The first two integers are the indexes 
in S of the strings belonging to the pair. The third integer is the position of the common letter.

For S = ['abc', 'bca', 'dbe'], as above, the result array should be represented as [0, 2, 1]. Another correct answer 
is [2, 0, 1] as the order of the indexes of strings doesn't matter

Tests
1. Given S = ['zzzz', 'ferz', 'zdsr', 'fgtd'], your function may return [0, 1, 3]. Both 'zzz' and 'ferz' have 'z' 
in position 3. The function may also return [1, 3, 0] which would reflect strings 'ferz', 'fgtd' and letter 'f'
2. Given S= ['gr', 'sd', 'rg'] your function should return []. There is no pair of strings that fulfils the criteria 
3. Given S = ['bdafg', 'ceagi'], your function may return [0,1,2]

Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..30,000]
M is an integer within the range [1..2,000]
Each element of S consists only of lowercase English letters (a-z)
N * M <= 30,000 

"""


"""
BDD 
1. Given : Array S of strings of same length S =['abc', 'bca', 'dbe']
2. When : A letter exists in the same index in a pair of strings
3. Then: return an array [x, y, z] where x and y = indexes in S of the strings belonging to the pair, z = index of the common letter

"""


def solution(S):
    # Dictionary whose key= letter and value = [(index of word, index of letter)]
    letter_positions = {}

    # enumerate adds a counter to an iterable and returns it as an enumerate object (iterator with index and the value).
    for word_index, word in enumerate(S):
        for letter_index, letter in enumerate(word):
            # if the letter is not found in the dictionary 
            if letter not in letter_positions:
                # initialize it 
                letter_positions[letter] = set()
            # else, add the new word_index and letter_index 
            letter_positions[letter].add((word_index, letter_index))

    #print(letter_positions)

    # to iterate through the values, use the .values()
    for position in letter_positions.values():
        # look at the first tuple 
        for pos1 in position:
            # look at the second tuple 
            for pos2 in position:
                # if the first tuple does not equals the second tuple
                # and index[1] or each tuple ie letter_index are equal 
                if pos1 != pos2 and pos1[1] == pos2[1]:
                    # return index 0 of the first and second tuple (word_index) as well as the letter_index
                    return [pos1[0], pos2[0], pos1[1]]
    # else return an empty list if no string pairs are found 
    return []

print(solution(['abc', 'bca', 'dbe']))  # Output: [0, 2, 1]
print(solution(['zzzz', 'ferz', 'zdsr', 'fgtd']))  # Output: [0, 1, 3]/ [0, 2, 0] or [1, 3, 0]
print(solution(['gr', 'sd', 'rg']))  # Output: []
print(solution(['bdafg', 'ceagi']))  # Output: [0, 1, 2]
