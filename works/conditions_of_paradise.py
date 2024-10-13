# https://anilist.co/manga/41867/The-Conditions-of-Paradise/
# Nyaa source ID: 1231713

volumes = [
    "The Conditions of Paradise (2020) (Digital) (danke-Empire).cbz",
]

details = {
    "title": "The Conditions of Paradise",
    "author": "Morishima Akiko",
    "artist": "Morishima Akiko",
    "description": "Collection of the following stories:\n\n1. Rakuen no Jouken (The Conditions for Paradise)\nTwo adult women figuring out the boundaries in their relationship--is too much freedom a bad thing?\n\n2. Hoshi no Mukougawa (Beyond the Stars)\nChapter 1 prequel. It's about how Sarina and Sumi first became more than friends.\n\n3. Bathed in Sunlight Filtering Through the Trees\nA continuation of Sarina and Sumi's relationship.\n\n4. 20-Musumex30-Otome\nAbout an art prep school teacher who feels like she can't compare to her new 20-year-old girlfriend.\n\n5. The Opposite of \"Seme\" is \"Protector\"\nChapter 4 sequel. Keiko wants to take things further. There are two more stories in this series in the Lapis Lazuli Dream collection.\n\n6. We're Aiming For Love Now\nIt's about two women who love each other just as they are.\n\n7. Momo no Aji (Peach Taste)\nA girl struggles to convince the object of her affections to take her seriously.\n\n8. Sakurahime Hanafubuki (Princess Sakura, Showered With Blossoms )\nA story set in Japan's past about a cherry blossom that falls in love with a girl. The cherry blossom is granted a human body with the condition that if she nor the girl she loves are able to sacrifice everything for their love, her body will crumble away.\n\n9. Extra: Getting Cozy",
    "genre": [
        "Romance",
    ],
    "status": "2",
}

toc = {
    "8.5": "Afterword",
}

chapter_overrides = {}
for i in range(143, 149 + 1):
    chapter_overrides[(1, str(i))] = "8.5"

page_regex = r"^The Conditions of Paradise - c(?P<chapter>\d+) \(OShot\) - p(?P<page>[\dp-]+) (?:\[(?:Cover|ToC|Afterword)\] )?\[dig\] \[(?P<chap_title>.*)\] \[Seven Seas\] \[danke-Empire\] {HQ}\.jpg$"

cover_volume = 1
cover_file = "The Conditions of Paradise - c001 (OShot) - p000 [Cover] [dig] [The Conditions of Paradise] [Seven Seas] [danke-Empire] {HQ}.jpg"

subchapter_separator = "#"
