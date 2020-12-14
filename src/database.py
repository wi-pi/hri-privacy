import psycopg2
from psycopg2.sql import SQL, Identifier
from datetime import datetime

import config


class Database:

    def __init__(self):
        self.conn = psycopg2.connect(dbname=config.DB_NAME,
                                     user=config.USERNAME,
                                     password=config.PASSWORD,
                                     host=config.HOSTNAME)

    def add_people(self, people):
        """
        description

        Keyword arguments:
        param -- description
        """
        cur = self.conn.cursor()
        for person in people:
            cur.execute(SQL('INSERT INTO person (person_id, aliases) \
                VALUES ({}, {})').format(person.person_id, person.aliases))
        for person in people:
            for p, trust in person.relationships.items():
                cur.execute(SQL('INSERT INTO person_trust (truster_id, trustee_id, trust) \
                 VALUES ({}, {}, {})').format(person.person_id, p, trust))
        cur.close()

    def add_information(self, topics, eavesdropping, timestamp, sentiment):
        """
        description

        Keyword arguments:
        param -- description
        """
        cur = self.conn.cursor()
        cur.execute(SQL('INSERT INTO information (topics, eavesdropping, datetime, sentiment_score, sentiment_magnitude) \
            VALUES ({}, {}, {}, {}, {})').format(topics, eavesdropping, timestamp, sentiment.score, sentiment.magnitude))
        cur.close()

    def add_person_information(self, conversation, listeners):
        """
        description

        Keyword arguments:
        param -- description
        """
        cur = self.conn.cursor()
        for person in listeners:
            cur.execute(SQL('INSERT INTO person_information (person_id, information_id) \
                VALUES ({}, {})').format(person, conversation))
        cur.close()

    def add_person_content(self, content, listeners):
        """
        description

        Keyword arguments:
        param -- description
        """
        cur = self.conn.cursor()
        for person in listeners:
            cur.execute(SQL('INSERT INTO person_content (person_id, content_id) \
                VALUES ({}, {})').format(person, content))
        cur.close()

    def add_content(self, data):
        """
        description

        Keyword arguments:
        param -- description
        """
        cur = self.conn.cursor()

        cur.execute(SQL('INSERT INTO content (speaker_id, information_id, addressee_id, position, text_content, emotion, \
            sentiment_score, sentiment_magnitude, privacy_score, datetime, intent, privacy_indication) \
            VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})').format(data['speaker_id'],
                                                                             data['information_id'],
                                                                             data['addressee_id'],
                                                                             data['position'],
                                                                             data['text_content'],
                                                                             data['emotion'],
                                                                             data['sentiment_score'],
                                                                             data['sentiment_magnitude'],
                                                                             data['privacy_score'],
                                                                             data['datetime'],
                                                                             data['intent'],
                                                                             data['privacy_indication']))
        cur.close()

    def add_entity(self, data):
        """
        description

        Keyword arguments:
        param -- description
        """
        cur = self.conn.cursor()

        cur.execute(SQL('INSERT INTO entities (content_id, representation, mention_text, type, mention_type, wiki_url, \
            knowledge_mid, currency, value, salience_score, sentiment_score, sentiment_magnitude) \
            VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})').format(data['content_id'],
                                                                             data['representation'],
                                                                             data['mention_text'],
                                                                             data['type'],
                                                                             data['mention_type'],
                                                                             data['wiki_url'],
                                                                             data['knowledge_mid'],
                                                                             data['currency'],
                                                                             data['value'],
                                                                             data['salience_score'],
                                                                             data['sentiment_score'],
                                                                             data['sentiment_magnitude']))
        cur.close()

    def update_(self, ):
        """
        description

        Keyword arguments:
        param -- description
        """


    def get_(self, ):
        """
        description

        Keyword arguments:
        param -- description
        """

