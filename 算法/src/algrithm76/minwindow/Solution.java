package algrithm76.minwindow;

class Solution {
    public String minWindow(String s, String t) {
        s = new StringBuilder(s).reverse().toString();
        boolean flag = false;
        String result = s;
        for (int i = 0; i < s.length(); i++) {
            String start = String.valueOf(s.charAt(i));
            if (! t.contains(start))
                continue;
            String temp = t.replaceFirst(start, "");
            for (int j = 0; j < s.substring(i).length(); j++) {
                String end = String.valueOf(s.substring(i).charAt(j));
                if (!t.contains(end))
                    continue;
                String sub = s.substring(i, i + j + 1);
                if (j != 0)
                    temp = temp.replaceFirst(end, "");
                if ("".equals(temp)){
                    flag = true;
                    result = sub.length() < result.length() ? sub : result;
                    break;
                }
            }
        }
        return flag ? new StringBuilder(result).reverse().toString() : "";
    }

    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        s = "a";
        t = "a";
        s = "a";
        t = "aa";
        s = "a";
        t = "b";
        System.out.println(new Solution().minWindow(s, t));
    }
}
