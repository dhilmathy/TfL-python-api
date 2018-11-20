[![PyPi Version](https://img.shields.io/pypi/v/sfctl.svg)](https://pypi.org/project/tflunifiedapi/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sfctl.svg)](https://pypi.org/project/tflunifiedapi/)
[![License](https://img.shields.io/pypi/l/sfctl.svg)](https://github.com/dhilmathy/TfL-python-api/blob/master/LICENSE)

# TfL-python-api

This repository contains Python APIs for interacting with Transport for London (TfL). 

Transport for London (TfL) Unified API is released [here](https://api.tfl.gov.uk/) is for open data users to use in their own software and services. 

## Installation

```pip install tflunifiedapi```

## Get Started

To use the TfL Unified API, developers should [register](https://api-portal.tfl.gov.uk/) for an Application ID (`app_id`) and Application Key (`app_key`).

```python
from tfl.client import Client
from tfl.api_token import ApiToken

app_id = 'APPLICATION ID'
app_key = 'APPLICATION KEY'

token = ApiToken(app_id, app_key)

client = Client(token)
print (client.get_line_meta_modes())
print (client.get_lines(mode="bus")[0])
print (client.get_lines(line_id="victoria")[0])
```

## API Documentation

This Python library provide a thin wrapper around the TfL Unified APIs. See the [Transport for London Unified API](https://api.tfl.gov.uk/) for more details.
