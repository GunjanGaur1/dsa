class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        vowels = "aeiou"
        count = 0
        for i in range(n):
            seen = set()
            for j in range(i,n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                print(seen)
                if len(seen)==5:
                    print("at i:=",i)
                    print("at j:=",j)
                    print(seen)
                    count = count + 1
                    print("count:=",count)
        return count 
