from tensorflow.contrib import learn
import gensim
from string import digits
import re

#Clean function, as with much, taken from Kim Yoon tutorial via NYCDSA tutors

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = string.translate(None, digits)
    return string.strip().lower()


reviews = open("reviews_lines.txt", 'r').readlines()

reviews = [x.decode('utf-8') for x in reviews]
reviews_token = [clean_str(x) for x in reviews]
reviews_token = [x for x in reviews_token if x!=[""]]
reviews_toekn = x.split(' ') for x in review]

model = gensim.models.Word2Vec(sentences = reviews_token, min_count=10, size=300, window=5, negative=20)
model.wv.save_word2vec_format("./review_model_10_300_5_neg20.bin")
