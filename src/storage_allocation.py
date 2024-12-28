def create_adjacency_matrix(chemicals):  # adjacency matrix for the graph
    num_chemicals = len(chemicals)
    mat = [[0] * num_chemicals for _ in range(num_chemicals)]
    
    for i in range(num_chemicals):
        for j in chemicals[i]["incompatible_with"]:
            mat[i][j-1] = 1  # incompatible
            mat[j-1][i] = 1  # incompatible
    
    return mat

def sort_chemicals_degree(adj_mat):  # sorts vertices by degree in descending order
    degrees = [sum(row) for row in adj_mat]
    sorted_chemicals = sorted(range(len(adj_mat)), key=lambda x: degrees[x], reverse=True)
    return sorted_chemicals

def check_chemical(adj_mat, chemical, chemicals, chemical_storage, curr_unit):  # checks if a vertex can be colored with the current color
    for i in range(len(adj_mat)):
        if (adj_mat[chemical][i] == 1) and (chemical_storage[i] == curr_unit):  # checks adjacency
            return False
        
        if (chemicals[chemical]["temperature"] != chemicals[i]["temperature"]) and (chemical_storage[i] == curr_unit):  # checks temperature
            return False
        
    return True

def assign_storage(adj_mat, chemicals, chemical_storage, chemical_amt):  # assigns colors to the vertices
    sorted_chemicals = sort_chemicals_degree(adj_mat)
    
    for chemical in sorted_chemicals:
        for curr_unit in range(chemical_amt):
            if check_chemical(adj_mat, chemical, chemicals, chemical_storage, curr_unit):
                chemical_storage[chemical] = curr_unit
                break

    return chemical_storage

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