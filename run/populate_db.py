from src.natural_language import Google_NLP
from src.db_wrapper import DatabaseWrapper
from data.metadata.conversation1 import INFO1
from data.metadata.conversation2 import INFO2
from data.metadata.conversation3 import INFO3
from data.metadata.people import PEOPLE
from data.metadata.topics import TOPICS, TOPIC_IDS
from src.people import get_person
import os


CONVERSATION = 3
db = DatabaseWrapper()
db.delete()
db.create()
path = os.path.join('data', 'conversation{}'.format(CONVERSATION))
text = ''
texts = []
for num, file in enumerate(os.listdir(path)):
    with open(os.path.join(path, '{}.txt'.format(num + 1)), 'r') as infile:
        t = infile.read()
        text += t
        texts.append(t)

information = {}
contents = []
listeners = []
speakers = {}

for p in INFO1.listeners:
    listeners.append(get_person(PEOPLE, p))
for i, p in INFO1.speakers.items():
    speakers[i] = get_person(PEOPLE, p)

db.add_people(PEOPLE)

nlp = Google_NLP(text)
sentiment = nlp.get_sentiment()
information['information_id'] = CONVERSATION
# information['topics'] = INFO1.topics
information['eavesdropping'] = False
information['timestamp'] = INFO1.timestamps[1]
information['sentiment'] = sentiment
information['threshold_low'] = -1
information['threshold_high'] = -1

db.add_information(information)
db.add_person_information(CONVERSATION, listeners)

for name, val in TOPICS.items():
    topic = {}
    topic['name'] = name
    topic['topic_id'] = TOPIC_IDS[name]
    db.add_topic(topic)
db.add_person_topic(PEOPLE, TOPICS, TOPIC_IDS)


topic_ids = []
topics = nlp.get_topic()
for i in topics.categories:
    topic_ids.append(TOPIC_IDS[i.name])
print(topic_ids)

db.add_information_topic(CONVERSATION, topic_ids)
for i, t in enumerate(texts):
    content = {}
    print(t)
    nlp.update_document(t)
    entities = nlp.get_entity_sentiment()
    content['sentiment'] = nlp.get_sentiment()
    print(content['sentiment'])
    content['datetime'] = INFO1.timestamps[i + 1]
    content['position'] = i + 1
    content['speaker_id'] = speakers[i + 1]
    content['information_id'] = CONVERSATION
    content['addressee_id'] = -1
    content['text_content'] = t
    content['emotion'] = 'none'
    content['privacy_score'] = -1
    content['intent'] = 'none'
    content['privacy_indication'] = 'none'

    db.add_content(content)
    content_id = db.get_last_content()
    db.add_person_content(content_id, listeners, 'none')
    
    for e in entities:
        e['content_id'] = content_id
        db.add_entity(e)

