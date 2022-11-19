import argparse
from converter.converter_course import run


def main():
    parser = argparse.ArgumentParser(description='Конвертатор валют')

    parser.add_argument('--from_course', required=True, type=str)
    parser.add_argument('--to', required=True, type=str)
    parser.add_argument('--value', required=True, type=float)

    args = parser.parse_args()

    print(run(args.from_course, args.to, args.value))


if __name__ == '__main__':
    main()