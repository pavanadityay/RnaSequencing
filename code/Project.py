import json
import requests

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import normalize
from sklearn.mixture import GaussianMixture


def feature_selection(train_dataset, test_dataset):
    # Variable declarations
    col_with_all_0s = []

    # Dropping columns whose value (Number of zeros) is greater than 10000
    labels = train_dataset.columns
    for col in labels:
        count_zeros = (train_dataset[col] == 0).sum(axis=0)
        if count_zeros > 10000:
            col_with_all_0s.append(col)

    train_dataset.drop(columns=col_with_all_0s, axis=1, inplace=True)
    test_dataset.drop(columns=col_with_all_0s, axis=1, inplace=True)

    # Applying variance filter
    var_thr = VarianceThreshold(
        threshold=0.2
    )  # Removing both constant and quasi-constant
    var_thr.fit(train_dataset)
    var_thr.get_support()
    concol = [
        column
        for column in train_dataset.columns
        if column not in train_dataset.columns[var_thr.get_support()]
    ]

    train_dataset.drop(concol, axis=1, inplace=True)
    test_dataset.drop(concol, axis=1, inplace=True)

    return train_dataset, test_dataset


def dimensionality_reduction(train_dataset, test_dataset):
    # Dimensionality reduction
    pca = PCA(n_components=0.95)
    pca.fit(train_dataset)
    train_data = pca.transform(train_dataset)
    test_data = pca.transform(test_dataset)

    return train_data, test_data


def normalization(dataset):
    # Normalization
    preprocessed_data = normalize(dataset)
    preprocessed_data = pd.DataFrame(preprocessed_data)

    return preprocessed_data


def rna_clustering():
    # Data load and adding header to it
    train_dataset = pd.read_csv("/data/data_tr.txt", sep="\t", header=None)
    test_dataset = pd.read_csv("/data/data_ts.txt", sep="\t", header=None)
    column_names = pd.read_csv("/data/gene_names.txt", header=None)

    labels = column_names[0].tolist()
    train_dataset.columns = labels
    test_dataset.columns = labels

    # Calling function to perform the feature selection
    train_dataset_fs, test_dataset_fs = feature_selection(train_dataset, test_dataset)

    # Calling function to perform dimensionality reduction
    train_dataset, test_dataset = dimensionality_reduction(
        train_dataset_fs, test_dataset_fs
    )

    # Calling function to normalize the data
    train_data = normalization(train_dataset)
    test_data = normalization(test_dataset)

    # Applying GaussianMixture clustering algorithm
    model = GaussianMixture(
        n_components=16, random_state=0, covariance_type="tied", tol=0.004
    )
    model.fit(train_data)
    predictions = model.predict(test_data)

    # Getting evaluation metric score
    score = silhouette_score(test_dataset, predictions, metric="euclidean")
    print("score = ", score)

    # Getting accuracy rate
    url = "https://www.csci555competition.online/scoretest"

    payload = json.dumps(predictions.tolist())

    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


rna_clustering()
