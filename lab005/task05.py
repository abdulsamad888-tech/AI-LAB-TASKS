import math

ab_leaves = 0

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global ab_leaves
    if depth == target:
        ab_leaves += 1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta)
            value = max(value, val)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta)
            value = min(value, val)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))

print("Alpha-Beta:", alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))
print("Leaves:", ab_leaves)