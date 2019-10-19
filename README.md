[![Build Status](https://travis-ci.com/allankp/json2dynamo.svg?branch=master)](https://travis-ci.com/allankp/json2dynamo)
[![PyPI version](https://badge.fury.io/py/json2dynamo.svg)](https://badge.fury.io/py/json2dynamo)
[![Downloads](https://pepy.tech/badge/json2dynamo)](https://pepy.tech/project/json2dynamo)


# Json to Dynamo Transformer
This tool transforms standard json files into dynamo mapping format. 
Allowing the insertion of the outputed files via the aws cli.


## Install
`pip install json2dynamo`

## Usage
`json2dynamo --inputpath <path/to/json> --outputpath <path/to/output/folder>`

## Development
This repo uses a [bake](https://github.com/kennethreitz/bake) file, to use the commands install it via

`pip install bake-cli`

Once installed run `bake` to see commands