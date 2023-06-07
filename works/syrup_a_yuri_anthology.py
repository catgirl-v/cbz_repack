# https://anilist.co/manga/111969/Syrup-A-Yuri-Anthology/
# https://anilist.co/manga/146507/Syrup-A-Yuri-Anthology-Vol-2/
# https://anilist.co/manga/146508/Syrup-A-Yuri-Anthology-Vol-3/
# https://anilist.co/manga/146509/Syrup-A-Yuri-Anthology-Vol-4/
# Nyaa source ID: 1378034, 1535750

volumes = [
    "Syrup - A Yuri Anthology v01 (2020) (Digital) (danke-Empire).cbz",
    "Syrup - A Yuri Anthology v02 (2020) (Digital) (danke-Empire).cbz",
    "Syrup - A Yuri Anthology v03 (2021) (Digital) (danke-Empire).cbz",
    "Syrup - A Yuri Anthology v04 (2022) (Digital) [nao].cbz",
]

details = {
    "title": "Syrup: A Yuri Anthology",
    "author": "Various",
    "artist": "Various",
    "description": "",
    "genre": [
        "Drama",
        "Romance",
        "Slice of Life",
        "Ecchi"
    ],
    "status": 1
}

toc = {
}

page_regex = r"^Syrup - A Yuri Anthology - c(?P<chapter>\d+) \(v(?P<volume>\d\d)\) - p(?P<page>[\d-]+) (?:\[(?:Cover|ToC|Afterword)] )?\[dig] \[(?P<chap_title>.+?)] \[Seven Seas] \[(?:danke-Empire|nao)] {HQ}\.jpg$"

cover_volume = 1
cover_file = "Syrup - A Yuri Anthology - c001 (v01) - p000 [Cover] [dig] [One AM at the Laundromat] [Seven Seas] [danke-Empire] {HQ}.jpg"

subchapter_separator = "."
