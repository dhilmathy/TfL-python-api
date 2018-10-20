import setuptools

setuptools.setup(name='tflunifiedapi',
      version='0.2.0',
      description='Python wrapper for Transport for London (TfL) Unified API',
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