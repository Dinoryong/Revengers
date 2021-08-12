'''
파이썬 아니면 개극혐일듯!
'''
from collections import defaultdict
import re
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    dic3 = defaultdict(int)
    dic4 = defaultdict(lambda: 0x3f3f3f3f)
    regex = re.compile('[a-z]{2}')
    for s in [str1[i:i+2] for i in range(len(str1)-1)]:
        res = re.match(regex, s)
        if res:
            dic1[s]+=1
    
    for s in [str2[i:i+2] for i in range(len(str2)-1)]:
        res = re.match(regex, s)
        if res:
            dic2[s]+=1
            
    for k in dic1.keys() | dic2.keys():
        dic3[k] = max(dic1[k], dic2[k])
        dic4[k] = min(dic2[k], dic1[k])
    sum1,sum2  = 0,0
    
    for k in set(dic1.keys()) | set(dic2.keys()):
        sum1 += dic3[k]
        sum2 += dic4[k]
    return(65536*sum2//sum1 if sum1 != 0 else 65536) 
