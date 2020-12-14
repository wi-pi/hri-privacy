from data.metadata.topics import TOPICS


class Person:
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
