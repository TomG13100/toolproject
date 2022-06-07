from numpy import dtype
from mlproject.distance import haversine

def test_distance_coordonates():
    assert type(haversine(49.7,2.4,51.2,3.5)) == float
