from __future__ import print_function
import shlex

from libearth.repository import from_url
from libearth.session import Session
from libearth.stage import Stage

ITEM_PREFIX = '$'
PROMPT = '>'


def quit(stage, *args):
    print('Bye bye')
    exit(0)


def read_loop(stage):
    commands = {
        'exit': quit,
    }

    while 1:
        args = shlex.split(raw_input(PROMPT))

        if not args:
            continue

        if args[0] not in commands:
            print('Command not found')
            continue

        commands[args[0]](stage, *args[1:])


def main(args):
    stage = Stage(
        Session(args.session_id),
        from_url(args.repository_dir)
    )

    read_loop(stage)
