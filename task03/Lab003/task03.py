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
    if limit <= 0:
        return "OFF", None
    
    for n in graph[node]:
        if n not in path:
            status, res_path = dls(n, goal, limit - 1, path + [n])
        if status == "FOUND":
                return "FOUND", res_path
            
    return "OFF", None

for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print(f"Limit {limit} -> Status: {status} | Path: {path}")