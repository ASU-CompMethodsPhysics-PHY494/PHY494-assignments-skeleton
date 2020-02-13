import pytest
import importlib

from numpy.testing import assert_almost_equal

import numpy as np

try:
    import skimage, skimage.io
    HAS_SKIMAGE = True
except ImportError:
    HAS_SKIMAGE = False

    # make sure that students are notified at the end of tests
    # (based on https://stackoverflow.com/a/38806934)
    import atexit
    def report():
        print("\n" + 60*"*" + "\n"
              "Some tests were SKIPPED because a package is missing that is needed\n"
              "for testing.\n"
              "For a complete test, install 'scikit-image' https://scikit-image.org/\n"
              "with the following command:\n\n"
              "   conda install scikit-image\n\n"
              "You can then rerun the tests and should see no more SKIPPED tests.\n"
              + 60*"*" + "\n"
              )
    atexit.register(report)


class TestProblem1(object):
    @pytest.fixture(scope="class")
    def solution(self):
        return importlib.import_module("problem1")

    def test_1b1(self, solution):
        assert_almost_equal(solution.result1b1,
                            np.zeros((2, 2), dtype=np.complex128))

    def test_1b2(self, solution):
        assert_almost_equal(solution.result1b2,
                            np.diag([1j, 1j]))

    def test_1b3(self, solution):
        assert_almost_equal(solution.result1b3,
                            2*1j*solution.sz)


class TestProblem2(object):
    @pytest.fixture(scope="class")
    def solution(self):
        return importlib.import_module("problem2")

    def test_2c(self, solution):
        assert_almost_equal(solution.result2c,
                            np.array([ 1.34234,  1.34234,  0.     ]))

    def test_2d(self, solution):
        assert_almost_equal(solution.result2d, 1.34234)

    def test_2e(self, solution):
        assert_almost_equal(solution.result2e,
                            np.array([[ 1.34234, -1.34234, -1.34234],
                                      [ 2.68468,  0.     , -1.34234],
                                      [ 2.68468, -1.34234,  0.     ],
                                      [ 1.34234,  0.     ,  0.     ]]))

    @pytest.mark.parametrize("x,t",
                             [
                                 (np.array(
                                     [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0],
                                      [1.34234, 0.0,  1.34234], [0.0, 1.34234, 1.34234]]),
                                  np.array([1.34234, -1.34234, -1.34234])),
                                 (np.array([[1.5, -1.5, 3], [-1.5, -1.5, -3]]),
                                  np.array([-1.5, 1.5, 3]))
                             ])
    def test_2f(self, solution, x, t):
        assert_almost_equal(solution.translate(x, t), x + t)


class TestProblem3a(object):
    @pytest.fixture(scope="class")
    def solution(self):
        return importlib.import_module("problem3a")

    def test_X(self, solution):
        assert_almost_equal(solution.X, np.arange(-6, 6, 0.2))

    def test_Y(self, solution):
        assert_almost_equal(solution.Y, np.sinc(np.arange(-6, 6, 0.2)))

    @pytest.mark.skipif(not HAS_SKIMAGE,
                        reason="Install scikit-image for this test to run")
    def test_png(self, filename="sinc.png"):
        # just make sure we can load it as an image file, not sure
        # how to do a real image comparison...
        img = skimage.io.imread(filename)
        assert len(img.shape) == 3


def test_Problem3b():
    solution = importlib.import_module("problem3b")
    assert_almost_equal(solution.mypi, 3.1320765318091062)

@pytest.mark.xfail
class TestProblem3c(object):
    @pytest.fixture(scope="class")
    def solution(self):
        return importlib.import_module("problem3c")

    @pytest.mark.parametrize("s,Nmax,result",
                             [
                                 (1, 10000, 9.78760604),
                                 (2, 100, 1.6349839),
                                 (2, 10000, 1.64483407),
                                 (5./3., 1000, 2.10852797),
                                 (5, 10000, 1.03692776),
                                 (10, 100, 1.00099458),
                             ])
    def test_zeta(self, solution, s, Nmax, result):
        assert_almost_equal(solution.zeta(s, Nmax), result)

    @pytest.mark.skipif(not HAS_SKIMAGE,
                        reason="Install scikit-image for this test to run")
    def test_png(self, filename="zeta.png"):
        # just make sure we can load it as an image file, not sure
        # how to do a real image comparison...
        img = skimage.io.imread(filename)
        assert len(img.shape) == 3

