import argparse
from converter.currency import run

def main():
    parser = argparse.ArgumentParser(description='Перевод валюты')

    parser.add_argument('--by', required=True, type=str)
    parser.add_argument('--to', required=True, type=str)
    parser.add_argument('--value', required=True, type=float)

    args = parser.parse_args()

    print(run(args.by, args.to, args.value))


if __name__ == '__main__':
    main()