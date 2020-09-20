class Solution:
    def groupAnagrams(self, strs):
        if all([x==strs[0] for x in strs]):
            return [strs]
        def _is_anagram(str1, str2):
            return sorted(str1)==sorted(str2)
        result = []
        while strs:
            curr_word = strs[0]
            inner_list = []
            inner_list.append(curr_word)
            strs.remove(curr_word)
            for next_word in strs:
                import pdb;pdb.set_trace()
                if not next_word or _is_anagram(curr_word, next_word):
                    inner_list.append(next_word)
                    strs.remove(next_word)
            result.append(inner_list)
        return result

s=Solution()
print (s.groupAnagrams(["ate","eat","tea"]))
