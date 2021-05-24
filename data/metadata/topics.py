from data.metadata.topic_list import ALL_TOPICS


TOPICS = {
    'Adult': 1.0,
    'Arts & Entertainment': 0.1,
    'Autos & Vehicles': 0.3,
    'Beauty & Fitness': 0.3,
    'Books & Literature': 0.1,
    'Business & Industrial': 0.4,
    'Computers & Electronics': 0.3,
    'Finance': 0.7,
    'Food & Drink': 0.1,
    'Games': 0.2,
    'Health': 0.9,
    'Hobbies & Leisure': 0.2,
    'Home & Garden': 0.2,
    'Internet & Telecom': 0.2,
    'Jobs & Education': 0.2,
    'Law & Government': 0.3,
    'News': 0.1,
    'Online Communities': 0.2,
    'People & Society': 0.2,
    'Pets & Animals': 0.1,
    'Real Estate': 0.3,
    'Reference': 0.3,
    'Science': 0.2,
    'Sensitive Subjects': 1.0,
    'Shopping': 0.2,
    'Sports': 0.1,
    'Travel': 0.2,
}

TOPIC_IDS = {
    'Adult': 1,
    'Arts & Entertainment': 2,
    'Autos & Vehicles': 3,
    'Beauty & Fitness': 4,
    'Books & Literature': 5,
    'Business & Industrial': 6,
    'Computers & Electronics': 7,
    'Finance': 8,
    'Food & Drink': 9,
    'Games': 10,
    'Health': 11,
    'Hobbies & Leisure': 12,
    'Home & Garden': 13,
    'Internet & Telecom': 14,
    'Jobs & Education': 15,
    'Law & Government': 16,
    'News': 17,
    'Online Communities': 18,
    'People & Society': 19,
    'Pets & Animals': 20,
    'Real Estate': 21,
    'Reference': 22,
    'Science': 23,
    'Sensitive Subjects': 24,
    'Shopping': 25,
    'Sports': 26,
    'Travel': 27,
}

for i in ALL_TOPICS:
    split = i.split('/')
    overview = split[1]
    if i not in TOPICS:
        TOPICS[i] = TOPICS[overview]
        TOPIC_IDS[i] = len(TOPIC_IDS.keys()) + 1
