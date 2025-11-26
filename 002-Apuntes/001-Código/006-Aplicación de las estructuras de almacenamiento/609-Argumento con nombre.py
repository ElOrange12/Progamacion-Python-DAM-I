import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nomobre')
parser.add_argument('--apellidos')

args = parse.parse_args()

diccionario = vars(args)
print(diccionario)
