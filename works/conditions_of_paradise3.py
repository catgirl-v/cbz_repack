# https://anilist.co/manga/47908/The-Conditions-of-Paradise-Azure-Dream/
# Nyaa source ID: 1333287

volumes = [
    "The Conditions of Paradise - Azure Dreams (2021) (Digital) (danke-Empire).cbz",
]

details = {
    "title": "The Conditions of Paradise: Azure Dream",
    "author": "Morishima Akiko",
    "artist": "Morishima Akiko",
    "description": "1. Ruriiro no Yume (瑠璃色の夢, Azure Dream)\nA sweet story about two OLs named Mikuni and Ruri. Ruri is an 'ordinary woman' at the age of 28, dreaming of getting married and having a child named after a gemstone like she is—that is, until Mikuni and she sleep together one night after drinking.\n2. Princess of the Stars (星のお姫様)\nTakes a look at the realities of being in a relationship.\n3. Honey & Mustard (ハニー&マスタード)\n4. Nostalgia (追憶)\n5. Virgin Season (20乙女の季節)\nThe next story in the 20-Musumex30-Otome series. Emi and Keiko have trouble finding time to spend together.\n6. Mangetsu no Yoru ni wa (満月の夜には, On a Night When the Moon is Full)\nKeiko and Emi go on a trip together.\n7. Soft-Boiled Fujoshi (半熟腐女子, Hanjuku Joshi side story)\n\"Soft-Boiled Fujoshi\" is about a minor character from Hanjuku Joshi. Moe is more important to fujoshi than love is... or is it?",
    "genre": [
        "Romance",
        "Slice of Life",
    ],
    "status": "2",
}

toc = {
    "7.5": "Afterword",
}

chapter_overrides = {}
for i in range(148, 151 + 1):
    chapter_overrides[(1, str(i))] = "7.5"

page_regex = r"^The Conditions of Paradise - Azure Dreams - c(?P<chapter>\d+) \(OShot\) - p(?P<page>[\dp-]+) (?:\[(?:Cover|ToC|Omake|Afterword)\] )?\[dig\] \[(?P<chap_title>.*)\] \[Seven Seas\] \[danke-Empire\] {HQ}\.jpg$"

cover_volume = 1
cover_file = "The Conditions of Paradise - Azure Dreams - c001 (OShot) - p000 [Cover] [dig] [Azure Dreams] [Seven Seas] [danke-Empire] {HQ}.jpg"

subchapter_separator = "#"
