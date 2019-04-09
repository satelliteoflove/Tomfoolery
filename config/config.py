#!/usr/bin/env python3

"""Loads and presents data stored in YAML files, specifically providing the
state manager with all configuration data for all programatically generated
objects.
"""

import yaml


def load_config(config_file):
    try:
        with open(config_file, 'r') as conf:
            cfg = yaml.safe_load(conf)
            return cfg
    except FileNotFoundError as fnf_error:
        print(fnf_error)