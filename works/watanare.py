# https://anilist.co/manga/119650/Theres-No-Freaking-Way-Ill-be-Your-Lover-Unless/
# Nyaa source ID: 1687465, 1775294

volumes = [
    "There's No Freaking Way I'll Be Your Lover! Unless... v01 (2023) (Digital) (danke-Empire).cbz",
    "There's No Freaking Way I'll Be Your Lover! Unless... v02 (2023) (Digital) (danke-Empire).cbz",
    "There's No Freaking Way I'll Be Your Lover! Unless... v03 (2023) (Digital) (nao).cbz",
    "There's No Freaking Way I'll Be Your Lover! Unless... v04 (2024) (Digital) (nao).cbz",
]

details = {
    "title": "There's No Freaking Way I'll Be Your Lover! Unless...",
    "author": "Musshu, Mikami Teren",
    "artist": "Musshu",
    "description": "Renako Amaori is leaving her awkward and lonely junior high school life behind, determined to become a normal girl with normal friends in high school. Glamorous, confident Mai Ouzuka is Renako’s total opposite: wealthy, outgoing, and a literal fashion model. Against the odds, the two girls form an immediate connection. Renako thinks she may have found the best friend of her dreams…until Mai’s romantic confession sends her into a tailspin. Renako wants to prove to Mai that being BFFs is better than being girlfriends, but Mai is dead set on convincing Renako that they’re destined to be lovers. Let the love games begin!",
    "genre": [
        "Comedy",
        "Ecchi",
        "Romance",
    ],
    "status": 1
}

toc = {
}

chapter_overrides = {}
for i in range(184, 193 + 1):
    chapter_overrides[(1, str(i))] = "8.1"
for i in range(214, 223 + 1):
    chapter_overrides[(2, str(i))] = "17.1"
for i in range(223, 225 + 1):
    chapter_overrides[(3, str(i))] = "26.1"

page_regex = r"^There's No Freaking Way I'll Be Your Lover! Unless\.\.\. - c(?P<chapter>[\dx]+) \(v(?P<volume>\d\d)\) - p(?P<page>[\d-]+) (?:\[(?:Cover|Inside Cover|ToC|Afterword|Colophon|Omake)] )?\[dig] \[Seven Seas] \[(?:danke-Empire|nao)](?: {HQ})?\.(?:jpg|png)$"

cover_volume = 1
cover_file = "There's No Freaking Way I'll Be Your Lover! Unless... - c001 (v01) - p000 [Cover] [dig] [Seven Seas] [danke-Empire] {HQ}.jpg"

subchapter_separator = "x"
