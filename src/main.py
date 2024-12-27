from input import *
from graph_coloring import *

def main():
    chemicals, chemical_names = get_input_data()
    
    adjacency_matrix = create_adjacency_matrix(chemicals)
    num_colors = len(chemicals)
    coloring = [-1] * len(chemicals)
    
    coloring = graph_coloring(adjacency_matrix, num_colors, chemicals, coloring)
    
    print("\nChemical storage allocation considering incompatibilities and temperature requirements:")
    result, container_temperatures = graph_color_list(adjacency_matrix, coloring, chemical_names, chemicals)
    
    for i, color_list in enumerate(result):
        print(f"Container {i+1} contains: {', '.join(color_list)}")
        print(f"Container {i+1} temperature: {container_temperatures[i]}")

if __name__ == "__main__":
    main()