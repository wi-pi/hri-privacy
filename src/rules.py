from src.db_wrapper import DatabaseWrapper
from data.metadata.people import PEOPLE

# TODO: remove the circular dependency of the relationship rule.


DEFAULT_WEIGHTS = {
    'topic': 1,
    'sentiment': 1,
    'relationship': 1,
    'number_of_people': 1,
    'information_detail': 1,
}


class Rules:
    """
    The rule enforcement class which updates the privacy score based on a set of rules and weights.
    """
    def __init__(self, rules=DEFAULT_WEIGHTS):
        self.RULES = {
            'topic': self.enforce_topic,
            'sentiment': self.enforce_sentiment, 
            'relationship': self.enforce_relationship,
            'number_of_people': self.enforce_number_of_people,
            'information_detail': self.enforce_information_detail,
            'privacy_indication': self.enforce_privacy_indication,
            'emotion': self.enforce_emotion
        }
        self.rules = rules
        self.DB = DatabaseWrapper()

    def enforce(self, content_id, person_id):
        """
        Enforces the set of weighted rules with denoted in self.rules.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        scores = []
        weights = []
        for r, w in self.rules.items():
            s = self.RULES[r](content_id, person_id)
            print('{} - {}\n'.format(s, r))
            if s is not None:
                scores.append(s)
                weights.append(w)
        self.update_privacy_level(content_id, person_id, scores, weights)

    def update_privacy_level(self, content_id, person_id, scores, weights):
        """
        

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        scores -- The list of scores computed within each rule.
        weights -- The list of weights associated with each rule.
        """
        threshold_low, threshold_high = self.DB.get_threshold(person_id)
        avg = 0
        for s, w in zip(scores, weights):
            avg += (s * w)
        avg /= len(scores)
        if avg < threshold_low:
            control = 'low'
        elif avg > threshold_high:
            control = 'high'
        else:
            control = 'moderate'
        print('Control level: {} | Privacy score: {} | Lower threshold: {} | High threshold: {}'.format(control, avg, threshold_low, threshold_high))
        self.DB.update_privacy(avg, control, person_id, content_id)

    def update_trust(self):
        """
        Updates trust score based on:
            Number of conversations had with each other.
            Level of detail of conversations.
            Privacy level of conversations.
        """
        people = self.DB.get_person_id()
        for p1 in people:
            for p2 in people:
                if p1 != p2:
                    text_content, privacy_score, control_level = self.DB.get_peoples_conversations(p1, p2)
                    detail = 0
                    privacy = 0
                    conversations = 0
                    total = len(text_content)
                    for i, t in enumerate(text_content):
                        detail += len(t) / total
                        if privacy_score[i] >= 0:
                            privacy += privacy_score[i] / total
                        if control_level[i] == 'low':
                            conversations += 0 / total
                        elif control_level[i] == 'moderate':
                            conversations += 0.5 / total
                        elif control_level[i] == 'high':
                            conversations += 1 / total
                    if detail < 100:
                        score = 0
                    elif detail < 500:
                        score = 0.5
                    else:
                        score = 1
                    privacy /= 3
                    print('Trust score: {} | Detail score: {} | Conversation score: {} | Privacy score: {}'.format(trust, score, conversations, privacy))
                    trust = score + conversations + privacy
                    self.DB.update_trust(p1, p2, trust)

    def enforce_topic(self, content_id, person_id):
        """
        Enforces privacy threshold rule based on:
            Conversation topic thresholds.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        information_id = self.DB.get_information_from_content(content_id)
        topic_id = self.DB.get_many_from_many(information_id, flag='topic_information')
        scores = self.DB.get_topic_scores(topic_id, person_id)
        average = 0
        for score in scores:
            average += score
        average /= len(scores)
        return average

    def enforce_sentiment(self, content_id, person_id):
        """
        Enforces privacy threshold rule based on:
            Strong negative sentiments.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        c_score, c_magnitude, e_sentiments, i_score, i_magnitude = self.DB.get_sentiments(content_id)
        score = ((1 - i_score) * i_magnitude) + (2 * (1 - c_score) * c_magnitude)
        temp_score = 0
        if e_sentiments is not None:
            for e in e_sentiments:
                temp_score += (1 - e[0]) * e[1] / len(e_sentiments)
        score = (score + temp_score)
        score /= 20
        return score

    def enforce_relationship(self, content_id, person_id):
        """
        Enforces privacy threshold rule based on:
            Relationship closeness and scores between people.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        trusts = self.DB.get_relationships(content_id, person_id)
        score = 0
        for i in trusts:
            score += (i[1])
        score /= len(trusts)
        return score

    def enforce_number_of_people(self, content_id, person_id):
        """
        Enforces privacy threshold rule based on:
            Number of people involved.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        num_people = self.DB.get_num_people(content_id)
        if num_people < 3:
            score = 1
        elif num_people < 6:
            score = 0.5
        else:
            score = 0
        return score      

    def enforce_information_detail(self, content_id, person_id):
        """
        Enforces privacy threshold rule based on:
            How detailed information is.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        text, all_text = self.DB.get_information_detail(content_id)
        detail = len(text[0])
        temp_detail = 0
        for i in all_text:
            temp_detail += len(i) / len(all_text)
        detail += temp_detail / 2
        detail /= 2
        if detail < 100:
            score = 0
        elif detail < 500:
            score = 0.5
        else:
            score = 1
        return score

    def enforce_privacy_indication(self, content_id, person_id):
        """
        UNFINISHED
        Enforces privacy threshold rule based on:
            Privacy indication phrases.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        indication = self.DB.get_privacy_indication(content_id)
        if indication != 'none':
            return 1
        else:
            return None

    def enforce_emotion(self, content_id, person_id):
        """
        UNFINISHED
        Enforces privacy threshold rule based on:
            Strong emotional displays.

        Keyword arguments:
        content_id -- The database row ID of the content in the conversation to be evaluated.
        person_id -- The database row ID of the person in the conversation to be evaluated.
        """
        emotion = self.DB.get_emotion(content_id)
        return None
