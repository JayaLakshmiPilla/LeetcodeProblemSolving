class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_a = defaultdict(list)
        for s in strs :
            key = "".join(sorted(s)) 
            dict_a[key].append(s) 
        return  list(dict_a.values())




        