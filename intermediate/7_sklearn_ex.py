"""
Python Libraries - SkLearn

https://scikit-learn.org/stable/
https://www.tensorflow.org/?gclid=EAIaIQobChMIuMaznoDF_AIVgRCLCh1lBA5AEAAYASAAEgI2X_D_BwE
"""


from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, BisectingKMeans
import matplotlib.pyplot as plt

from sklearn.ensemble import HistGradientBoostingRegressor
import numpy as np


def regressor():
    rng = np.random.RandomState(42)
    X_1d = np.linspace(0, 10, num=2000)
    X = X_1d.reshape(-1, 1)
    y = X_1d * np.cos(X_1d) + rng.normal(scale=X_1d / 3)

    quantiles = [0.95, 0.5, 0.05]
    parameters = dict(loss="quantile", max_bins=32, max_iter=50)
    hist_quantiles = {
        f"quantile={quantile:.2f}": HistGradientBoostingRegressor(
            **parameters, quantile=quantile
        ).fit(X, y)
        for quantile in quantiles
    }

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(X_1d, y, "o", alpha=0.5, markersize=1)
    for quantile, hist in hist_quantiles.items():
        ax.plot(X_1d, hist.predict(X), label=quantile)
    _ = ax.legend(loc="lower left")
    plt.show()


regressor()


def clusters():
    X, _ = make_blobs(n_samples=1000, centers=2, random_state=0)

    km = KMeans(n_clusters=5, random_state=0, n_init="auto").fit(X)
    bisect_km = BisectingKMeans(n_clusters=5, random_state=0).fit(X)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].scatter(X[:, 0], X[:, 1], s=10, c=km.labels_)
    ax[0].scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=20, c="r")
    ax[0].set_title("KMeans")
    ax[1].scatter(X[:, 0], X[:, 1], s=10, c=bisect_km.labels_)
    ax[1].scatter(
        bisect_km.cluster_centers_[:, 0], bisect_km.cluster_centers_[:, 1], s=20, c="r"
    )
    ax[1].set_title("BisectingKMeans")
    plt.show()


clusters()
