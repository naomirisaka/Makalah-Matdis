def create_adjacency_matrix(chemicals):  # adjacency matrix for the graph
    num_chemicals = len(chemicals)
    matrix = [[0] * num_chemicals for _ in range(num_chemicals)]
    
    for i in range(num_chemicals):
        for j in chemicals[i]["incompatible_with"]:
            matrix[i][j-1] = 1  # incompatible
            matrix[j-1][i] = 1  # incompatible
    
    return matrix

def sort_vertices_degree(graph):  # sorts vertices by degree in descending order
    degrees = [sum(row) for row in graph]
    sorted_vertices = sorted(range(len(graph)), key=lambda x: degrees[x], reverse=True)
    return sorted_vertices

def check_vertex(graph, vertex, vertices, color_list, curr_color):  # checks if a vertex can be colored with the current color
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color_list[i] == curr_color:  # checks adjacency
            return False
        if vertices[vertex]["temperature"] != vertices[i]["temperature"] and color_list[i] == curr_color:  # checks temperature
            return False
    return True

def color_graph(graph, vertices, color_list, color_amt):  # assigns colors to the vertices
    sorted_vertices = sort_vertices_degree(graph)
    
    for vertex in sorted_vertices:
        for curr_color in range(color_amt):
            if check_vertex(graph, vertex, vertices, color_list, curr_color):
                color_list[vertex] = curr_color
                break

    return color_list

def group_chemicals(adj_mat, chemicals, chemical_names, chemical_storage):  # groups the chemicals by storage unit
    result = [[] for _ in range(max(chemical_storage) + 1)]  
    storage_temp = ['' for _ in range(len(result))]

    # split based on temperatures
    for i in range(len(adj_mat)):
        idx = chemical_storage[i]
        result[idx].append(chemical_names[i])
        
        if storage_temp[idx] == '':
            storage_temp[idx] = chemicals[i]["temperature"]
        else:
            if storage_temp[idx] != chemicals[i]["temperature"]:
                result.append([chemical_names[i]])
                storage_temp.append(chemicals[i]["temperature"])
                result[idx].remove(chemical_names[i])

    # split based on incompatiblity
    final_result = []
    final_storage_temp = []
    
    for i in range(len(result)):
        if result[i]:
            temp = storage_temp[i]
            found = False
            for j in range(len(final_result)):
                if final_storage_temp[j] == temp:
                    can_merge = True
                    for chem in result[i]:
                        for existing_chem in final_result[j]:
                            idx1 = chemical_names.index(chem)
                            idx2 = chemical_names.index(existing_chem)
                            if adj_mat[idx1][idx2] == 1: 
                                can_merge = False
                                break
                        if not can_merge:
                            break
                    if can_merge:
                        final_result[j].extend(result[i])
                        found = True
                        break
            if not found:
                final_result.append(result[i])
                final_storage_temp.append(temp)

    return final_result, final_storage_temp