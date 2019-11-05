import json
import nltk
import sys
from textblob import TextBlob
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize, sent_tokenize
# sandwich.encode("utf-8")

# arrayList = json.loads(open('210SplitPara.json').read())


def pos_tagging(sentence):
    words_list = word_tokenize(sentence)
    tagged = nltk.pos_tag(words_list)
    return tagged


def remove_stop_words(sentence):
    words_list = word_tokenize(sentence)
    words_list = [w for w in words_list if not w in stop_words]
    return words_list


def split_para_to_sentences(para):
    sentences_list = sent_tokenize(process_text(para))
    return sentences_list


def process_text(text):
    text = text.replace('>', ' ')
    text = text.lower()

    return text


def genQuestion(line):
    """
    outputs question from the given text
    """

    if type(line) is str:  # If the passed variable is of type string.
        line = TextBlob(line)  # Create object of type textblob.blob.TextBlob

    bucket = {}  # Create an empty dictionary

    for i, j in enumerate(line.tags):  # line.tags are the parts-of-speach in English
        if j[1] not in bucket:
            bucket[j[1]] = i  # Add all tags to the dictionary or bucket variable
    question = ''  # Create an empty string

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

    # Create a list of tag-combination

    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']

    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']

    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']

    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']
    l14 = ['JJ', 'NN', 'VBZ', 'PRP', 'FW', 'IN']
    l15 = ['JJ', 'CC', 'VBP', 'NN', 'NNP', 'CD']
    # With the use of conditional statements the dictionary is compared with the list created above
    if all(key in bucket for key in l14):
        question = 'What does '+ str(line)[0:28] + ' to?'
    elif all(key in bucket for key in l1):  # 'NNP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l2):  # 'NNP', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l3):  # 'PRP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l4):  # 'PRP', 'VBG', 'VBZ' in sentence.
        question = 'What ' + line.words[bucket['PRP']] + ' ' + ' does ' + line.words[bucket['VBG']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l7):  # 'NN', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NN']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l8):  # 'NNP', 'VBZ', 'JJ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l9):  # 'NNP', 'VBZ', 'NN' in sentence
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l11):  # 'PRP', 'VBZ' in sentence.
        if line.words[bucket['PRP']] in ['she', 'he']:
            question = 'What' + ' does ' + line.words[bucket['PRP']].lower() + ' ' + line.words[
                bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l10):  # 'NNP', 'VBZ' in sentence.
        question = 'What' + ' does ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l13):  # 'NN', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NN']] + '?'
    elif all(key in bucket for key in l15):
        question = "What is "+ str(line)[0:42] + ' ?'
    # When the tags are generated 's is split to ' and s. To overcome this issue.
    if 'VBZ' in bucket and line.words[bucket['VBZ']] == "'":
        question = question.replace(" ' ", "'s ")

    if question != '':
        return [question]
    else:
        return []

sentences_list = split_para_to_sentences(el['text'])
tag_array = []
for each_sentence in sentences_list:
    tagged_list = pos_tagging(each_sentence)
    tag_array.append(tagged_list)

print(tag_array)

def main():
    """
    Accepts a text file as an argument and generates questions from it.
    """
    # Open the file given as argument in read-only mode.
    if len(sys.argv) > 1:
        print(sys.argv[1])
        array_list = json.loads(open(sys.argv[1]).read())
        write_path = sys.argv[2];
    else:
        array_list = json.loads(open('210SplitPara.json').read())
        write_path = 'result.json'
    sampleData = ''
    for array in array_list:
        for el in array:
            el['sentences'] = []
            sampleData = sampleData + el['text']+'\n'
            if el['bold']:
                sentence = process_text(el['text'])

                # Send the content of text file as string to function parse()
                questions = genQuestion(sentence)
                tagged_list = pos_tagging(sentence)
                posTag = []
                for each_tag in tagged_list:
                    each_tag = {'word': each_tag[0], 'tag': each_tag[1]}
                    posTag.append(each_tag)
                el['sentences'].append({
                    'sentence': sentence,
                    'posTags': posTag,
                    'questions': questions
                })
            else:
                sentences_list = split_para_to_sentences(el['text'])
                xyz = []
                for each_sentence in sentences_list:
                    questions = genQuestion(sentence)
                    tagged_list = pos_tagging(each_sentence)
                    for each_tag in tagged_list:
                        each_tag = {'word': each_tag[0], 'tag': each_tag[1]}
                        xyz.append(each_tag)
                    el['sentences'].append({
                        'sentence': each_sentence,
                        'posTags': xyz,
                        'questions' : questions
                    })
            print(el)
    # print(array_list)
    json_object = json.dumps(array_list)

    # with open(write_path, 'w') as file:
    #     file.write(json.dumps(json_object))
    with open('sample1.txt','w') as file:
        file.write(sampleData)
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>JSON',json_object)


# if __name__ == "__main__":
#     main()