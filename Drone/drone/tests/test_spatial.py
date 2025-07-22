from .conflict_checker import spatial_conflict

def test_conflict_detected():
    assert spatial_conflict([0,0], [5,5], radius=10)

def test_no_conflict():
    assert not spatial_conflict([0,0], [20,20], radius=10)
