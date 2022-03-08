from data.metadata.topics import TOPICS


class Person:
    """
    The class which represents people, their topic sensitivity, and their relationships.
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
        """
        UNUSED
        """
        for p, t in zip(people, trust):
            self.relationships[p] = trust

    def update_topics(self, topics, scores):
        """
        UNUSED
        """
        for t, s in zip(topics, scores):
            self.topics[t] = s

    def update_thresholds(self, control_levels, thresholds):
        """
        UNUSED
        """
        for c, t in zip(control_levels, thresholds):
            self.thresholds[c] = t


def get_person(people, alias):
    """
    Finds a person ID using the person's alias.

    Keyword arguments:
    people -- The dictionary of all people.
    alias -- The alias to search for.
    """
    for i, person in people.items():
        if alias in person.aliases:
            return person.person_id
    return None
