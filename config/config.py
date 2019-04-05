#!/usr/bin/env python3

"""Loads and presents data stored in YAML files, specifically providing the
state manager with all configuration data for all programatically generated
objects.
"""

import yaml


class LoadConfig():

    """Load YAML config file and return a "config" object."""

    def __init__(self):
        """Load all configuration content."""
