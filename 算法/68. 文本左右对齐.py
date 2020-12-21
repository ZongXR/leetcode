"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/text-justification
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        """
        左右对齐\n
        :param words: 单词列表
        :param maxWidth: 每行最大长度
        :return: 对其后的文本列表
        """
        results = []
        result = ""
        while len(words) > 0:
            word = words.pop(0)
            result, new_len = self.get_str(result, word)
            if len(result) > maxWidth:
                results.append(result[:-new_len])
                words.insert(0, word)
                result = ""
                continue
        results.append(result)
        for i, result in enumerate(results):
            if len(result.strip().split(" ")) == 1 or i == len(results) - 1:
                # 如果只有一个单词 或 最后一行应为左对齐
                results[i] = self.left_justify(result, maxWidth)
                continue
            results[i] = self.left_right_justify(result, maxWidth)
        return results

    def left_right_justify(self, words: str, max_length: int) -> str:
        """
        左右对齐\n
        :param words: 字符串
        :param max_length: 字符串长度
        :return: 左右对齐后的字符串
        """
        words = words.strip()
        word = words.split(" ")
        insert_space_num = max_length - len("".join(word))
        space_num = insert_space_num // len(word[:-1])
        last_space = insert_space_num % len(word[:-1])
        end_word = word[-1]
        word = list(map(lambda x: x + " " * space_num, word[:-1]))
        for i, wor in enumerate(word[:-1]):
            if last_space == 0:
                break
            word[i] = wor + " "
            last_space = last_space - 1
        return "".join(word) + end_word

    def left_justify(self, text: str, max_length: int) -> str:
        """
        左对齐\n
        :param text: 文本
        :param max_length: 最大长度
        :return: 左对齐的文本
        """
        space_num = max_length - len(text.strip())
        return text.strip() + " " * space_num

    def get_str(self, text: str, word: str) -> (str, int):
        """
        获得字符串\n
        :param text: 原始的字符串
        :param word: 新加入的单词
        :return: 加入后的字符串, 新加的长度
        """
        if text == "":
            return word, len(word)
        else:
            return text + " " + word, len(word) + 1


if __name__ == '__main__':
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
    # print(Solution().insert_space("acknowledgment ", 16))

