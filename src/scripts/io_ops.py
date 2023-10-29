from pathlib import Path
import os, sys, json

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


def file_operations(in_file, out_file):
    in_file = os.path.join(parentdir, 'data', in_file)
    out_file = os.path.join(parentdir, 'data', out_file)
    with open(in_file, 'r') as input_file, open(out_file, 'w') as output_file:
        output_file.write(input_file.read())


def write_to_file(data, out_file):
    out_file = os.path.join(parentdir, 'data', out_file)
    with open(out_file, 'w') as output_file:
        json.dump(data, output_file)
