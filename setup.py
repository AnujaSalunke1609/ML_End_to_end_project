from setuptools import find_packages,setup


setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Anuja Salunke',
    author_email='salunkeanuja999@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)