file = "input.txt"
file = "test2.txt"

import networkx as nx

def part1():
    G = nx.DiGraph()  # a directed graph

    direct_cnt = 0
    indirect_cnt = 0

    with open(file) as f:
        for line in f:
            a, b = line.strip().split(")")

            G.add_edge(a, b)

    orbit_count = 0

    for node in G.nodes:
        print node, nx.descendants(G, node), len(nx.descendants(G, node))
        orbit_count += len(nx.descendants(G, node))
    print orbit_count


def part2():
    G = nx.DiGraph()  # a directed graph

    direct_cnt = 0
    indirect_cnt = 0

    with open(file) as f:
        for line in f:
            a, b = line.strip().split(")")

            G.add_edge(a, b)

    min_dist = 99999999
    print G.nodes
    for node in G.nodes:
        value_set = set()

        print node, nx.dfs_successors(G, node), len(nx.dfs_successors(G, node))
        for i in nx.dfs_successors(G, node):
            for j in i:
                for k in (nx.dfs_successors(G, node)[j]):
                    value_set.add(k)

        if ("YOU" in value_set) & ("SAN" in value_set):
            dist = len(nx.dfs_successors(G, node)) -1

            if dist < min_dist:
                min_dist = dist

        print min_dist

if __name__ == '__main__':

    part2()