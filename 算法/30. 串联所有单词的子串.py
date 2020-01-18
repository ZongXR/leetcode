from itertools import permutations
from re import finditer


class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if len(words) == 0:
            return []
        elif len(set(words)) == 1:
            words_str = "".join(words)
            if len(words_str) <= len(s):
                return [m.start() for m in finditer(r"(?=%s)" % words_str, s)]
            else:
                return []
        result = []
        stack = []
        length = len(words[0])
        i = 0
        while True:
            words_copy = words.copy()
            string = s[i:i+length]
            if len(string) != length:
                break
            if string in words_copy:
                words_copy.remove(string)
                stack.append(i+1)
                i = i + length
                flag = True
                while len(words_copy) > 0:
                    string = s[i:i+length]
                    if len(string) != length:
                        flag = False
                        break
                    if string in words_copy:
                        words_copy.remove(string)
                        i = i + length
                    else:
                        flag = False
                        break
                if flag:
                    result.append(i - length * len(words))
                i = stack.pop()
            else:
                i = i + 1
        return result

    def find_substring(self, s: str, words: [str]) -> [int]:
        if len(words) == 0:
            return []
        temp = permutations(words, len(words))
        all_words = ["".join(x) for x in temp]
        result = [m.start() for x in all_words for m in finditer(r"(?=%s)" % x, s)]
        return list(set(result))


if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print(Solution().findSubstring("foobarfoobar", ["foo", "bar"]))
    print(Solution().findSubstring("aaa", ["a", "a"]))
    print(Solution().findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel", ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]))
    print(Solution().findSubstring("a", ["a"]))
    print(Solution().findSubstring("aaaaaaaa", ["aa", "aa", "aa"]))
    print(Solution().findSubstring("abababab", ["ab", "ab", "ab"]))

