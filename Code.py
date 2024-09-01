class Solution:
    def defangIPaddr(self, address: str) -> str:
        t = address.replace(".","[.]")
        return t
