#Libraries. nltk is a cool nlp library
import nltk
import random
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#gets the word and figures out parts of speech
print("input your mad libs text below.")
Text = input()
tokens = nltk.word_tokenize(Text)
tagged = nltk.pos_tag(tokens)

#gets a random sample of the words. sample size is just a fraction of the words
n = int( len(tagged) / 4)
madtagged = random.sample(list(enumerate(tagged)), n)

#gets indexes of the samples
indexes = []
values = []
for idx, val in madtagged:
    indexes.append(idx)
    values.append(val)

#removes all the articles and shit so we just do fun things like nouns and verbs
goodones = ["NN", "NNP", "RB", "VB", "JJ"]
newlist =[]
goodidx = []
for i in values:
  if i[1] in goodones:
    idx = indexes[values.index(i)]
    goodidx.append(idx)
    newlist.append(i)

#asks you for new words and replaces them
for i in newlist:
  print("enter" + i[1])
  new_word = input()
  idx = goodidx[newlist.index(i)]
  tokens[idx] = new_word

print(' '.join(tokens))