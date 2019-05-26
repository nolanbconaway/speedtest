# speedtestimage

A command line utility to save the results of a speed test to an image.

This is useful if, for example, you want to serve the result as an image over HTTP.

## Install

I'm just installing over git for now.

```sh
pip install git+https://github.com/nolanbconaway/speedtestimage.git
```

## Usage

```sh
$ speedtestimage -h                                       
usage: speedtestimage [-h] [-t [TXTCOLOR]] [-b [BACKCOLOR]] out

positional arguments:
  out                   Save destination. Must end in .png

optional arguments:
  -h, --help            show this help message and exit
  -t [TXTCOLOR], --txtcolor [TXTCOLOR]
                        Text color. Comma delimited RGBA. Default=0,0,0,255
                        (black).
  -b [BACKCOLOR], --backcolor [BACKCOLOR]
                        Back color. Comma delimited RGBA.
                        Default=255,255,255,0 (transparent white).
```

### Example:

```sh
$ speedtestimage speedtest.png --backcolor 100,100,100,255
```

![](speedtest.png)