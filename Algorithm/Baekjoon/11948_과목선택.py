"""
11948 과목선택
"""

total_score = 0
min_score = 101
for i in range(4):
    score = int(input())
    min_score = min(score, min_score)
    total_score += score
total_score -= min_score

min_score = 101
for i in range(2):
    score = int(input())
    min_score = min(score, min_score)
    total_score += score
total_score -= min_score

print(total_score)
