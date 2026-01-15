import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import networkx as nx

# Path ke file font Montserrat
font_path = "/home/amir/Downloads/Montserrat/static/Montserrat-Regular.ttf"  

# Load font
montserrat = fm.FontProperties(fname=font_path)

# Tema utama
main_theme = "Community Resilience"

# Sub-domain dan kode
domains = {
    "Collective Preparedness & Coping Strategies": [
        "Community-Based Evacuation Tools",
        "Construction of Second Floors",
        "Experiences in Coping with Floods"
    ],
    "Social Capital & Community Networks": [
        "Community Solidarity",
        "Youth Involvement",
        "Neighborhood WhatsApp Groups",
        "Role of RT/RW Officials"
    ],
    "Risk Communication & Early Response": [
        "Responsiveness to Early Signs",
        "Manual Information Dissemination",
        "Neighborhood WhatsApp Groups"
    ],
    "External–Internal Resource Integration": [
        "External Assistance",
        "Evacuation Prioritization"
    ]
}

# Warna untuk tiap domain
domain_colors = {
    "Collective Preparedness & Coping Strategies": "lightblue",
    "Social Capital & Community Networks": "lightgreen",
    "Risk Communication & Early Response": "orange",
    "External–Internal Resource Integration": "violet"
}

# Buat nodes
nodes = [main_theme]
for domain, codes in domains.items():
    nodes.append(domain)
    nodes.extend(codes)

# Index mapping
node_indices = {name: i for i, name in enumerate(nodes)}

# Buat edges
edges = []
for domain, codes in domains.items():
    edges.append((main_theme, domain))
    for code in codes:
        edges.append((domain, code))

# Cross-relations
cross_relations = [
    ("Community Solidarity", "Community-Based Evacuation Tools"),
    ("Community Solidarity", "Responsiveness to Early Signs"),
    ("Youth Involvement", "Manual Information Dissemination"),
    ("Neighborhood WhatsApp Groups", "Evacuation Prioritization"),
    ("Role of RT/RW Officials", "External Assistance")
]
edges.extend(cross_relations)

# Graph
G = nx.Graph()
G.add_edges_from(edges)

# Layout
pos = nx.spring_layout(G, seed=42, k=0.6)

# Node colors
node_color = []
for node in G.nodes():
    if node == main_theme:
        node_color.append("red")
    elif node in domains.keys():
        node_color.append(domain_colors[node])
    else:
        for domain, codes in domains.items():
            if node in codes:
                node_color.append(domain_colors[domain])
                break
        else:
            node_color.append("lightgrey")

# Setting ukuran Full HD
plt.figure(figsize=(19.2, 10.8))  # 1920x1080 px, skala 100 dpi -> dpi bisa diatur lebih tinggi

# Draw edges
nx.draw_networkx_edges(G, pos, alpha=0.8, width=2, edge_color="#444444")

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=700, edgecolors='black')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='bottom')

# Hilangkan axis
plt.axis('off')
plt.title("Thematic Network: Community Resilience", fontsize=20)

# Simpen potonya
plt.tight_layout()
plt.savefig("thematic_network_matplotlib.png", dpi=600)
plt.show()
