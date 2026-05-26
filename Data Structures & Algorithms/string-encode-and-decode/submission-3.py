class Solution:
    def encode(self, strs: List[str]) -> str:
        # O(N)?
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # index of next '#'
            j = s.find('#', i)
            length = int(s[i:j])
            
            # extract based on length
            i = j + 1
            j = i + length
            res.append(s[i:j])
            
            i = j
        return res
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i=j
        return res
