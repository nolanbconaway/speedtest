"""CLI Handler for the speedtestimage package."""

import argparse
import datetime

from speedtestimage import do_speedtest
from speedtestimage import text_to_image
from speedtestimage import rgba_string


def rgba_string(v: str) -> tuple:
    """Parse a comma delimited RGBA string.
    
    This does checkes to ensure its a valid RGBA string, then parses it and returns the tuple.
    """
    # split comma delimited string
    parts = v.split(",")

    # check all values are digits
    if not all(map(lambda x: x.isdigit(), parts)):
        raise argparse.ArgumentTypeError(f"Nondigit value detected, got {v}.")

    parts = tuple(int(i) for i in parts)

    if len(parts) != 4:
        raise argparse.ArgumentTypeError(f"RGBA requires four values, got {v}")

    if not all(map(lambda x: x <= 255 and x >= 0, parts)):
        raise argparse.ArgumentTypeError(f"All values must be 0-255, got {v}")

    return parts


def main():
    """CLI handler."""
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("out", help="Save destination. Must end in .png", type=str)
    parser.add_argument(
        "-t",
        "--txtcolor",
        help="Text color. Comma delimited RGBA. Default=0,0,0,255 (black).",
        type=rgba_string,
        default="0,0,0,255",
        nargs="?",
    )
    parser.add_argument(
        "-b",
        "--backcolor",
        help="Back color. Comma delimited RGBA. Default=255,255,255,0 (transparent white).",
        type=rgba_string,
        default="255,255,255,0",
        nargs="?",
    )

    # super secret. run it in test mode.
    parser.add_argument("--test", action="store_true", help=argparse.SUPPRESS)

    args = parser.parse_args()

    # validate out arg
    if not args.out.endswith(".png"):
        raise ValueError(f"Invalid out path: {args.out}.")

    results = (
        dict(download_mb=100.5, upload_mb=30.2, ping_ms=18.2)
        if args.test
        else do_speedtest()
    )
    text = "My network speedtest! \n"
    text += "\n".join(
        f"""{k.split('_')[0]:9s}: {v} {k.split('_')[1]}""" for k, v in results.items()
    )
    text += "\n" + f"""  as of {datetime.datetime.utcnow().strftime('%c')} UTC"""
    img = text_to_image(text, fill=args.txtcolor, background=args.backcolor)
    img.save(args.out, format="png")


if __name__ == "__main__":
    main()

