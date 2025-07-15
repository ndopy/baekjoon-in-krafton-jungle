import sys

word_count = int(input())
words = list(sys.stdin.read().split())

# 중복 제거
unique_words = list(set(words))

# 정렬
sorted_words = sorted(unique_words, key=lambda word: (len(word), word))

for word in sorted_words:
    print(word)