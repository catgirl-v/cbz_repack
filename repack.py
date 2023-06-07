#!/usr/bin/env python3

import collections
import dataclasses
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
os.makedirs(repack_dir, exist_ok=True)
with open(os.path.join(repack_dir, "details.json"), "w") as f:
    json.dump(metadata.details, f)

@dataclasses.dataclass
class Chapter:
    title: str = None
    pages: list[str] = dataclasses.field(default_factory=list)

for vol_num, vol_fn in enumerate(metadata.volumes, 1):
    print(f"Volume {vol_num}")
    with zipfile.ZipFile(vol_fn) as volfile:
        if vol_num == metadata.cover_volume:
            cover = volfile.read(metadata.cover_file)
            with open(os.path.join(repack_dir, "cover.jpg"), "wb") as f:
                f.write(cover)

        chapters = collections.defaultdict(Chapter)
        for page in volfile.namelist():
            if not (matches := page_regex.match(page)):
                raise Exception(page)
            matches = matches.groupdict()
            chapter = chapters[matches["chapter"]]
            chapter.pages.append(page)
            if not chapter.title:
                if title := matches.get("chap_title"):
                    chapter.title = title

        for chap_num, chapter in chapters.items():
            chap_num = chap_num.lstrip("0").replace(metadata.subchapter_separator, ".")
            print(f"    Chapter {chap_num}")

            fn = []
            if len(metadata.volumes) > 1:
                fn.append(f"Vol.{vol_num}")
            fn.append(f"Ch.{chap_num}")
            if title := metadata.toc.get(chap_num, chapter.title):
                fn.append("-")
                fn.append(title)
            fn = " ".join(fn) + ".cbz"

            path = os.path.join(repack_dir, fn)
            with zipfile.ZipFile(path, "w") as chapfile:
                for page in chapter.pages:
                    data = volfile.read(page)
                    chapfile.writestr(
                        page,
                        data,
                        # Saves a little bit even though the pages are already
                        # compressed
                        compress_type=zipfile.ZIP_DEFLATED,
                    )
