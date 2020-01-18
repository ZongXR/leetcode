class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        my_dict = {}
        for x in strs:
            if ''.join(sorted(x)) in my_dict.keys():
                my_dict[''.join(sorted(x))].append(x)
            else:
                my_dict[''.join(sorted(x))] = [x]
        return list(my_dict.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))