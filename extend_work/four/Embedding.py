# -*- coding: utf-8 -*-
"""
Created on Tue May 7 2019

@author: Seahymn
"""

import os
import pickle
from gensim.models import Word2Vec
from keras.preprocessing.text import Tokenizer

working_dir = './data/'

# Load the *.pkl data. 
def LoadData(file_to_load):
    with open(file_to_load, 'rb') as f:
        loaded_file = pickle.load(f)
    return loaded_file
    
def total(working_dir,directory):
    total_list = []    
    Files_path = os.listdir(working_dir + directory)
    for file in Files_path:
        path = working_dir + directory + '/' + file + '/'
        pkl_file = path + file + '_total_list.pkl'
        if os.path.isfile(pkl_file):
            func_list = LoadData(pkl_file)
            total_list = total_list + func_list
    return total_list

total_list = total(working_dir,'Train') +  total(working_dir,'Validation') + total(working_dir,'Test') 
print ("The length of the list is : " + str(len(total_list)))

#--------------------------------------------------------#
# 2. Tokenization: convert the loaded text (the nodes of ASTs) to tokens.

new_total_token_list = []

for sub_list_token in total_list:
    new_line = ','.join(sub_list_token)
    new_total_token_list.append(new_line)

tokenizer = Tokenizer(num_words=None, filters=',', lower=False, char_level=False, oov_token=None)
tokenizer.fit_on_texts(new_total_token_list)

# Save the tokenizer.
with open(working_dir + 'all_tokenizer_no_comments.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)
    
# ----------------------------------------------------- #
# 3. Train a Vocabulary with Word2Vec -- using the function provided by gensim

#w2vModel = Word2Vec(train_token_list, workers = 12, size=100) # With default settings, the embedding dimension is 100 and using, (sg=0), CBOW is used.  
w2vModel = Word2Vec(total_list, workers = 12)

print ("----------------------------------------")
print ("The trained word2vec model: ")
print (w2vModel)

w2vModel.wv.save_word2vec_format(working_dir + "all_w2v_model_CBOW_no_comments.txt", binary=False)