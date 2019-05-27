"""Utilities for writing the results of a speed ted to an image."""

import speedtest
from PIL import Image, ImageDraw, ImageFont
import os
from collections import OrderedDict


def do_speedtest() -> dict:
    """Run the speedtest under the default config.
    
    Returns a dictonary with keys specifying each metric followed by its unit. Like `metric_unit`.
    """
    s = speedtest.Speedtest(source_address=None, timeout=10, secure=False)
    s.get_best_server()
    s.download()
    s.upload(pre_allocate=True)

    results_raw = s.results.dict()

    results = OrderedDict()
    results["download_mbits/s"] = round(results_raw["download"] * 1e-6, 1)
    results["upload_mbits/s"] = round(results_raw["upload"] * 1e-6, 1)
    results["ping_ms"] = round(results_raw["ping"], 1)
    return results


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

