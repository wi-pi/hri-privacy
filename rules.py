class Rules:
    self.RULES = {
        'topic': enforce_topic,
        'sentiment': enforce_sentiment,
        'relationship': enforce_relationship,
        'threshold': enforce_threshold,
        'indication': enforce_privacy_indication
    }
    def __init__(self, rules):
        self.rules = rules

    def enforce(self, data):
        for r in self.rules:
            self.RULES[r](data)
            
    def enforce_topic(data):
        """
        Enforces privacy based on conversation topics.

        Keyword arguments:
        param -- description
        """

    def enforce_sentiment(data):
        """
        Enforces privacy based on negative sentiments.

        Keyword arguments:
        param -- description
        """

    def enforce_relationship(data):
        """
        Enforces privacy based on relationship closeness.

        Keyword arguments:
        param -- description
        """

    def enforce_threshold(data):
        """
        Enforces privacy threshold rule based on:
            Number of people involved.
            How detailed information is.
            Relationship scores between people.

        Keyword arguments:
        param -- description
        """

    def enforce_privacy_indication(data):
        """
        description

        Keyword arguments:
        param -- description
        """
