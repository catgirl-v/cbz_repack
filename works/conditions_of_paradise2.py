# https://anilist.co/manga/85231/The-Conditions-of-Paradise-Our-First-Time/
# Nyaa source ID: 1321116

volumes = [
    "The Conditions of Paradise - Our First Time (2020) (Digital) (danke-Empire).cbz",
]

details = {
    "title": "The Conditions of Paradise: Our First Time",
    "author": "Morishima Akiko",
    "artist": "Morishima Akiko",
    "description": "Hajimete, Kanojo to., by Morishima Akiko-sensei, takes a look back at the origins of some of our favorite couples from her previous works.\n\nFirst we look back at Rakuen no Joken. For Sarina and Sumi we learn how they got together and why they’ve never really been a steady item. The series ends as Sarina realizes that Sumi moving in isn’t the life she wants, but travelling the world together with her is.\n\nShinobu and Lalaa have been living together for a while and Lalaa is inexpressibly happy. But, as she reminisces about how they got together, she misses, just a little, the crybaby Shinobu of her youth. We then move on to Sayaka and Ruri from Ruri-iro Yume. Sayaka’s dream has changed since we first met her, but she thinks it’s okay – and so do we.\n\nAnd last, we meet up once again with Mitsuki and Kaoru from Renai Joshika. With them, we travel back into their school years, how they met, became friends, became lovers and what went on between them during their first time dating.",
    "genre": [
        "Romance",
    ],
    "status": "2",
}

toc = {
    "8.5": "Afterword",
    "8.6": "Extra",
}

chapter_overrides = {}
for i in range(146, 147 + 1):
    chapter_overrides[(1, str(i))] = "8.5"
for i in range(148, 153 + 1):
    chapter_overrides[(1, str(i))] = "8.6"

page_regex = r"^The Conditions of Paradise - Our First Time - c(?P<chapter>\d+) \(OShot\) - p(?P<page>[\dp-]+) (?:\[(?:Cover|ToC|Omake|Afterword)\] )?\[dig\] \[(?P<chap_title>.*)\] \[Seven Seas\] \[danke-Empire\] {HQ}\.jpg$"

cover_volume = 1
cover_file = "The Conditions of Paradise - Our First Time - c001 (OShot) - p000 [Cover] [dig] [The Conditions of Paradise - Side A] [Seven Seas] [danke-Empire] {HQ}.jpg"

subchapter_separator = "#"
