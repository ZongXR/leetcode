import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        try:
            return True if re.match(p, s).group(0) == s else False
        except:
            return False
