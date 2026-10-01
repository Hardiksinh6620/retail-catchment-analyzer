import networkx as nx
from src.core import add_travel_time,reachable_nodes,catchment_subgraph
def test_catchment():
    g=nx.Graph(); g.add_edge(1,2,length=1000); g.add_edge(2,3,length=1000); g=add_travel_time(g,60)
    assert set(reachable_nodes(g,1,1.1))=={1,2}
    assert set(catchment_subgraph(g,1,1.1))=={1,2}
