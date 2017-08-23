import sys
import igraph
from igraph import *

def create_co_occurrence(words, is_directed, window_size, output_file):
    g = Graph(directed = is_directed)
    
    g.add_vertices(words[0])
    for i in range(1,len(words)):
        if words[i] not in g.vs['name']:
            g.add_vertices(words[i])
        if not g.are_connected(words[i-1],words[i]):
            g.add_edge(words[i-1],words[i])
        #adding the connections for other window sizes
        if i > 1 and window_size > 1:
            if not g.are_connected(words[i-2],words[i]):
                g.add_edge(words[i-2],words[i])
        if i > 2 and window_size > 2:
            if not g.are_connected(words[i-3],words[i]):
                g.add_edge(words[i-3],words[i])

    g.vs['id'] = g.vs['name'] 
    g.write_pajek(output_file)

if __name__ == '__main__':
    if len(sys.argv) < 5: 
        sys.exit("Input format is wrong. Missing arguments.")

    direction = sys.argv[1]
    if direction == "-d": 
        is_directed = True
    elif direction == "-u": 
        is_directed = False
    else: 
        sys.exit("Input format is wrong. Expecting -d or -u")

    window_size = sys.argv[2]
    if(window_size.isdigit() == False or int(window_size) < 1 or int(window_size) > 3):
        sys.exit("Input format is wrong. Expecting 1, 2 or 3 for the window size.")

    input_file = sys.argv[3]
    input_data = open(input_file).read().split()

    output_file = sys.argv[4]

    create_co_occurrence(input_data, is_directed, int(window_size), output_file)