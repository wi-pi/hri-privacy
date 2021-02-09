from src.database import Database


class DatabaseWrapper:
    def __init__(self):
        self.DB = Database()

    def add_people(self, people):
        table = 'person'
        cols = ['person_id', 'threshold_low', 'threshold_high', 'aliases']
        for person_id, person in people.items():
            self.DB.insert(table, cols, (person_id,
                                         person.thresholds['low'],
                                         person.thresholds['high'],
                                         person.aliases))

        table = 'person_trust'
        cols = ['truster_id', 'trustee_id', 'trust']
        for person_id, person in people.items():
            for trustee, trust in person.relationships.items():
                self.DB.insert(table, cols, (person_id,
                                             trustee,
                                             trust))

    def add_information(self, data):
        table = 'information'
        cols = ['information_id', 'eavesdropping', 'datetime', 'sentiment_score', 'sentiment_magnitude', \
            'threshold_low', 'threshold_high']
        self.DB.insert(table, cols, (data['information_id'],
                                     data['eavesdropping'],
                                     data['timestamp'],
                                     data['sentiment'].score,
                                     data['sentiment'].magnitude,
                                     data['threshold_low'],
                                     data['threshold_high']))

    def add_topic(self, data):
        table = 'topic'
        cols = ['topic_id', 'name']
        self.DB.insert(table, cols, (data['topic_id'],
                                     data['name']))

    def add_person_information(self, information_id, listeners):
        table = 'person_information'
        cols = ['person_id', 'information_id']
        for person in listeners:
            self.DB.insert(table, cols, (person,
                                         information_id))

    def add_person_content(self, content, listeners, control_level):
        table = 'person_content'
        cols = ['person_id', 'content_id', 'control_level']
        for person in listeners:
            self.DB.insert(table, cols, (person,
                                         content,
                                         control_level))

    def add_person_topic(self, people, topics, topic_ids):
        table = 'person_topic'
        cols = ['person_id', 'topic_id', 'score']
        for key, person in people.items():
            for name, score in topics.items():
                self.DB.insert(table, cols, (person.person_id,
                                             topic_ids[name],
                                             score))

    def add_information_topic(self, information_id, topics):
        table = 'information_topic'
        cols = ['information_id', 'topic_id']
        for topic in topics:
            self.DB.insert(table, cols, (information_id,
                                         topic))

    def add_content(self, data):
        table = 'content'
        cols = ['speaker_id', 'information_id', 'addressee_id', 'position', 'text_content', 'emotion', \
            'sentiment_score', 'sentiment_magnitude', 'privacy_score', 'datetime', 'intent', 'privacy_indication']
        self.DB.insert(table, cols, (data['speaker_id'],
                                     data['information_id'],
                                     data['addressee_id'],
                                     data['position'],
                                     data['text_content'],
                                     data['emotion'],
                                     data['sentiment'].score,
                                     data['sentiment'].magnitude,
                                     data['privacy_score'],
                                     data['datetime'],
                                     data['intent'],
                                     data['privacy_indication']))

    def add_entity(self, data):
        table = 'entities'
        cols = ['content_id', 'representation', 'mention_text', 'type', 'mention_type', 'wiki_url', \
            'knowledge_mid', 'salience_score', 'sentiment_score', 'sentiment_magnitude']
        self.DB.insert(table, cols, (data['content_id'],
                                     data['representation'],
                                     data['mention_text'],
                                     data['type'],
                                     data['mention_type'],
                                     data['wiki_url'],
                                     data['knowledge_mid'],
                                     data['salience_score'],
                                     data['sentiment'].score,
                                     data['sentiment'].magnitude))

    def get_last_content(self):
        return self.DB.do('SELECT content_id FROM content ORDER BY content_id DESC LIMIT 1')[0]

    def get_many_from_many(self, col_id, flag=''):
        """
        Gets ___ from ___
        """
        if flag == 'person_topic':
            data = self.DB.select('person_topic', ['person_id', 'score'], ['topic_id'], ([col_id],))
        elif flag == 'topic_person':
            data = self.DB.select('person_topic', ['topic_id', 'score'], ['person_id'], ([col_id],))
        elif flag == 'information_topic':
            data = self.DB.select('information_topic', ['information_id'], ['topic_id'], ([col_id],))
        elif flag == 'topic_information':
            data = self.DB.select('information_topic', ['topic_id'], ['information_id'], ([col_id],))
        elif flag == 'person_information':
            data = self.DB.select('person_information', ['person_id'], ['information_id'], ([col_id],))
        elif flag == 'information_person':
            data = self.DB.select('person_information', ['information_id'], ['person_id'], ([col_id],))
        elif flag == 'person_truster':
            data = self.DB.select('person_trust', ['trustee_id', 'trust'], ['truster_id'], ([col_id],))
        elif flag == 'person_trustee':
            data = self.DB.select('person_trust', ['truster_id', 'trust'], ['trustee_id'], ([col_id],))
        elif flag == 'person_content':
            data = self.DB.select('person_content', ['person_id', 'control_level'], ['content_id'], ([col_id],))
        elif flag == 'content_person':
            data = self.DB.select('person_content', ['content_id', 'control_level'], ['person_id'], ([col_id],))

        else:
            raise Exception('Need to select a flag')
        return data
        
    def get_many_from_one(self, col_id, flag=''):
        if flag == 'speaker_person':
            data = self.DB.select('content', ['content_id'], ['speaker_id'], ([col_id],))
        elif flag == 'addressee_person':
            data = self.DB.select('content', ['content_id'], ['addressee_id'], ([col_id],))
        elif flag == 'content_information':
            data = self.DB.select('content', ['content_id'], ['information_id'], ([col_id],))
        elif flag == 'entity_content':
            data = self.DB.select('entities', ['entity_id'], ['content_id'], ([col_id],))
        else:
            raise Exception('Need to select a flag')
        return data

    def get_all(self, flag=''):
        if flag == 'content':
            data = self.DB.select('content', ['*'])
        elif flag == 'information':
            data = self.DB.select('information', ['*'])
        elif flag == 'person':
            data = self.DB.select('person', ['*'])
        elif flag == 'topic':
            data = self.DB.select('topic', ['*'])
        elif flag == 'entities':
            data = self.DB.select('entities', ['*'])
        else:
            raise Exception('Need to select a flag')
        return data

    def get_information_from_content(self, content_id):
        return self.DB.select('content', ['information_id'], ['content_id'], ([content_id],))[0]
        
    def get_topic_scores(self, topic_id, person_id):
        return self.DB.select('person_topic', ['score'], ['topic_id', 'person_id'], (topic_id, [person_id]))

    def get_threshold(self, person_id):
        return self.DB.select('person', ['threshold_low', 'threshold_high'], ['person_id'], ([person_id],))[0]

    def get_sentiments(self, content_id):
        entities = self.get_many_from_one(content_id, 'entity_content')
        information_id = self.get_information_from_content(content_id)
        c_score, c_magnitude = self.DB.select('content', ['sentiment_score', 'sentiment_magnitude'], ['content_id'], ([content_id],))[0]
        if entities is not None:
            e_sentiments = self.DB.select('entities', ['sentiment_score', 'sentiment_magnitude'], ['entity_id'], (entities,))
        else:
            e_sentiments = None
        i_score, i_magnitude = self.DB.select('information', ['sentiment_score', 'sentiment_magnitude'], ['information_id'], ([information_id],))[0]
        return c_score, c_magnitude, e_sentiments, i_score, i_magnitude

    def get_privacy_score(self, content_id):
        return self.DB.select('content', ['privacy_score'], ['content_id'], ([content_id],))

    def get_num_people(self, content_id):
        people =  self.get_many_from_many(content_id, 'person_content')
        return len(people)

    def get_person_id(self):
        return self.DB.select('person', ['person_id'])

    def get_relationships(self, content_id, person_id):
        trusts = self.get_many_from_many(person_id, 'person_truster')
        return trusts

    def get_information_detail(self, content_id):
        information_id = self.get_information_from_content(content_id)
        text = self.DB.select('content', ['text_content'], ['content_id'], ([content_id],))
        all_text = self.DB.select('content', ['text_content'], ['information_id'], ([information_id],))
        return text, all_text

    def get_privacy_indication(self, content_id):
        return self.DB.select('content', ['privacy_indication'], ['content_id'], ([content_id],))

    def get_emotion(self, content_id):
        return self.DB.select('content', ['emotion'], ['content_id'], ([content_id]),)

    def get_peoples_conversations(self, truster_id, trustee_id):
        text_content = []
        privacy_score = []
        control_level = []
        information_id = self.get_many_from_many(truster_id, 'information_person')
        if information_id is not None:
            for i in information_id:
                people = self.get_many_from_many(i, 'person_information')
                for p in people:
                    if p == trustee_id:
                        data = self.DB.select('content', ['text_content', 'privacy_score', 'content_id'], ['information_id'], ([i],))
                        for r in data:
                            text_content.append(r[0])
                            privacy_score.append(r[1])
                            control_level.append(self.DB.select('person_content', ['control_level'], ['content_id'], ([r[2]],)))
        return text_content, privacy_score, control_level

    def update_privacy(self, score, control_level, person_id, content_id):
        self.DB.update('content', ['privacy_score'], ['content_id'], ([score], [content_id]),)
        self.DB.update('person_content', ['control_level'], ['content_id', 'person_id'], ([control_level], [content_id], [person_id]))

    def update_trust(self, truster_id, trustee_id, trust):
        self.DB.update('person_trust', ['trust'], ['truster_id', 'trustee_id'], ([trust], [truster_id], [trustee_id]))

    def delete(self):
        self.DB.delete_all()

    def create(self):
        self.DB.create_all()