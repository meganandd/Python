g = {
"A" : {"A" : 0, "B" : 1, "C" : 0, "D" : 1},
"B" : {"A" : 1, "B" : 0, "C" : 1, "D" : 1},
"C" : {"A" : 0, "B" : 1, "C" : 0, "D" : 0},
"D" : {"A" : 1, "B" : 1, "C" : 0, "D" : 1},
}

def dijkstra (graph, start):
    for node, cost in graph[start].items():
        print node, cost
