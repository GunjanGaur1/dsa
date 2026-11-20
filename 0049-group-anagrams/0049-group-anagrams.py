class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        hash = {}
        for word in strs:
            key = "".join(sorted(word))
            print(key)
            if key not in hash:
                hash[key]=[]
            hash[key].append(word)

        return list(hash.values())

