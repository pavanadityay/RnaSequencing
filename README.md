# Single Cell RNA Sequencing
## _Clustering of Genes and samples_

Single-cell Rna sequencing is a well-known genomic technique for detecting and quantifying messenger RNA molecules in biological samples, and it's valuable for investigating cellular responses.

- ##### Operating system : Windows 7 or greater
- #####  IDE's:  Visual Studio Code(Recommended) or Pycharm IDE
- ##### Language Used: Python

## Dataset

The `data_tr.txt` file contains total of 13177 data points with 13166 features. The data is related to Single-cell RNA sequencing (scRNA-seq) which is a favoured technique that enables the power to profile a entire transcriptomes of individual cells. 'data_ts' file is our test data with 13,166 features and few samples. They can be downloaded from the below links that are provided and should be included in the data folder.
- [Training dataset](https://drive.google.com/file/d/1wzKaUp7b6GidHez3yoH1i7RECNhLWjOu/view?usp=sharing)
- [Testing dataset](https://drive.google.com/file/d/1Tps1XNCB37uQgkjjdI_tZ_LMzxzTbe0T/view?usp=sharing)
- [Labels](https://drive.google.com/file/d/1eqDC_Jroi9kFgAM1CVKQ2vpmCrMFLz2k/view?usp=sharing)

## Installation

The project code should be executed on Python and can be downloaded from below:
- [Python](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe) 

Python's package manager(Pip) is required to install python libraries. This will be downloaded and installed automatically with the above step. In case if its not installed by default, follow the below steps:
- Download the package from [Package Manager](https://bootstrap.pypa.io/get-pip.py) using Firefox browser. For any other browser, right click on the opened page and click `Save As` to save the file
- From command prompt, navigate to the directory where the pacakge is downloaded
- Run the command `python get-pip.py`

To install the dependent libraries execute the below commands in command prompt:
- pip install pandas
- pip install -U scikit-learn

To run the code, we also need an IDE which can be installed from [Visual Studio](https://code.visualstudio.com/docs/python/python-tutorial)  or [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

## Code

- The executable code is given in the code folder and the filename is `Project.py`. The code performs the preprocessing on training and testing datasets followed by dimensionality reduction,scaling and normalization to cluster the data.
-  The model is built and the test data is passed to calclulate silhoutte score which is our internal evaluation metric and the clusters are passed to a Web Service API to get the actual score based on an external evaluation metric called rand_index. 

## Execution
Run `Project.py` which is available in the Code folder, dataset files that are mentioned above should be downloaded and placed in `data` folder and follow the below steps:
- Open Visual Studio
- Click on `Explorer` (option which is available left top corner)
- From pop-up window, click `Open Folder` and navigate to the folder where the `Project.py` is kept
- Once the Explorer lists the file names, double click on `Project.py` to open and click on `Run Python File` which is available at the right top corner (looks like play button)

## Repository

Project Link: https://github.com/pavanadityay/RnaSequencing








