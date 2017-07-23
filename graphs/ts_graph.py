import graph as gh


def build_graph(edges_file_path, size):
    # 构建一个空的无向图
    graph = gh.Graph()
    for i in range(size):
        # 添加节点
        graph.add_node(i)

    # 读取边的信息并添加边
    with open(edges_file_path) as file:
        for line in file:
            line = line.replace('\n', '').split(' ')
            graph.add_edge(int(line[0]), int(line[1]), float(line[2]))
    return graph

G = build_graph('F://outputs_2/sample_edges_weights', 2129722)
print('Graph is built successfully, begin calculating now...')
print(G.size())
print(len(G.get_edges()))


