"""
processor.py — a small file the hooks will watch.

Ask Claude Code to add error handling to this function using a bare
`except:` clause, and watch what each hook does about it.
"""


def process_item(item):
    try:
        return item.upper()
    except:
        pass
