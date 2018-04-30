"""Unit tests for base_manifolds module."""

import numpy as np
import unittest

from geomstats.manifold import Manifold


class TestManifoldMethods(unittest.TestCase):
    _multiprocess_can_split_ = True

    def setUp(self):
        self.dimension = np.random.randint(low=1, high=10)
        self.manifold = Manifold(self.dimension)

    def test_dimension(self):
        result = self.manifold.dimension
        expected = self.dimension
        self.assertTrue(np.allclose(result, expected))

    def test_belongs(self):
        point = np.array([1, 2, 3])
        self.assertRaises(NotImplementedError,
                          lambda: self.manifold.belongs(point))

    def test_regularize(self):
        point = np.array([1, 2, 3])
        self.assertTrue(np.allclose(point, self.manifold.regularize(point)))


if __name__ == '__main__':
        unittest.main()
