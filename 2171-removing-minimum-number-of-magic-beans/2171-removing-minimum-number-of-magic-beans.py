class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        beans.sort()
        total = sum(beans)
        print(total)
        n = len(beans)
        ans = float(inf)
        for i in range(n):
            current = beans[i]
            print("current",current)
            # 1 4 5 6 
            # curr = 1 * (4-0)
            kept = total - current * (n-i)
            ##print(kept)
            ans = min(ans,kept)
            ##print("ans",ans)

        return ans

