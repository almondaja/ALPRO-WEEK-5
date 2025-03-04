import networkx as nx
import matplotlib.pyplot as plt

# Membuat graf
G = nx.Graph()

# Menambahkan edge sesuai dengan gambar
edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'E'), ('B', 'F'), ('C', 'E'), ('C', 'F'), ('D', 'F'),
    ('E', 'G'), ('E', 'H'), ('F', 'I'), ('F', 'J'),
    ('G', 'H'), ('H', 'K'), ('I', 'J'), ('J', 'K')
]
G.add_edges_from(edges)

# Fungsi untuk menampilkan graf
def draw_graph(G):
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G)  # Posisi node
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    plt.show()

# 1. Semua Path dari A ke K
all_paths_A_K = list(nx.all_simple_paths(G, source='A', target='K'))

# 2. Semua Path dari G ke J
all_paths_G_J = list(nx.all_simple_paths(G, source='G', target='J'))

# 3. Semua Path dari E ke F
all_paths_E_F = list(nx.all_simple_paths(G, source='E', target='F'))

# 4. Semua Cycle jika A adalah titik awal
cycles_with_A = [cycle for cycle in nx.cycle_basis(G) if 'A' in cycle]

# 5. Semua Cycle jika K adalah titik awal
cycles_with_K = [cycle for cycle in nx.cycle_basis(G) if 'K' in cycle]

# 6. Circuit terpendek dan terpanjang dari A ke K
shortest_path_A_K = nx.shortest_path(G, source='A', target='K')
longest_path_A_K = max(nx.all_simple_paths(G, source='A', target='K'), key=len)

# 7. Circuit terpendek dan terpanjang dari G ke J
shortest_path_G_J = nx.shortest_path(G, source='G', target='J')
longest_path_G_J = max(nx.all_simple_paths(G, source='G', target='J'), key=len)

# 8. Circuit terpendek dan terpanjang dari E ke F
shortest_path_E_F = nx.shortest_path(G, source='E', target='F')
longest_path_E_F = max(nx.all_simple_paths(G, source='E', target='F'), key=len)

# Menampilkan hasil
print("Semua Path dari A ke K:", all_paths_A_K)
print("\nSemua Path dari G ke J:", all_paths_G_J)
print("\nSemua Path dari E ke F:", all_paths_E_F)
print("\nSemua Cycle yang melalui A:", cycles_with_A)
print("\nSemua Cycle yang melalui K:", cycles_with_K)
print("\nCircuit Terpendek dari A ke K:", shortest_path_A_K)
print("\nCircuit Terpanjang dari A ke K:", longest_path_A_K)
print("\nCircuit Terpendek dari G ke J:", shortest_path_G_J)
print("\nCircuit Terpanjang dari G ke J:", longest_path_G_J)
print("\nCircuit Terpendek dari E ke F:", shortest_path_E_F)
print("\nCircuit Terpanjang dari E ke F:", longest_path_E_F)

# Tampilkan visualisasi graf
draw_graph(G)
