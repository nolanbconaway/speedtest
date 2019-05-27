"""Utilities for writing the results of a speed ted to an image."""

import speedtest
from PIL import Image, ImageDraw, ImageFont
import os


def do_speedtest() -> dict:
    """Run the speedtest under the default config.
    
    Returns a dictonary with keys specifying each metric followed by its unit. Like `metric_unit`.
    """
    s = speedtest.Speedtest()
    s.get_servers([])
    s.get_best_server()
    s.download()
    s.upload()

    results = s.results.dict()

    return dict(
        download_mb=round(results["download"] / 8e6, 1),
        upload_mb=round(results["upload"] / 8e6, 1),
        ping_ms=round(results["ping"], 1),
    )


def text_to_image(
    text: str, fill: tuple = (0, 0, 0), background: tuple = (255, 255, 255, 0)
) -> Image:
    """Build a simple image with text on it.
    
    Options for the text and background color. The size of the image was predetermined based
    on the amount of space you'd need for the current text.
    """
    img = Image.new("RGBA", (350, 105), color=background)
    font = ImageFont.truetype(
        os.path.join(os.path.split(__file__)[0], "Courier.ttf"), 15
    )

    d = ImageDraw.Draw(img)
    d.text((10, 10), text, fill=fill, font=font)

    return img

