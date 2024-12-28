from input import *
from storage_allocation import *

def main():
    print("-------------- Chemical Storage Allocator --------------")
    chemicals, chemical_names = input_chemical_info()
    adj_mat = create_adjacency_matrix(chemicals) # adjacency matrix for the graph
    
    chemical_amt = len(chemicals)
    chemical_storage = [0 for i in range (chemical_amt)] # stores the storage number for each chemical
    chemical_storage = color_graph(adj_mat, chemicals, chemical_storage, chemical_amt)

    print("\nChemical storage allocation:")
    result, storage_temp = group_chemicals(adj_mat, chemicals, chemical_names, chemical_storage)
    
    print(f"The number of storage units needed is {len(result)}.") 

    for i, color_list in enumerate(result):
        print(f"Storage unit {i+1} ({storage_temp[i]}) contains: {', '.join(color_list)}")
    
    print("\nAllocation completed.")

if __name__ == "__main__":
    main()