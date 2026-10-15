import math
mm_leaves = 0
ab_leaves = 0

def minimax(depth, index, max_turn, scores, target):
    global mm_leaves
    if depth == target:
        mm_leaves += 1
        return scores[index]
    
    if max_turn:
        return max(
            minimax(depth + 1, index * 2, False, scores, target),
            minimax(depth + 1, index * 2 + 1, False, scores, target)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, scores, target),
            minimax(depth + 1, index * 2 + 1, True, scores, target)
        )

def alphabeta(depth, index, max_turn, scores, target, alpha, beta):
    global ab_leaves
    if depth == target:
        ab_leaves += 1
        return scores[index]
    if max_turn:
        val = float('-inf')
        for i in range(2):
            val = max(val, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta))
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return val
    else:
        val = float('inf')
        for i in range(2):
            val = min(val, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta))
            beta = min(beta, val)
            if alpha >= beta:
                break
        return val
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))

print("Minimax Value:", minimax(0, 0, True, scores, depth))
print("Minimax Leaves Evaluated:", mm_leaves)

print("Alpha-Beta Value:", alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))
print("Alpha-Beta Leaves Evaluated:", ab_leaves)