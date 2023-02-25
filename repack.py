#!/usr/bin/env python3

import collections
import importlib
import json
import os
import re
import sys
import zipfile

meta_module = sys.argv[1]
metadata = importlib.import_module(f"works.{meta_module}")

page_regex = re.compile(metadata.page_regex)

repack_dir = meta_module
os.mkdirs(repack_dir, exist_ok=True)
with open(os.path.join(repack_dir, "details.json"), "w") as f:
    json.dump(metadata.details, f)

for num, vol in enumerate(metadata.volumes, 1):
    print(f"Volume {num}")
    with zipfile.ZipFile(vol) as volfile:
        if num == metadata.cover_volume:
            cover = volfile.read(metadata.cover_file)
            with open(os.path.join(repack_dir, "cover.jpg"), "wb") as f:
                f.write(cover)

        chapters = collections.defaultdict(list)
        for page in volfile.namelist():
            if not (matches := page_regex.match(page)):
                raise Exception(page)
            chapters[matches["chapter"]].append(page)

        for chapter, pages in chapters.items():
            chapter = chapter.lstrip("0").replace(metadata.subchapter_separator, ".")
            print(f"    Chapter {chapter}")

            fn = []
            if len(metadata.volumes) > 1:
                fn.append(f"Vol.{num}")
            fn.append(f"Ch.{chapter}")
            if title := metadata.toc.get(chapter):
                fn.append("-")
                fn.append(title)
            fn = " ".join(fn) + ".cbz"

            path = os.path.join(repack_dir, fn)
            with zipfile.ZipFile(path, "w") as chapfile:
                for page in pages:
                    data = volfile.read(page)
                    chapfile.writestr(
                        page,
                        data,
                        # Saves a little bit even though the pages are already
                        # compressed
                        compress_type=zipfile.ZIP_DEFLATED,
                    )
