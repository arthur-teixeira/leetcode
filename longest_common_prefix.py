from typing import List


# Naive


def longest_common_prefix(strs: List[str]):
    prefix = ""

    strs.sort(key=len)
    for i in range(len(strs[0])):
        for s in range(len(strs) - 1):
            if strs[s][i] != strs[s + 1][i]:
                return prefix
        prefix += strs[0][i]
    return prefix


# Faster, only compares two string, sorted alphabetically with min max

def lcp_minmax(strs: List[str]):
    if not strs:
        return ''

    s1 = min(strs)
    s2 = max(strs)

    for i, char in enumerate(s1):
        if char != s2[i]:
            return s1[:i]
    return s1


lcp_minmax(['leet', 'leetcode', 'leets', 'leeta', 'leetuce', 'leeb', 'leez'])
