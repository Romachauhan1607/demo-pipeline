from setuptools import setup, find_packages

setup(name="census-income",
      version="2.0.1",
      author="roma",
      author_email="roma.chauhan167@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )

