"""Helper functions to keep images organized in the blog.

Features:
* Convert all images to @1x and @2x versions, sized for max column width.
* Create @1x and @2x thumbnails for the home page.
* Organize into separate assets folders.
* Various migration functions.

Usage:
1. Put hi-res "raw" images into the `_raw_images` directory.
2. Reference the image names in markdown files within `_posts`.
3. Run `python _compile_images.py` to put compiled imaged into `assets`.
4. Run `jekyll serve` to confirm images have loaded properly.
"""
import argparse
import os
from os.path import abspath, dirname, exists, join, splitext
import re
from shutil import copy2, rmtree
import subprocess

from PIL import Image, UnidentifiedImageError


ROOT = dirname(abspath(join(__file__, '..')))


def run(dry_run=False):
    """Compile images and move to the `assets` folder."""
    image_map = get_image_map()
    thumbnails = get_thumbnail_map()
    compile_images(image_map, thumbnails, dry_run)


def get_image_map():
    """Cross-reference `_raw_images` and `_posts` to build a map.

    Determines where to move compiled images to keep the
    `assets` directory clean.

    Return a dict with image filenames as keys and post filenames as values.
    """
    image_names = os.listdir(join(ROOT, '_raw_images'))
    image_map = {}
    front_matter = re.compile(r"^---\n(.+\n)+---\n")
    for file in os.listdir(join(ROOT, '_posts')):
        post_name = splitext(file)[0]
        with open(join(ROOT, '_posts', file)) as in_file:
            content = in_file.read()
        content = front_matter.sub('', content)
        for image_name in image_names:
            if image_name in content:
                image_map[image_name] = post_name
    return image_map


def get_thumbnail_map():
    """Identify thumbnails for compilation.

    Fills `assets/index` with lightweight thumbnails for the home page.

    Return a dict with image filenames as keys and post filenames as values.
    """
    thumbnail_regex = re.compile(r'thumbnail: (.*)')
    thumbnails = []
    for file in os.listdir(join(ROOT, '_posts')):
        # post_name = splitext(file)[0]
        with open(join(ROOT, '_posts', file)) as in_file:
            content = in_file.read()
        thumbnails.append(thumbnail_regex.search(content).group(1))
    return thumbnails


def compile_images(image_map, thumbnails, dry_run=False):
    """Compile images into multiple resolutions and copy to `assets`."""
    tmp_path = join(ROOT, '_raw_images/tmp')
    os.makedirs(tmp_path, exist_ok=True)
    for image, post in image_map.items():
        dst = join(ROOT, 'assets', post)
        if exists(join(dst, image)):
            continue
        os.makedirs(dst, exist_ok=True)
        paths = compile_image(image)
        if not dry_run:
            for path in paths:
                copy2(path, dst)
        if image in thumbnails:
            paths = compile_thumbnail(image)
            if not dry_run:
                for path in paths:
                    copy2(path, join(ROOT, 'assets/index'))
    rmtree(tmp_path)


def compile_image(image):
    """Downsize an image to match maximum webpage width.

    Generates vanilla and @2x versions to support retina screens.
    """
    print(f"Processing {image}")
    raw_path = join(ROOT, '_raw_images')
    tmp_path = join(ROOT, '_raw_images/tmp')

    # Make a non-retina image sized to max blog width
    # Scale down to 720px max width, but don't scale up if lower res
    # https://stackoverflow.com/a/14390892
    regular = (r"convert -resize 720x720\> "
               "+repage -auto-orient -strip -interlace Plane -quality 80 "
               f'"{join(raw_path, image)}" "{join(tmp_path, image)}"')
    subprocess.Popen(regular, shell=True).wait()

    # If the source image offers a higher resolution, use it for 2x retina
    image_width = Image.open(join(raw_path, image)).size[0]
    if image_width > 720:
        name, ext = splitext(image)
        hi_res_name = f'{name}@2x{ext}'
        hi_res = (r"convert -resize 1440x1440\> "
                  "+repage -auto-orient -strip -interlace Plane -quality 80 "
                  f'"{join(raw_path, image)}" "{join(tmp_path, hi_res_name)}"')
        subprocess.Popen(hi_res, shell=True).wait()

    output = [join(tmp_path, image)]
    if image_width > 720:
        output.append(join(tmp_path, hi_res_name))
    return output


def compile_thumbnail(image):
    """Downsize an image to thumbnail size.

    Generates vanilla and @2x versions to support retina screens.
    """
    print(f"Processing {image} thumbnail")
    raw_path = join(ROOT, '_raw_images')
    tmp_path = join(ROOT, '_raw_images/tmp')

    # Make a small thumbnail image for the main page
    w, h = 350, 200
    thumbnail = (f"convert -resize {w}x{h}^ -gravity Center -crop {w}x{h}+0+0 "
                 "+repage -auto-orient -strip -interlace Plane -quality 80 "
                 f'"{join(raw_path, image)}" "{join(tmp_path, image)}"')
    subprocess.Popen(thumbnail, shell=True).wait()

    w, h = w * 2, h * 2
    name, ext = splitext(image)
    hi_res_name = f'{name}@2x{ext}'
    hi_res = (f"convert -resize {w}x{h}^ -gravity Center -crop {w}x{h}+0+0 "
              "+repage -auto-orient -strip -interlace Plane -quality 80 "
              f'"{join(raw_path, image)}" "{join(tmp_path, hi_res_name)}"')
    subprocess.Popen(hi_res, shell=True).wait()

    return [join(tmp_path, image), join(tmp_path, hi_res_name)]


def update_image_paths(image_map):
    """Replace image references with absolute paths.

    This replaces {image} with /assets/{post}/{image}. Used as a one-off
    migration script.
    """
    for file in os.listdir(join(ROOT, '_posts')):
        print(f"Updating image paths in {file}")
        post_name = splitext(file)[0]
        path = join(ROOT, '_posts', file)
        with open(path) as in_file:
            content = in_file.read()
        images = [i for i, p in image_map.items() if p == post_name]
        for image in images:
            content = content.replace(f'image: {image}',
                                      f'image: /assets/{post_name}/{image}')
        with open(path, 'w') as out_file:
            out_file.write(content)


def upscale_old_images():
    """Increase the size of 600px-width images to 720px width.

    Replaces old column width with new one. Used as a one-off migration
    script.
    """
    raw_path = join(ROOT, '_raw_images')
    tmp_path = join(ROOT, '_raw_images/tmp')
    os.makedirs(tmp_path, exist_ok=True)

    image_names = os.listdir(join(ROOT, '_raw_images'))
    for image in image_names:
        try:
            image_width = Image.open(join(raw_path, image)).size[0]
        except (UnidentifiedImageError, IsADirectoryError):
            continue
        if image_width == 600:
            print(f"Upscaling {image}")
            upscale = (r"convert -resize 720x720 "
                       f'"{join(raw_path, image)}" "{join(tmp_path, image)}"')
            subprocess.Popen(upscale, shell=True).wait()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert raw images into "
                                     "multiple resolutions of smaller images "
                                     "for faster site loading.")
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help="Test without copying to assets directory.")
    args = parser.parse_args()
    run(dry_run=args.dry_run)
