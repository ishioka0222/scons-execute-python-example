import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out')
    args = parser.parse_args()

    with open(args.out, 'w') as f:
        f.write('hello, world!')


if __name__ == "__main__":
    main()
