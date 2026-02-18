class Solution:
    def countAndSay(self, n: int) -> str:
        cas = "1"
        if n == 1:
            return cas
        for _ in range(n - 1):
            cas = self.rle(cas)
            # print(cas)

        return cas
        

    def rle(self, cas: str) -> str:
        start = 0
        curr = ""
        for i in range(len(cas)):
            if (i >= 1 and cas[i - 1] != cas[i]):
                # record the current
                curr += str(i - start)
                curr += cas[start]
                # update the start pointer
                start = i
            else:
                continue
        
        curr += str(i - start + 1)
        curr += cas[start]
            
        return curr
