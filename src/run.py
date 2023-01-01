import argparse
from scripts.api_calls import get_generic, post_generic, put_generic, delete_generic
from scripts.io_ops import file_operations


def add_args(parser):
    parser.add_argument('--get', required=False, help='Path variable for the GET endpoint')
    parser.add_argument('--post', required=False, help='Path variable for the POST endpoint')
    parser.add_argument('--put', required=False, help='Path variable for the PUT endpoint')
    parser.add_argument('--delete', required=False, help='Path variable for the DELETE endpoint')

    parser.add_argument('--input', required=False, help='input file')
    parser.add_argument('--output', required=False, help='output file')


def main():
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()

    if args.get:
        get_generic(args.get)
        return

    if args.post:
        post_generic(args.post)
        return

    if args.put:
        put_generic(args.put)
        return

    if args.delete:
        delete_generic(args.delete)
        return

    if args.input and args.output:
        file_operations(args.input, args.output)
        return


if __name__ == '__main__':
    main()
