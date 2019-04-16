#!/usr/bin/env python3

"""Manages state, object creation, primary "glue" code."""

from config.config import load_config
from actors.actor import Actor
from pprint import pprint as pp

print("classes: ")
pp(load_config("config/class_traits.yaml")["class_traits"].keys())
print("races: ")
pp(load_config("config/race_traits.yaml")["race_traits"].keys())

test_actor = Actor()
pp(dir(test_actor))
