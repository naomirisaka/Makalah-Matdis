# Chemical Storage Optimization Utilizing the Welch-Powell Algorithm
> Makalah IF1220 Matematika Diskrit
## Project Overview
This project uses the Welch-Powell graph coloring algorithm for optimizing chemical storage. The chemicals and their relationships are represented as a graph, with chemicals as vertices and incompatibilities as edges. The developed program processes the graph in adjacency matrix form, where adjacency indicates incompatibility between chemicals. The program allocates different storage units, represented colors in graph coloring theory, ensuring only chemicals that are compatible and have the same storage temperature are placed in the same unit. 
## Project Structure
The project is structured as below:
```
├── .gitignore
├── README.md
└── src/
    ├── input.py
    ├── main.py
    └── storage_allocation.py
```

## How to Use
1. Clone the repository: 
   ```sh
   git clone https://github.com/naomirisaka/Makalah-Matdis.git

2. Open the cloned local repository in an IDE that supports Python.

3. Run the program:
   ```sh
   cd src
   python main.py
