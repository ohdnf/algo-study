from collections import defaultdict

def get_multiset(string):
    multiset = defaultdict(int)
    for idx in range(len(string)-1):
        if string[idx:idx+2].isalpha():
            multiset[string[idx:idx+2].lower()] += 1
    return multiset

def solution(str1, str2):
    """
    자카드 유사도를 이용하여 문자열 사이 유사도를 계산
    """
    mulset1, mulset2 = get_multiset(str1), get_multiset(str2)
    key1 = {key for key in mulset1}
    key2 = {key for key in mulset2}
    # 교집합 => 분자
    numerator = [min(mulset1.get(key, float('inf')), mulset2.get(key, float('inf'))) for key in key1 & key2]
    # 합집합 => 분모
    denominator = [max(mulset1.get(key, 0), mulset2.get(key, 0)) for key in key1 | key2]
    
    if not denominator:
        return 65536
    return int(65536 * sum(numerator) / sum(denominator))


# 다른 사람의 풀이
import re
import math

def other_solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if not hap:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return int(gyo_sum/hap_sum*65536)


if __name__ == "__main__":
    print(solution("FRANCE", "french"), 16384)
    print(solution("handshake", "shake hands"), 65536)
    print(solution("aa1+aa2", "AAAA12"), 43690)
    print(solution("E=M*C^2", "e=m*c^2"), 65536)
