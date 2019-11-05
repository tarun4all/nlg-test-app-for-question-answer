import json
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
import sys
from textblob import TextBlob
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize, sent_tokenize

# These are the english part-of-speach tags used in this demo program.
    # .....................................................................
    # NNS     Noun, plural
    # JJ  Adjective
    # NNP     Proper noun, singular
    # VBG     Verb, gerund or present participle
    # VBN     Verb, past participle
    # VBZ     Verb, 3rd person singular present
    # VBD     Verb, past tense
    # IN      Preposition or subordinating conjunction
    # PRP     Personal pronoun
    # NN      Noun, singular or mass
    # .....................................................................

def pos_tagging(sentence):
    words_list = remove_stop_words(sentence)
    # words_list = word_tokenize(sentence)
    tagged = nltk.pos_tag(words_list)
    return tagged

def remove_stop_words(sentence):
    words_list = word_tokenize(sentence)
    words_list = [w for w in words_list if not w in stop_words]
    return words_list

def process_text(text):
    text = text.replace('>', ' ')
    text = text.lower()

    return text

def split_para_to_sentences(para):
    sentences_list = sent_tokenize(process_text(para))
    return sentences_list

def main():
    para = sys.argv[1]
    # print(para)
    sentences_list = split_para_to_sentences(para)
    tag_array = []
    for each_sentence in sentences_list:
        tagged_list = pos_tagging(each_sentence)
        tag_array.append(tagged_list)

    print(tag_array)
    sys.stdout.flush()

main()