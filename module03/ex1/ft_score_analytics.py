import sys

def calculation(scores :[]):
    print("Total players:", len(scores))
    print("Total score:",sum(scores))
    print("Average score:",sum(scores)/len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:",max(scores) - min(scores))

print("=== Player Score Analytics ===")
length = len(sys.argv)
scores = []
if length == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1>" 
    "<score2> ..")
else:
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError :
            print(f"Invalid score : {arg}")
    print("Scores processed",scores)
    calculation(scores)
