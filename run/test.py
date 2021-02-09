from src.rules import Rules

CONTENT_ID = 22
PERSON_ID = 6 # Misty

def test_coordinated():
    """
    Evaluate when privacy boundaries are coordinated

    Keyword arguments:
    param -- description
    """

def test_disjointed():
    """
    Evaluate when privacy boundaries are unsynched

    Keyword arguments:
    param -- description
    """

def test_contradiction():
    """
    Evaluate when privacy boundary rules are contradictory

    Keyword arguments:
    param -- description
    """

def test_ignore():
    """
    Evaluate when privacy boundaries are ignored

    Keyword arguments:
    param -- description
    """

def test(content_id, person_id):
    weights = {
        'topic': 1,
        'sentiment': 1,
        'relationship': 1,
        'number_of_people': 1,
        'information_detail': 1,
    }
    r = Rules(weights)
    r.update_trust()
    # r.enforce(content_id, person_id)


def test_loop():
    for i in range(1, 27):
        print('Content ID: {}'.format(i))
        print('---------------------------')
        test(i, 6)


if __name__ == '__main__':
    test(CONTENT_ID, PERSON_ID)
    # test_loop()
