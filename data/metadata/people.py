class Person:
    """

    """
    def __init__(person_id=0,
                 aliases=[],
                 relationships={},
                 topics={},
                 thresholds={}):
        self.person_id = person_id
        self.aliases = aliases
        self.relationships = relationships
        self.topics = topics
        self.thresholds = thresholds


    def update_relationships(people, trust):
        for p, t in zip(people, trust):
            self.relationships[p] = trust


    def update_topics(topics, scores):
        for t, s in zip(topics, scores):
            self.topics[t] = s


    def update_thresholds(control_levels, thresholds):
        for c, t in zip(control_levels, thresholds):
            self.thresholds[c] = t


TOPICS = {
    0: 1.0,
    1: 0.1,
    2: 0.3,
    3: 0.3,
    4: 0.1,
    5: 0.4,
    6: 0.3,
    7: 0.7,
    8: 0.1,
    9: 0.2,
    10: 0.9,
    11: 0.2,
    12: 0.2,
    13: 0.2,
    14: 0.2,
    15: 0.3,
    16: 0.1,
    17: 0.2,
    18: 0.2,
    19: 0.1,
    20: 0.3,
    21: 0.3,
    22: 0.2,
    23: 1.0,
    24: 0.2,
    25: 0.1,
    26: 0.2,
}

PEOPLE = {
    1:Person(person_id=1,
           aliases=['alice'],
           relationships={
                2: 0.9,
                3: 0.5,
                4: 0.5,
                5: 0.1,
                6: 0.5,
           },
           topics=TOPICS,
           thresholds={
                'low': 0.2,
                'high': 0.7
           }),
    2:Person(person_id=2,
           aliases=['bob', 'robert', 'bobby'],
           relationships={
                1: 1.0,
                3: 0.5,
                4: 0.5,
                5: 0.2,
                6: 0.3,
           },
           topics=TOPICS,
           thresholds={
                'low': 0.3,
                'high': 0.6
           }),
    3:Person(person_id=3,
           aliases=['charlie', 'charles'],
           relationships={
                2: 0.5,
                1: 0.5,
                4: 0.8,
                5: 0.9,
                6: 1.0,
           },
           topics=TOPICS,
           thresholds={
                'low': 0.2,
                'high': 0.8
           }),
    4:Person(person_id=4,
           aliases=['daniel'],
           relationships={
                2: 0.3,
                3: 0.6,
                1: 0.8,
                5: 0.3,
                6: 0.6,
           },
           topics=TOPICS,
           thresholds={
                'low': 0.1,
                'high': 1.0
           }),
    5:Person(person_id=5,
           aliases=['eve', 'harapeco'],
           relationships={
                2: 0.0,
                3: 0.7,
                4: 0.5,
                1: 0.1,
                6: 0.2,
           },
           topics=TOPICS,
           thresholds={
                'low': 0.4,
                'high': 0.5
           }),
    6:Person(person_id=6,
           aliases=['misty', 'robot'],
           relationships={
                2: 0.4,
                3: 0.7,
                4: 0.9,
                5: 0.2,
                1: 0.5,
           },
           topics=TOPICS,
           thresholds={
                'low': 0.4,
                'high': 0.6
           })
          }
