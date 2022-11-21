import argparse
from converter.currency import run2


def main():
    parser = argparse.ArgumentParser(description='Конвертер валют')

    parser.add_argument('--out_of', required=True, type=int)
    parser.add_argument('--to', required=True, type=int)
    parser.add_argument('--value', required=True, type=float)

    args = parser.parse_args()

    print(run2(args.out_of, args.to, args.value))


if __name__ == '__main__':
    main()

# --from заменил на --out_of, так как в конструкции args.from этот from воспринимается как инструмент python 