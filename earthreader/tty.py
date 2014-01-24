from __future__ import print_function
import shlex
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from libearth.repository import from_url
from libearth.session import Session
from libearth.stage import Stage

SUBSCRIPTION_PREFIX = '$'
SUBSCRIPTIONS = {0: 'all'}
PROMPT = '>'


def quit(stage, *args):
    print('Bye bye')
    exit(0)


def print_subscriptions(stage, *args):
    def add_to_subscriptions(subscription):
        index = max(SUBSCRIPTIONS.keys()) + 1
        SUBSCRIPTIONS[index] = subscription
        return index

    def print_category(subscriptions, indent, depth=1):
        for (title, category) in subscriptions.categories.items():
            index = add_to_subscriptions(category)
            print('{0}{1} {2}'.format(indent*depth,
                                      SUBSCRIPTION_PREFIX + str(index),
                                      title))
            print_category(category, indent, depth=depth+1)
        for subs in subscriptions.subscriptions:
            index = add_to_subscriptions(subs)
            print('{0}{1} {2}'.format(indent*depth,
                                      SUBSCRIPTION_PREFIX + str(index),
                                      subs.label))

    indent = '+---'
    with stage:
        print('{0} {1}'.format(SUBSCRIPTION_PREFIX + str(0),
                              SUBSCRIPTIONS[0]))
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
