class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using a hashmap 
        res = defaultdict(list) #create the result dictionary as a list
        for s in strs:
            count = [0] * 26 #creating the key for strings that contain chars
            for c in s: #access each char in s using c
                count[ord(c) - ord("a")] += 1 #using the current char we will subtract from the asci value from both and record it in our key library count
            res[tuple(count)].append(s) #once we finish counting the chars of the current string s we will append the string value into our dictionary  

        return res.values() 