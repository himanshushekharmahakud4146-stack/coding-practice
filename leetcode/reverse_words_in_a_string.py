class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        reverse_words = words[::-1]
        return ' '.join(reverse_words)

if __name__ == '__main__':
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))