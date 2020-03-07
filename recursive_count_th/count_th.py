'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    occurence = "th"
    if len(word) < len(occurence):
        return 0
    elif word[0: len(occurence)] == occurence:
       return  count_th(word[len(occurence):]) + 1
    else:
        return count_th(word[len(occurence) - 1:])
        
    
