#!/usr/bin/env python3
"""
api_client.py — a fake "connector" to a small item catalog API.

This version deliberately returns RAW, cryptic errors — exactly the kind
a real, poorly-designed API or SDK often gives you. The point of this
project is to compare how an agent behaves against THIS file versus
api_client_actionable.py, which does the identical job but with errors
rewritten to be self-healing.

Commands:
  get-item --id <id>
  create-item --name <name>

Valid ids are 1-100. id 500 always simulates a transient server error,
for a repeatable demo.
"""

import argparse
import os
import sys


def get_item(item_id_raw: str) -> None:
    if not item_id_raw.lstrip("-").isdigit():
        print("Error: 400", file=sys.stderr)
        sys.exit(1)

    item_id = int(item_id_raw)

    if os.environ.get("API_KEY") != "demo-key-123":
        print("Error: 401", file=sys.stderr)
        sys.exit(1)

    if item_id == 500:
        print("Error: 500", file=sys.stderr)
        sys.exit(1)

    if item_id < 1 or item_id > 100:
        print("Error: 404", file=sys.stderr)
        sys.exit(1)

    print(f'{{"id": {item_id}, "name": "Item #{item_id}"}}')


def create_item(name: str | None) -> None:
    if os.environ.get("API_KEY") != "demo-key-123":
        print("Error: 401", file=sys.stderr)
        sys.exit(1)

    if not name:
        print("Error: 400", file=sys.stderr)
        sys.exit(1)

    print(f'{{"id": 101, "name": "{name}", "status": "created"}}')


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_get = sub.add_parser("get-item")
    p_get.add_argument("--id", required=True)

    p_create = sub.add_parser("create-item")
    p_create.add_argument("--name", required=False)

    args = parser.parse_args()

    if args.command == "get-item":
        get_item(args.id)
    elif args.command == "create-item":
        create_item(args.name)


if __name__ == "__main__":
    main()
