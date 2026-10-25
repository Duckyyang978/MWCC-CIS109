
import argparse
from cryptlib import encrypt, decrypt


def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a message using a Caesar cipher."
    )

    action = parser.add_mutually_exclusive_group(required=True)

    action.add_argument(
        "-e",
        "--encrypt",
        action="store_true",
        help="Encrypt the message"
    )

    action.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        help="Decrypt the message"
    )

    parser.add_argument(
        "-m",
        "--message",
        required=True,
        help="The message to encrypt or decrypt"
    )

    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        default=3,
        help="Number of positions to shift (default: 3)"
    )

    args = parser.parse_args()

    if args.encrypt:
        result = encrypt(args.message, args.shift)
    else:
        result = decrypt(args.message, args.shift)

    print(result)


if __name__ == "__main__":
    main()
