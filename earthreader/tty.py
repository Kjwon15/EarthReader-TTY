from __future__ import print_function
import shlex
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from libearth.repository import from_url
from libearth.session import Session
from libearth.stage import Stage

ITEM_PREFIX = '$'
PROMPT = '>'


def quit(stage, *args):
    print('Bye bye')
    exit(0)


def print_subscriptions(stage, *args):
    def print_category(subscriptions, indent, depth=0):
        for (title, category) in subscriptions.categories.items():
            print('{0}{1}'.format(indent*depth, title))
            print_category(category, indent, depth=depth+1)
        for subs in subscriptions.subscriptions:
            print('{0}{1}'.format(indent*depth, subs.label))

    indent = '+---'
    with stage:
        print_category(stage.subscriptions, indent)


def read_loop(stage):
    commands = {
        'exit': quit,
        'subscriptions': print_subscriptions,
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
