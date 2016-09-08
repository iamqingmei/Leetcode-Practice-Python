"""
 Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine): #146 ms
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mlist = list(magazine)
        for i in list(ransomNote):
            if i in mlist:
                mlist.remove(i)
            else:
                return False
        return True
            