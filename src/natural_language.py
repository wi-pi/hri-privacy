import os
from google.cloud import language_v1
import textrazor as tr
from data import config


tr.api_key = config.TEXTRAZOR_KEY
manager = tr.DictionaryManager()


class Google_NLP:
    """
    Google natural language API class. Can be used to get metadata such as entities, sentiments, and topics from a specified document.
    """
    def __init__(self, text):
        self.client = language_v1.LanguageServiceClient()
        self.language = "en"

        print("Text: {}".format(text))
        self.document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language=self.language)

    def update_document(self, text):
        print("Text: {}".format(text))
        self.document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language=self.language)
        
    def get_sentiment(self):
        """
        Get sentiment score and magnitude of document.
        """
        return self.client.analyze_sentiment(request={'document': self.document}).document_sentiment

    def get_topic(self):
        """
        Get document category classification from a set of topics.
        """
        return self.client.classify_text(request={'document': self.document})

    def get_entity_sentiment(self):
        """
        Get sentiments, salience, metadata for each entity in the document.
        """
        response = self.client.analyze_entity_sentiment(request={'document': self.document})
        entities = []
        for entity in response.entities:
            e_name = entity.name
            e_type = language_v1.Entity.Type(entity.type_).name
            e_salience = entity.salience
            e_sentiment = entity.sentiment

            print(u"Representative name for the entity: {}".format(e_name))
            print(u"Entity type: {}".format(e_type))
            print(u"Salience score: {}".format(e_salience))
            print(u"Entity sentiment score: {}".format(e_sentiment.score))
            print(u"Entity sentiment magnitude: {}".format(e_sentiment.magnitude))

            # Metadata includes Wikipedia links and MIDs
            e_metadata = {}
            e_metadata['wiki_url'] = 'none'
            e_metadata['knowledge_mid'] = 'none'
            for metadata_name, metadata_value in entity.metadata.items():
                print(u"{} = {}".format(metadata_name, metadata_value))
                e_metadata[metadata_name] = metadata_value

            e_mention = ''
            e_mention_type = ''
            for mention in entity.mentions:
                print(u"Mention text: {}".format(mention.text.content))
                print(u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name))
                e_mention += mention.text.content
                e_mention_type += language_v1.EntityMention.Type(mention.type_).name


            e = {'representation': e_name,
                 'type': e_type,
                 'salience_score': e_salience,
                 'mention_text': e_mention,
                 'mention_type': e_mention_type,
                 'sentiment': e_sentiment}
            e.update(e_metadata)
            entities.append(e)
        return entities


class Text_Razor:
    def __init__(self, extractors=['entities', 'topics', 'dependency-trees', 'relations', 'entailments', 'senses', 'phrases', 'words']):
        self.client = tr.TextRazor(extractors=extractors)

    def query(self, text):
        response = self.client.analyze(text)
        if response.ok:
            self.entities = response.entities()
            self.entailments = response.entailments()
            self.topics = response.topics()
            self.categories = response.categories()
            self.noun_phrases = response.noun_phrases()
            self.properties = response.properties()
            self.relations = response.relations()

    def get_topic(self):
        for topic in self.topics:
            if topic.score > 0.3:
                
        return self.topics

    def get_sentiment(self):
        pass

    def get_entities(self):
        for entity in self.entities:
            if entity.confidence_score > 1:
                e = {'representation': entity.matched_text,
                     'type': 'idk',
                     'relevance': entity.relevance_score,
                     'mention_words': entity.matched_words}
try:
    manager.get_dictionary('names')
except tr.TextRazorAnalysisException as e:
    manager.create_dictionary({'names':'names123'})

manager.add_entries('names', [{'Bob':'Bob'}, {'Misty':'Misty'}])

path = os.path.join('data', 'conversation{}'.format(3))
texts = []
for num, file in enumerate(os.listdir(path)):
    with open(os.path.join(path, '{}.txt'.format(num + 1)), 'r') as infile:
        t = infile.read()
        texts.append(t)
t = Text_Razor()
for i, text in enumerate(texts):
    t.query(text)
print(tr.AccountManager().get_account().requests_used_today)
# add dictionary support
