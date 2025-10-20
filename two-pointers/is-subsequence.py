class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        else:
            new_t = ''
            s_pointer = 0
            t_pointer = 0
            while s_pointer < len(s) and t_pointer < len(t):
                if s[s_pointer] == t[t_pointer]:
                    new_t += s[s_pointer]
                    s_pointer += 1
                    t_pointer += 1
                else:
                    t_pointer += 1
            if new_t == s:
                return True
            return False

        