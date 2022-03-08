class Information:
    """
    Class for conversations which contains hard-coded topics, speakers, listeners, timestamps.
    """
    def __init__(self, speakers, listeners, topics, timestamps, location):
        self.speakers = speakers
        self.listeners = listeners
        self.topics = topics
        self.timestamps = timestamps
        self.location = location