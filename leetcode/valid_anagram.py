class Solution:
    def isanagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] -= 1

            if d[ch] == 0:
                del d[ch]

        return len(d) == 0

if __name__ == "__main__":
    sol = Solution()
    st = "aab"
    ts = "aba"
    print(sol.isanagram(st, ts))

