import networkx as nx
import matplotlib.pyplot as plt

# Membuat graf
G = nx.Graph()

# Menambahkan edge sesuai dengan gambar
edges = [
    ('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E'),
    ('C', 'E'), ('C', 'F'), ('D', 'E'), ('E', 'F')
]
G.add_edges_from(edges)

# Fungsi untuk menampilkan graf
def draw_graph(G):
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)  # Posisi node
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    plt.show()

# 1. Semua Path dari A ke C
all_paths_A_C = list(nx.all_simple_paths(G, source='A', target='C'))

# 2. Semua Cycle jika C adalah titik awal
cycles_with_C = [cycle for cycle in nx.cycle_basis(G) if 'C' in cycle]

# 3. Semua Cycle jika B adalah titik awal
cycles_with_B = [cycle for cycle in nx.cycle_basis(G) if 'B' in cycle]

# 4. Circuit terpendek dan terpanjang dari A ke A (Hamiltonian Circuit)
shortest_circuit = None
longest_circuit = None

try:
    # Mencari sirkuit terpendek menggunakan algoritma TSP
    shortest_circuit = nx.approximation.traveling_salesman_problem(G, cycle=True)
except:
    pass

# Menampilkan hasil
print("Semua Path dari A ke C:", all_paths_A_C)
print("\nSemua Cycle yang melalui C:", cycles_with_C)
print("\nSemua Cycle yang melalui B:", cycles_with_B)
print("\nCircuit Terpendek dari A ke A:", shortest_circuit)

# Tampilkan visualisasi graf
draw_graph(G)
