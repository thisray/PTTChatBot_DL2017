import os
import sys

import tensorflow as tf

from lib import data_utils
from lib.seq2seq_model_utils import create_model, get_predicted_sentence

import jieba

import random
from time import sleep


def fight(args, args1):
    
    #create two graphs to build nested sessions
    model_graph = tf.Graph()
    adv_graph = tf.Graph()

    adv_sess = tf.Session(graph=adv_graph)
    sess = tf.Session(graph=model_graph)

    total_sent = []
    total_sent = open('%s/random_sent.txt' % args.work_root, 'r').readlines()
    total_sent_len = len(total_sent)

    chatbot_A = 'Chatbot_A'
    chatbot_B = 'Chatbot_B'
    fight_tims = 5
    Sleep_or_not = True #False

    # model_name
    if args.model_name[0] == 'g':
        chatbot_A = 'Gossiping_Bot'
    elif args.model_name[0] == 'w':
        chatbot_A = 'WomenTalk_Bot'

    # model_2_name
    if args.model_2_name[0] == 'g':
        chatbot_B = 'Gossiping_Bot'
    elif args.model_2_name[0] == 'w':
        chatbot_B = 'WomenTalk_Bot'

    # # gpu_options test
    # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpu_usage)
    # config=tf.ConfigProto(gpu_options=gpu_options)
    
    ## 1st session
    with sess.as_default():
        # Create model and load parameters.
        with model_graph.as_default():
                args.batch_size = 1  # We decode one sentence at a time.
                model = create_model(sess, args)

                # Load vocabularies.
                vocab_path = os.path.join(args.data_dir, "vocab%d.in" % args.vocab_size)
                vocab, rev_vocab = data_utils.initialize_vocabulary(vocab_path)
        
        ## 2nd session
        with adv_sess.as_default():
            with adv_graph.as_default():
                
                # Create model and load parameters.
                args1.batch_size = 1  # We decode one sentence at a time.
                model_r = create_model(adv_sess, args1)

                # Load vocabularies.
                vocab_path_r = os.path.join(args1.data_dir, "vocab%d.in" % args1.vocab_size)
                vocab_r, rev_vocab_r = data_utils.initialize_vocabulary(vocab_path_r)

                # Decode from standard input.
                print('\n')
                sys.stdout.write("> ")
                sys.stdout.flush()
                sentence = sys.stdin.readline()

                ## make sure jieba split
                sentence = sentence_split(sentence)

                while sentence:

                    if sentence == 'random':
                        sentence = total_sent[random.randint(0, total_sent_len)]
                        sentence = sentence_split(sentence)
                        print('>> ', sentence)
                    elif sentence == 'exit':
                        print('\nBYE BYE ~ \n')
                        break

                    for turns in range(0, fight_tims):

                        # ChatbotA
                        predicted_sentence = get_predicted_sentence(args, sentence, vocab, rev_vocab, model, sess)
                        str1 = predicted_sentence[0]['dec_inp']
                        str1 = sentence_split(str1) ## make sure jieba split

                        # ChatbotB
                        predicted_sentence1 = get_predicted_sentence(args1, str1, vocab_r, rev_vocab_r, model_r, adv_sess)

                        # print(predicted_sentence)

                        # ChatbotA
                        if isinstance(predicted_sentence, list):
                            for sent in predicted_sentence:
                                # random_sleep(Sleep_or_not)
                                print("%s: %s" % (chatbot_A, sentence_combine(sent['dec_inp'])))
                        
                        # ChatbotB
                        if isinstance(predicted_sentence1, list):
                            for sent in predicted_sentence1:
                                random_sleep(Sleep_or_not)
                                print("%s: %s" % (chatbot_B, sentence_combine(sent['dec_inp'])))

                        sentence = predicted_sentence1[0]['dec_inp']
                        sentence = sentence_split(sentence) ## make sure jieba split
                    
                    print('\n')
                    sys.stdout.write("> ")
                    sys.stdout.flush()
                    sentence = sys.stdin.readline()
                    
                    sentence = sentence_split(sentence) ## make sure jieba split


## jieba split input sentence
def sentence_split(sentence):
    seg_list = jieba.cut(sentence, cut_all=False)
    sentence = ' '.join((' '.join(seg_list)).split())
    return sentence

def sentence_combine(sentence):
    seg_list = jieba.cut(sentence, cut_all=False)
    sentence = ''.join((' '.join(seg_list)).split())
    return sentence

def random_sleep(sleep_TF=True):
    if sleep_TF == True:
        # sleep(randint(1,3))
        sleep(random.uniform(1, 2))

                                
        
