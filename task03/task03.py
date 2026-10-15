
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    depth = len(path) - 1
    if depth == limit:
        for child in graph[node]:
            if child not in path:
                return "CUTOFF", None
        return "FAILURE", None
    cutoff_occurred = False
    for child in graph[node]:
        if child in path:
            continue
        status, result = dls(
            child, goal, limit, path + [child]
        )
        if status == "FOUND":
            return status, result
        if status == "CUTOFF":
            cutoff_occurred = True
    if cutoff_occurred:
        return "CUTOFF", None
    return "FAILURE", None


def iddfs(start, goal, max_depth):
    attempts = []

    for limit in range(max_depth + 1):
        status, path = dls(
            start, goal, limit, [start]
        )
        attempts.append((limit, status))

        if status == "FOUND":
            return status, path, attempts

        if status == "FAILURE":
            return status, None, attempts

    return "CUTOFF", None, attempts

print("DLS RESULTS")
for limit in range(1, 5):
    status, path = dls("A", "G", limit, ["A"])
    print(limit, status, path)

print("\nIDDFS RESULTS")
for maximum in range(1, 5):
    status, path, attempts = iddfs("A", "G", maximum)
    print("Maximum:", maximum)
    print("Attempts:", attempts)
    print("Status:", status)
    print("Path:", path)
