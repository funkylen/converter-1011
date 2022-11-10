import argparse
from converter.converter import run


def main():
    parser = argparse.ArgumentParser(description='Перевод единиц измерения')

    parser.add_argument('--option1', required=True, type=int)
    parser.add_argument('--option2', required=True, type=int)
    parser.add_argument('--number', required=True, type=float)

    args = parser.parse_args()

    print(run(args.option1, args.option2, args.number))


if __name__ == '__main__':
    main()
