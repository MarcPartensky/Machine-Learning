#import the model
from gensim.models import KeyedVectors
import tensorflow as tf
from tensorflow import keras
from gensim.models import Doc2Vec


# help(Doc2Vec)




# Load vectors directly from the file
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)

# Access vectors for specific words with a keyed lookup:
vector = model['finance']

# see the shape of the vector (300,)
print(vector.shape)

# Processing sentences is not as simple as with Spacy:
# vectors = [model[x] for x in "This is some text I am processing with Marc".split(' ')]


s1 = "degree"
# s2 = "Access vectors for specific words easy the keyed lookup, easier"
s2 = "hello i am valentin and i want a job because im poor"

s1 = s1.split(" ")
s2 = s2.split(" ")

for m1 in s1:
    for m2 in s2:
        if m1 in model.index2word:
            if m2 in model.index2word:
                value = model.similarity(m1, m2)
                if value>0.5:
                    print(m1, m2, value)


#Make a demonstration
# print(model.most_similar('finance'))
# print(model.similarity('spain', 'france'))
#
# print(model)
