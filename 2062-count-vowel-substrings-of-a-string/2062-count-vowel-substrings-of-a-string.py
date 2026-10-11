class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        n = len(word)
        ans = 0
        count = 0
        seen = set()
        for i in range(n):
            seen = set()
            for j in range(i,n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen)==5:
                    count = count + 1

        return count
