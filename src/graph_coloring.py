def create_adjacency_matrix(chemicals):
    num_chemicals = len(chemicals)
    matrix = [[0] * num_chemicals for _ in range(num_chemicals)]
    
    for i in range(num_chemicals):
        for j in chemicals[i]["incompatible_with"]:
            matrix[i][j-1] = 1  
            matrix[j-1][i] = 1  
    
    return matrix

def is_color_valid(graph, vertex, color, c, chemicals):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:  
            return False
        if chemicals[vertex]["storage_requirements"]["temperature"] != chemicals[i]["storage_requirements"]["temperature"] and color[i] == c:
            return False
    return True

def graph_coloring(graph, num_colors, chemicals, coloring):
    for vertex in range(len(graph)):
        for c in range(num_colors):
            if is_color_valid(graph, vertex, coloring, c, chemicals):
                coloring[vertex] = c
                break
    return coloring

def graph_color_list(graph, coloring, node_names, chemicals):
    result = [[] for _ in range(max(coloring) + 1)]  
    container_temperatures = [''] * len(result)  
    
    for i in range(len(graph)):
        container_idx = coloring[i]
        result[container_idx].append(node_names[i])
        
        if container_temperatures[container_idx] == '':
            container_temperatures[container_idx] = chemicals[i]["storage_requirements"]["temperature"]
        else:
            if container_temperatures[container_idx] != chemicals[i]["storage_requirements"]["temperature"]:
                new_container_idx = len(result)
                result.append([node_names[i]])
                container_temperatures.append(chemicals[i]["storage_requirements"]["temperature"])
                result[container_idx].remove(node_names[i]) 
    return result, container_temperatures