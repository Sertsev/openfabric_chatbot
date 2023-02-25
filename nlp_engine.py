import nltk
from nltk.corpus import wordnet

# Download the required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Define some science-related synonyms for named entity recognition
science_synonyms = {
    'physics': ['mechanics', 'energy', 'motion', 'gravity', 'quantum'],
    'chemistry': ['elements', 'reactions', 'molecules', 'atoms', 'organic'],
    'biology': ['organisms', 'cells', 'evolution', 'genetics', 'ecology']
}

# Define a function to extract named entities from a question
def extract_entities(question):
    tokens = nltk.word_tokenize(question)
    tagged_tokens = nltk.pos_tag(tokens)
    entities = []
    for word, tag in tagged_tokens:
        if tag == 'NN':
            synsets = wordnet.synsets(word)
            if len(synsets) > 0:
                synset = synsets[0]
                entity = synset.name().split('.')[0]
                if entity in science_synonyms.keys():
                    entities.append(entity)
    return entities

# Define a function to answer science-related questions
def answer_question(question):
    # Extract named entities from the question
    entities = extract_entities(question)
    # If no entities were found, return a generic response
    if len(entities) == 0:
        return "I'm sorry, I don't understand the question."
    # If multiple entities were found, return a response asking for clarification
    elif len(entities) > 1:
        return "Which of these fields of science is your question related to? " + ', '.join(entities) + "?"
    # If a single entity was found, generate a response based on the entity
    else:
        entity = entities[0]
        if entity == 'physics':
            return "Physics is the branch of science that deals with matter, energy, and their interactions."
        elif entity == 'chemistry':
            return "Chemistry is the branch of science that deals with the composition, structure, properties, and reactions of matter."
        elif entity == 'biology':
            return "Biology is the branch of science that deals with living organisms and their interactions with each other and their environment."
