from data.metadata.topics import TOPICS


class Person:
    """

    """
    def __init__(self, 
                 person_id=0,
                 aliases=[],
                 relationships={},
                 topics={},
                 thresholds={}):
        self.person_id = person_id
        self.aliases = aliases
        self.relationships = relationships
        self.topics = topics
        self.thresholds = thresholds

    def update_relationships(self, people, trust):
        for p, t in zip(people, trust):
            self.relationships[p] = trust

    def update_topics(self, topics, scores):
        for t, s in zip(topics, scores):
            self.topics[t] = s

    def update_thresholds(self, control_levels, thresholds):
        for c, t in zip(control_levels, thresholds):
            self.thresholds[c] = t


def get_person(people, alias):
    for person in people:
        if alias in person.aliases:
            return person.person_id
    return None


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
