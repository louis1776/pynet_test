#!/usr/bin/env python
import yaml
from pprint import pprint


with open ("my_list.yml") as f:
    output = yaml.load(f)

pprint(output)
