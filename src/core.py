import networkx as nx
def add_travel_time(graph,speed_kph=30):
    if speed_kph<=0: raise ValueError("speed must be positive")
    out=graph.copy(); metres_per_second=speed_kph*1000/3600
    for _,_,data in out.edges(data=True):
        if "length" not in data: raise ValueError("edge length is required")
        data["travel_time"]=data["length"]/metres_per_second
    return out
def reachable_nodes(graph,center,minutes):
    if minutes<0: raise ValueError("minutes must be non-negative")
    return nx.single_source_dijkstra_path_length(graph,center,cutoff=minutes*60,weight="travel_time")
def catchment_subgraph(graph,center,minutes): return graph.subgraph(reachable_nodes(graph,center,minutes)).copy()
