#!/usr/bin/env python3
"""Validate a repository's scopes.yaml against the organization schema."""

import json
import pathlib
import sys

import jsonschema
import yaml

SCHEMA_PATH = pathlib.Path(__file__).resolve().parent / "scopes.schema.json"


def main() -> int:
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "scopes.yaml")
    if not target.exists():
        print(f"::error::{target} not found - every repository must have one at its root")
        return 1

    with SCHEMA_PATH.open(encoding="utf-8") as f:
        schema = json.load(f)
    try:
        with target.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"::error::{target} is not valid YAML: {e}")
        return 1

    try:
        jsonschema.validate(data, schema)
    except jsonschema.ValidationError as e:
        location = "/".join(str(p) for p in e.absolute_path) or "(root)"
        print(f"::error::{target} does not match scopes.schema.json at {location}: {e.message}")
        return 1

    print(f"{target}: valid against scopes.schema.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
