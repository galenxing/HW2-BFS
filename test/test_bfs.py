# write tests for bfs
import pytest
import pathlib
from search import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    data_dir = pathlib.Path(__file__).resolve().parent
    
    g = Graph(data_dir/'../data/tiny_network.adjlist')
    
    bfs = g.bfs('31806696')
    
    assert len(bfs) == 30
    assert bfs == ['31806696',
                   'Luke Gilbert',
                     '33483487',
                     '31626775',
                     '31540829',
                     'Martin Kampmann',
                     'Neil Risch',
                     'Nevan Krogan',
                     '32790644',
                     '29700475',
                     '34272374',
                     '32353859',
                     '30944313',
                     'Steven Altschuler',
                     'Lani Wu',
                     'Michael Keiser',
                     'Atul Butte',
                     'Marina Sirota',
                     'Hani Goodarzi',
                     '32036252',
                     '32042149',
                     '30727954',
                     '33232663',
                     '33765435',
                     '33242416',
                     '31395880',
                     '31486345',
                     'Michael McManus',
                     'Charles Chiu',
                     '32025019'
                  ]
   
def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    data_dir = pathlib.Path(__file__).resolve().parent
    g = Graph(data_dir/'../data/citation_network.adjlist')
    bfs = g.bfs('33217318', 'Steven Altschuler')

    assert len(bfs) == 2
    assert g.bfs('34930904', '34874009') is None
    
    with pytest.raises(Exception):
        g.bfs('asdfasdf')
    
    with pytest.raises(Exception):
        assert g.bfs('34930904', 'asdfasdf')
        

    