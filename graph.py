from queue import PriorityQueue

# declear data
edge_list = [
	["a", "c", 5],
	["a", "i", 1],
	["a", "e", 3],
	["c", "e", 6],
	["g", "e", 2],
	["g", "i", 2],
	["g", "h", 3],
	["c", "d", 8],
	["e", "b", 9],
	["d", "b", 5],
	["h", "b", 8]

]

first_person = "a"
second_person = "b"


# here I have mapped string sources to integer to make the algorithm easy
INF = 1000000000000000
MAX_LIST = 12

map_node = {}
demap_node = {}
map_len = 0

def add_node(name):
	global map_node
	global map_len
	if name in map_node.keys():
		return map_node[name]
	else:
		map_node[name] = map_len + 1
		demap_node[str(map_len+1)] = name
		map_len += 1
		return map_len

def get_node(name):
	return map_node[name]

def get_node_name(node_index):
	return demap_node[str(node_index)]



# node class
class node:
	def __init__(self, u, cost):
		self.u = u
		self.cost = cost 

	def __lt__(self, other):
	    return self.cost < other.cost


# dijstkra 
def dijstkra(map_len, node_vector, cost_vector, source):
    distance = [INF] * MAX_LIST
    q = PriorityQueue()
    q.put(node(source, 0))
    distance[source] = 0

    while not q.empty():
    	top = q.get()
    	u = top.u

    	for idx, val in enumerate(node_vector[u]):
    		if distance[u] + cost_vector[u][idx] < distance[val]:
    			distance[val] = distance[u] + cost_vector[u][idx]
    			q.put(node(val, distance[val]))
    return distance


# main problem 
node_vector = []
cost_vector = []

for i in range(MAX_LIST):
	node_vector += [[]]
	cost_vector += [[]]

# insert edges to node_vector and cost_vector with mapping
for edge in edge_list:
	u = add_node(edge[0])
	v = add_node(edge[1])
	cost = edge[2]

	node_vector[u] += [v]
	node_vector[v] += [u]

	cost_vector[u] += [cost]
	cost_vector[v] += [cost]


# print("node_vector")
# print(node_vector)
# print()

# print("cost_vector")
# print(cost_vector)
# print()

# source map
first_source = get_node(first_person)
second_source = get_node(second_person)

nodes = map_len
edges = len(edge_list)

# print("Extras")
# print(map_node)
# print(nodes)
# print(edges)

# print()
# print()


first_distance_list = dijstkra(map_len, node_vector, cost_vector, first_source);
second_distance_list = dijstkra(map_len, node_vector, cost_vector, second_source);


# print("source list")
# print(first_distance_list)
# print(second_distance_list)

# calculate min distance
min_distance = INF
for i in range(MAX_LIST):
	if max(first_distance_list[i] , second_distance_list[i]) < min_distance:
		min_distance = max(first_distance_list[i] , second_distance_list[i])


print(f"from {first_person} to {second_person} -> minimum meeting distance is {min_distance}")

'''
 complexity :
 	we have to travel all nodes and edges.
 	complexity = O(n + e) [ n-> number of nodes, e-> number of edges]
 	here i have used priority queue to store each node. complexity of storing a node in priority queue is log(n)

 	so complexity of this solution is: O(nlog(n) + e) 

'''
