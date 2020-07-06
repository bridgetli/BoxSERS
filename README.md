# Advanced processing and machine learning for vibrational spectra

This repository includes SpecMaster, a ready-to-use and efficient python library for processing and applying machine learning to vibrational spectra. Two Jupyter notebooks to aid in the use of Specmaster are also included, as well as a pre-trained machine learning model and a database of SERS bile acid spectra that were used in the article published by **Lebrun and Boudreau (2020)**.


## Setup

### SpecMaster Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install specmaster.

```bash
pip install specmaster
```

### Requirements
Listed below are the main modules needed to operate the codes: 

* Keras
* Sklearn
* Scipy
* Numpy
* Pandas
* Matplotlib
* Tensor flow (GPU or CPU)


## Usage / Description 


### Getting Started 

SpecMaster package covers methods for data augmentation, spectral correction, dimensional reduction and data visualization. Ready-to-use supervised and unsupervised machine learning models with several options are also included in this package. 

It is strongly suggested to start with the two Jupyter notebook script which presents the complete procedure and describes each step in detail while adding information to make it easier to understand.  

- **Important:** This project doesn't cover database conception and requires user to have completed this step before using this project. As an indication, the rows of the database must correspond to the different spectra and the columns to the different Raman shift or wavelenght. The column(s) with the labels must be appended to the left of the database.

### Spectrum Visualization

* Generation of the training, validation and test sets
* Visualization feature to check the distribution of the different classes in each newly generated set.

### Database Splitting

Functions: 
- **data_split**: Generates two subsets of spectra from the input database.
- **distribution_plot**: Plots the distribution of the different classes in a selected set.

```python
from specmaster import data_split, distribution_plot

(x_train, x_int, y_train, y_int) = data_split(spectra, lab_enc, b_size=0.4, rdm_ste=3, report_enabled=False)

distribution_plot(y_train, title='Train set distribution', class_names=classnames)
```


### Spectral Data Augmentation
* Spectra mixeup: linear combination of two or three spectra 
* Simple data augmentation methods: Noise addition, offset , multiplicative factor
* Visualization feature to check the results of different data augmentation methods

### Spectral Data Correction
* Savitsy-Golay Smoothing
* ALS baseline correction 
* Data cut 

### Dimensional reduction
* Principal component analysis visualization 

### Unsupervised Machine Learning Models 

### Supervised Machine Learning Models 
* Convolutional Neural Networt (3 x Convolutional layer 1D , 2 x Dense layer)   


```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
