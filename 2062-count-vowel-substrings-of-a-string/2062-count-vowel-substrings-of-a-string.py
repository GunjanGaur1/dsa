class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        vowels = "aeiou"
        count = 0

        for i in range(n):
            seen = set() ## why add here seen
            for j in range(i,n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                print(seen)
                if len(seen)==5:
                    count = count + 1

        return count

