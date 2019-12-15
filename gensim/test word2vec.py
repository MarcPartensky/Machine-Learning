#import the model
from gensim.models import KeyedVectors
import tensorflow as tf
from tensorflow import keras
from gensim.models import Doc2Vec


# help(Doc2Vec)




# Load vectors directly from the file
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=50000)

# Access vectors for specific words with a keyed lookup:
vector = model['easy']

# see the shape of the vector (300,)
print(vector.shape)

# Processing sentences is not as simple as with Spacy:
# vectors = [model[x] for x in "This is some text I am processing with Marc".split(' ')]

#Make a demonstration
# print(model.most_similar('easy'))
#
# print(model)
