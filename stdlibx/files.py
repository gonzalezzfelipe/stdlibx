import ast
import json
import logging
from configparser import RawConfigParser

import yaml


def read(path, **kwargs):
    with open(path, 'r', **kwargs) as _file:
        return _file.read()


def read_yaml(filepath, **kwargs):
    """Load contents of YAML file."""
    return yaml.safe_load(read(filepath), **kwargs)


def read_json(filepath, **kwargs):
    """Load content of JSON file into python."""
    return json.loads(read(filepath), **kwargs)


def read_cfg(filepath, **kwargs):
    """Load content of CFG file into python."""
    cp = RawConfigParser(**kwargs)
    cp.read(filepath)
    conf = {}
    for section in cp.sections():
        items = dict(cp.items(section))
        for k, v in items.items():
            items[k] = ast.literal_eval(v)
        conf[section] = items
    return conf


def read_extension(
        filepath,
        cfg_kwargs=None,
        json_kwargs=None,
        yaml_kwargs=None):
    if filepath.endswith('.cfg'):
        return read_cfg(filepath, **(cfg_kwargs or {}))
    elif filepath.endswith('.json'):
        return read_json(filepath, **(json_kwargs or {}))
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return read_yaml(filepath, **(yaml_kwargs or {}))
    else:
        logging.warning('Extension not recognised.')
        return read(filepath)
