from src.rules import Rules

CONTENT_ID = 22
PERSON_ID = 6 # Misty


def test_coordinated():
    """
    UNFINISHED
    Evaluate when privacy boundaries are coordinated.
    """
    pass


def test_disjointed():
    """
    UNFINISHED
    Evaluate when privacy boundaries are unsynched.
    """
    pass


def test_contradiction():
    """
    UNFINISHED
    Evaluate when privacy boundary rules are contradictory.
    """
    pass


def test_ignore():
    """
    UNFINISHED
    Evaluate when privacy boundaries are ignored.
    """
    pass


def test_trust_updater():
    """
    Tests the functionality of the trust score updating mechanism.
    """
    weights = {
        'topic': 1,
        'sentiment': 1,
        'relationship': 1,
        'number_of_people': 1,
        'information_detail': 1,
    }
    r = Rules(weights)
    r.update_trust()


def test_enforce(content_id, person_id):
    """
    Tests the functionality of the privacy score rule enforcement mechanism.

    Keyword arguments:
    content_id -- The database row ID of the content in the conversation to be evaluated.
    person_id -- The database row ID of the person in the conversation to be evaluated.
    """
    weights = {
        'topic': 1,
        'sentiment': 1,
        'relationship': 1,
        'number_of_people': 1,
        'information_detail': 1,
    }
    r = Rules(weights)
    r.enforce(content_id, person_id)


def test_enforce_loop():
    """
    Tests the privacy score rule enforcement for a range of content_id's.
    """
    for i in range(1, 27):
        print('Content ID: {}'.format(i))
        print('---------------------------')
        test_enforce(i, 6)


if __name__ == '__main__':
    test_enforce(CONTENT_ID, PERSON_ID)
    test_enforce_loop()
    test_trust_updater()
