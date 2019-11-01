![](https://github.com/allankp/json2dynamo/workflows/master/badge.svg)
[![PyPI version](https://badge.fury.io/py/json2dynamo.svg)](https://badge.fury.io/py/json2dynamo)
[![Downloads](https://pepy.tech/badge/json2dynamo)](https://pepy.tech/project/json2dynamo)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a48990e744fd4eb5be47400b6faa64af)](https://www.codacy.com/manual/allankp/json2dynamo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=allankp/json2dynamo&amp;utm_campaign=Badge_Grade)

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