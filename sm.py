#!/usr/bin/env python3

"""Manages state, object creation, primary "glue" code."""

from config.config import load_config
from actors.actor_old import Actor

test_character = Actor(load_config("config/class_traits.yaml"),
                       load_config("config/race_traits.yaml"))
