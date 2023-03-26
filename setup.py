from setuptools import setup, find_packages

setup(name="census_income",
      version="0.0.1",
      description="A package to calculate income",
      author="Saroj Nilesh",
      author_email="sarojnilesh10@gmail.com",
      packages=find_packages(),
      install_requires=[
          'numpy',
          'pandas',
          'flask']
      )