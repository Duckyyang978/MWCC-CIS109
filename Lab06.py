
import argparse


def transform_upper(text):
    return text.upper()


def transform_lower(text):
    return text.lower()


def get_word_count(text):
    return len(text.split())


def filter_short(text, min_length):
    if len(text) > min_length:
        return text
    else:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--action", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--min-length", type=int, default=3)

    args = parser.parse_args()

    data_list = args.data.split(",")

    for item in data_list:
        if args.action == "upper":
            result = transform_upper(item)
        elif args.action == "lower":
            result = transform_lower(item)
        elif args.action == "count":
            result = get_word_count(item)
        elif args.action == "filter":
            result = filter_short(item, args.min_length)
        else:
            print("Invalid action")
            break

        if result is not None:
            print(result)
