class Solution:
    def first_uniq_char(self, s: str) -> int:
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1

if __name__ == '__main__':
    st = 'loveleetcode'
    sol = Solution()
    print(sol.first_uniq_char(st))