from collections import deque

"""
given two words (begin_word and end_word), and a dictionary's word list,
retuirn the shortest transformation sequence from begin_word to end_word, such that:

only one letter can be changed at a time.
each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Note:

return [] if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.


Sample:
beginWord = "hit",
endWord = "cog"
wordList = ["hot", "dot", "dog","lot","log","cog"]
["hit", "hot", "dot", "dog", "cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot","dog","lot","log"]
[]

Plan
1. Translate into graph terminology
vertices = wordList
edges = wordList
weight

2. Build your graph if needed
create all possible transformations in an adjacency list would be too much
we can come up with how to find out the next vertex by determining if it's even a valid vertex to visit
we should visit a vertex if that vertex is in the wordlist

3. Traverse Graph
since we want the shortest path, we want to use BFS
start from beginWord and generate word transformations from it
enqueue transformations that are in wordlist, ignore the rest
once we find endWord, return the path it took to get to that node
"""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def findLAdders(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    queue = deque()
    queue.append([beginWord])

    while len(queue) > 0:
        currPath = queue.popleft()
        currWord = currPath[-1]
        if currWord in visited:
            continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i + 1:]
                if transformedWord in words:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
    return []

print(findLAdders("hit", "cog", ["hot", "dot", "dog","lot","log","cog"] ))
# beginWord = "hit",
# endWord = "cog"
# wordList = ["hot", "dot", "dog","lot","log","cog"]
# ["hit", "hot", "dot", "dog", "cog"]

print(findLAdders("hit", "cog", ["hot", "dot", "dog","lot","log"] ))
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot","dog","lot","log"]
# []