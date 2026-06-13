class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mp = {
        'a': 25,
        'b': 24,
        'c': 23,
        'd': 22,
        'e': 21,
        'f': 20,
        'g': 19,
        'h': 18,
        'i': 17,
        'j': 16,
        'k': 15,
        'l': 14,
        'm': 13,
        'n': 12,
        'o': 11,
        'p': 10,
        'q': 9,
        'r': 8,
        's': 7,
        't': 6,
        'u': 5,
        'v': 4,
        'w': 3,
        'x': 2,
        'y': 1,
        'z': 0
    }
        string=""
        for i in range(len(words)): 
            sm=0
            for j in words[i]:
                sm+=weights[ord(j)-97]
            print(sm)
            sm=sm%26
            print(sm)
            for i,v in mp.items():
                if v==sm: 
                    string+=i
        
        return string

        