"""Unit tests for the Agglomerative Hierarchical Clustering."""

import geomstats.backend as gs
import tests.conftest
from geomstats.geometry.euclidean import Euclidean
from geomstats.geometry.hypersphere import Hypersphere
from geomstats.learning.agglomerative_hierarchical_clustering import (
    AgglomerativeHierarchicalClustering,
)


@tests.conftest.np_and_autograd_only
class TestAgglomerativeHierarchicalClustering(tests.conftest.TestCase):
    """Class defining the Agglomerative Hierarchical Clustering tests."""

    def setup_method(self):
        """Define the parameters to test."""
        gs.random.seed(1234)

    def test_fit_euclidean_distance_callable(self):
        """Test the 'fit' class method using the Euclidean distance."""
        n_clusters = 2
        dimension = 2
        space = Euclidean(dim=dimension)
        dataset = gs.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
        clustering = AgglomerativeHierarchicalClustering(
            space,
            n_clusters=n_clusters,
        )
        clustering.fit(dataset)
        clustering_labels = clustering.labels_
        result = (clustering_labels == gs.array([1, 1, 1, 0, 0, 0])).all() or (
            clustering_labels == gs.array([0, 0, 0, 1, 1, 1])
        ).all()
        expected = True
        self.assertAllClose(expected, result)

    def test_fit_hypersphere_distance(self):
        """Test the 'fit' class method using the hypersphere distance."""
        n_clusters = 2
        dimension = 2
        space = Hypersphere(dim=dimension)
        dataset = gs.array(
            [
                [1, 0, 0],
                [3 ** (1 / 2) / 2, 1 / 2, 0],
                [3 ** (1 / 2) / 2, -1 / 2, 0],
                [0, 0, 1],
                [0, 1 / 2, 3 ** (1 / 2) / 2],
                [0, -1 / 2, 3 ** (1 / 2) / 2],
            ]
        )
        clustering = AgglomerativeHierarchicalClustering(
            space,
            n_clusters=n_clusters,
        )
        clustering.fit(dataset)
        clustering_labels = clustering.labels_
        result = (clustering_labels == gs.array([1, 1, 1, 0, 0, 0])).all() or (
            clustering_labels == gs.array([0, 0, 0, 1, 1, 1])
        ).all()
        expected = True
        self.assertAllClose(expected, result)
