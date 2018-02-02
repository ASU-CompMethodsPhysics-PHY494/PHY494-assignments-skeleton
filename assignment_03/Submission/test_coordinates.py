import pytest
import importlib

from numpy.testing import assert_almost_equal

@pytest.mark.parametrize("module",
                    ["coordinates_a", "coordinates_b",
                     "coordinates_c", "coordinates_d"])
def test_imports(module):
    try:
        importlib.import_module(module)
    except:
        raise AssertionError("module {} does not import correctly".format(module))



@pytest.mark.parametrize("module,variable,ref",
                         [("coordinates_a", "particle2", [1.34234, 1.34234, 0.0]),
                          ("coordinates_b", "y2", 1.34234),
                          ("coordinates_c", "new_positions",
                           [[1.34234, -1.34234, -1.34234],
                            [2.68468, 0.0, -1.34234],
                            [2.68468, -1.34234, 0.0],
                            [1.34234, 0.0, 0.0]]),
                         ])
def test_abc(module, variable, ref):
    try:
        mod = importlib.import_module(module)
    except:
        raise AssertionError("module {} does not import correctly".format(module))
    result = getattr(mod, variable)
    assert_almost_equal(result, ref)

# hard-code data here (we don't want anyone being able to change the
# input data)
data_d = {"positions":
          [[0.0, 0.0, 0.0],
           [1.34234, 1.34234, 0.0],
           [1.34234, 0.0, 1.34234],
           [0.0, 1.34234, 1.34234]],
          "t": [1.34234, -1.34234, -1.34234],
          "positions2":
          [[1.5, -1.5, 3],
           [-1.5, -1.5, -3]],
          "t2": [-1.5, 1.5, 3]
          }

@pytest.mark.parametrize("positions,t,ref",
                         [(data_d["positions"], data_d["t"],
                           [[1.34234, -1.34234, -1.34234],
                            [2.68468, 0.0, -1.34234],
                            [2.68468, -1.34234, 0.0],
                            [1.34234, 0.0, 0.0]]),
                          (data_d["positions2"], data_d["t2"],
                           [[0.0, 0.0, 6], [-3.0, 0.0, 0]])
                         ])
def test_d(positions, t, ref):
    from coordinates_d import translate
    assert_almost_equal(translate(positions, t), ref)

