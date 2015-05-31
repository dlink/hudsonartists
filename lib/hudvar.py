#!/usr/bin/env python

import os
import sys
import copy

from vlib.utils import pretty, shift, validate_num_args

from parties import Parties

VERBOSE = 0

COMMANDS = {'parties': ['add <field>=<value> [<field>=<value> [...]]',
                        'list'],
             'party': ['get <party_id>']
            }

class HudvarError(Exception): pass

class Hudvar(object):
    '''Hudvar system Seerver'''

    def __init__(self, verbose=VERBOSE):
        self.verbose = verbose

    def process(self, args):
        '''Parse arguments and act upon them'''
        if not args:
            syntax()

        cmd = shift(args)

        # parites

        if cmd == 'parties':
            from parties import Parties
            validate_num_args('parties', 1, args)
            op = shift(args)
            if op == 'add':
                validate_num_args('parties add', 1, args)
                record = {}
                while args:
                    arg = shift(args)
                    if arg.count('=') != 1:
                        raise HudvarError("arguments must be of the form 'field=value': %s" % arg)
                    field, value = arg.split('=')
                    record[field] = value
                party_id = Parties().add(record)
                return party_id

            elif op == 'list':
                o = ''
                p = Parties()
                o += ','.join(p.table_columns)
                for row in p.get():
                    o += ','.join([str(row[c]) for c in p.table_columns]) + '\n'
                return o
            unrecognized_op(cmd, op)

        elif cmd == 'party':
            from parties import Party
            validate_num_args('party', 2, args)
            op = shift(args)
            party_id = shift(args)
            if op == 'get':
                return Party(party_id).data
            unrecognized_op(cmd, op)

        # Fall through
        raise HudvarError('Unrecognized command: %s' % cmd)


def unrecognized_op(cmd, op):
    raise HudvarError('%s: unrecognized op: %s' % (cmd, op))

def syntax_str():
    '''Generate syntax string from hardcoded COMMANDS list, like this:

       Syntax:

          hudvar.py [OPTIONS] parties list
                              party <party_id> show
    '''
    progname = os.path.basename(sys.argv[0])
    ws = ' '*len(progname)

    ln = 0
    o = ''
    for command in sorted(COMMANDS.keys()):
        for ops in COMMANDS[command]:
            ln += 1
            if ln == 1:
                prefix = '   %s [-v] ' % progname
            else:
                prefix = '   %s      ' % ws
            o += "%s%s %s\n" % (prefix, command, ops)
    return o

def syntax():
    progname = os.path.basename(sys.argv[0])
    ws = ' '*len(progname)

    print "Syntax:"
    print
    print syntax_str()
    sys.exit(1)

if __name__ == '__main__':
    args = copy.copy(sys.argv)
    progname = shift(args)
    progname = os.path.basename(progname)

    # verbose?
    verbose = 0
    if '-v' in args:
        verbose = 1
        p = args.index('-v')
        args = args[0:p]+args[p+1:]

    # Do it
    hudvar = Hudvar(verbose=verbose)
    try:
        print pretty(hudvar.process(args))
    except Exception, e:
        if verbose:
            raise
        print "%s: %s" % (e.__class__.__name__, e)


