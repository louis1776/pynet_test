#!/usr/bin/env python

import yaml
from pprint import pprint


with open("my_dict.yml") as f:
    output = yaml.load(f)

pprint(output)
