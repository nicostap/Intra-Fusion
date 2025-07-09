from setuptools import setup, find_packages

setup(
    name='torch_pruning_ot',
    version='0.1',
    packages=find_packages(where='.'),
    package_dir={'': '.'},
    install_requires=[
        'torch',
        'numpy',
        'scikit-learn',
        'POT'
    ],
)