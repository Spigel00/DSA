class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            label="".join(sorted(word))
            if label not in groups:
                groups[label] = []
            groups[label].append(word)
        return list(groups.values())