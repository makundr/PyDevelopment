import argparse
import cowsay

parser = argparse.ArgumentParser(
    prog='cowsay',
    description='Realization package cowsay')


parser.add_argument('message', type=str, nargs='?', default='',  help='Text for cow')
parser.add_argument('-e', type=str, default='oo', help='A custom eye string')
parser.add_argument('-f', help='A custom string representing a cow')
parser.add_argument('-l', action='store_true', default='default', help='List all cowfiles')
parser.add_argument('-T', type=str, default='', help='A custom tongue string')
parser.add_argument('-W', type=int, default=40, help='The width of the text bubble')
parser.add_argument('-p', action='store_true', help='paranoia mode')
parser.add_argument('-b', action='store_true', help='borg mode')
parser.add_argument('-d', action='store_true', help='dead mode')
parser.add_argument('-y', action='store_true', help='young mode')
parser.add_argument('-g', action='store_true', help='greedy mode')
parser.add_argument('-s', action='store_true', help='stoned mode')
parser.add_argument('-t', action='store_true', help='tired mode')
parser.add_argument('-w', action='store_true', help='wired mode')


args = parser.parse_args()

if args.l != 'default':
    print(cowsay.list_cows())
else:
    preset = ''
    for i in 'pbdygstw':
        if i in args.__dict__:
            preset += i
    print(cowsay.cowsay(message=args.message, preset=preset, eyes=args.e, tongue=args.T, width=args.W, wrap_text=args.n, cowfile=args.f))