import argparse
from converter.currency import run


def main():
    parser = argparse.ArgumentParser(description="Конвертер валют")

    parser.add_argument('--fromm', required=True, type=int)
    parser.add_argument('--to', required=True, type=int)
    parser.add_argument('--value', required=True, type=float)

    args = parser.parse_args()

    print(run(args.fromm, args.to, args.value))


if __name__ == '__main__':
    main()