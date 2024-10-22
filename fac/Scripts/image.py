import click
import cv2 as cv
import os
import sys
from . import blurframe


@click.command()
@click.argument("img_path", type=click.Path(exists=True, file_okay=True))
@click.option(
    "-o",
    "--output",
    "output",
    default=None,
    show_default="{img_name}_fac.{img_extension}",
    type=click.Path(writable=True),
    help="Enter output path for image",
)
def image(img_path, output):

    if output == None:
        directory, img_name = os.path.split(img_path)
        img_name = img_name.split(".")

        if len(img_name) < 2:
            sys.exit("Enter path with image file.")

        img_name[0] = f"{img_name[0]}_fac"
        output = ".".join(img_name)

    else:
        outpath, output_image = os.path.split(output)
        output_image = output_image.split(".")

        if len(output_image) < 2:
            sys.exit("Enter output path with image name.")

        if not os.path.exists(outpath):
            os.mkdir(outpath)

    img = cv.imread(img_path)
    blurredimage = blurframe.blurframe(img)

    cv.imwrite(output, blurredimage)
    if os.path.exists(output):
        print(f"Image Successfully blurred. Saved at {output}")
