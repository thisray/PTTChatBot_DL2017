# PTTChatBot_DL2017
![some results](https://github.com/thisray/PTTChatBot_DL2017/blob/master/0_pic/pic.png)
Group member: ninetf135246, thisray

## Introduction
In one of the course assignments, we have experimented with RNN to generate and process text sequences. It was a very interesting experience and motivated us to study whether it is possible to train talkshow chatbots.  

In order to build chatbots capable of handling a wide range to topics, we trained our chatbots using the Chinese corpus from two of the PTT gossip forums: Gossiping and Women Talk. Both forums have their own styles of opinionated expressions. We aim to create chatbots to deliver quarrelsome or sarcastic responds to input queries.

## Code instruction
* `1_ptt_crawler`: crawl Chinese corpus from PTT.
* `2_make_QA`: make data into Q & A type.
* `3_chatbot_model`: train & use chatbot.

## ChatBot environment
* python version: > 3.0
* requirement python package: tensorflow, numpy, jieba
* tensorflow version: 1.0 

## Reference (Codes credits)
* https://github.com/fxsjy/jieba
* https://github.com/zake7749/PTT-Chat-Generator
* https://www.tensorflow.org/tutorials/seq2seq
* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/Marsan-Ma/tf_chatbot_seq2seq_antilm
