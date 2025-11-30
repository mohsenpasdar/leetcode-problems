from collections import Counter

words = ["aabb", "baba", "abab", "abbc", "bcab", "ab"]

groups = {}
for word in words:
    key = frozenset(Counter(word).items())
    groups.setdefault(key, []).append(word)

for group in groups.values():
    print(group)