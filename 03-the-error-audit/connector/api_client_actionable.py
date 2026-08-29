#!/usr/bin/env python3
"""
api_client_actionable.py — the IDENTICAL API, with errors rewritten to
be self-healing.

Same commands, same failure conditions as api_client.py. The only thing
that changed is the error message: each one now tells the agent (or a
human) exactly what's wrong and exactly what to do about it — matching
Loop Engineering's connector rule: "the error message is the input to
the next beat."

Commands:
  get-item --id <id>
  create-item --name <name>
"""

import argparse
import os
import sys


def get_item(item_id_raw: str) -> None:
    if not item_id_raw.lstrip("-").isdigit():
        print(
            f"400 Bad Request: '--id {item_id_raw}' is not a valid integer. "
            f"The --id argument must be a whole number, e.g. --id 5. Retry "
            f"with a numeric id.",
            file=sys.stderr,
        )
        sys.exit(1)

    item_id = int(item_id_raw)

    if os.environ.get("API_KEY") != "demo-key-123":
        print(
            "401 Unauthorized: the API_KEY environment variable is missing "
            "or incorrect. Set it before retrying: "
            "export API_KEY=demo-key-123 (this is a demo key for this "
            "project only). Then run the exact same command again.",
            file=sys.stderr,
        )
        sys.exit(1)

    if item_id == 500:
        print(
            "500 Internal Server Error: this is a TRANSIENT failure, not a "
            "problem with your request. Wait a moment and retry the exact "
            "same command unchanged. If it fails 3 times in a row, stop "
            "and report it rather than retrying indefinitely.",
            file=sys.stderr,
        )
        sys.exit(1)

    if item_id < 1 or item_id > 100:
        print(
            f"404 Not Found: no item exists with id {item_id}. Valid ids "
            f"are 1 through 100 inclusive. Check the id and retry with a "
            f"value in that range.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f'{{"id": {item_id}, "name": "Item #{item_id}"}}')


def create_item(name: str | None) -> None:
    if os.environ.get("API_KEY") != "demo-key-123":
        print(
            "401 Unauthorized: the API_KEY environment variable is missing "
            "or incorrect. Set it before retrying: "
            "export API_KEY=demo-key-123. Then run the exact same command "
            "again.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not name:
        print(
            "400 Bad Request: the --name argument is required and was not "
            "provided. Retry with a name, e.g.: "
            'create-item --name "Widget"',
            file=sys.stderr,
        )
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
