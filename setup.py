from setuptools import setup, find_packages

setup(
    name='BoxSERS',
    url='https://github.com/ALebrun-108/BoxSERS',
    author='Alexis Lebrun',
    author_email='alexis.lebrun.1@ulaval.ca',
    # dependencies
    install_requires=['joblib', 'numpy', 'pandas', 'scikit-learn', 'matplotlib', 'scipy', 'seaborn', 'keras',
                      'tensorflow'],
    python_requires='>=3',
    # *strongly* suggested for sharing
    version='0.1.1',
    # The license can be anything you like
    license='MIT',
    description='Provides a full range of functionality to process and analyze vibrational spectra.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
)
