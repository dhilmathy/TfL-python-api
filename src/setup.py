import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='tflunifiedapi',
      version='0.2.1',
      description='Python wrapper for Transport for London (TfL) Unified API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/dhilmathy/TfL-python-api',
      author='Mathivanan Palanisamy',
      author_email='mathy@outlook.com',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False,
      install_requires=[
          'msrest',
      ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        ])