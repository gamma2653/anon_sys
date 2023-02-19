from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-n', '--name', required=True, action='store')
# parser.add_argument('')

known_args, _ = parser.parse_known_args()

NAME = known_args.name


