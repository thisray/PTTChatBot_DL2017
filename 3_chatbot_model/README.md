## ChatBot Model
Use the preprocess dataset from [1_ptt_crawler](https://github.com/thisray/PTTChatBot_DL2017/tree/master/1_ptt_crawler), [2_make_QA](https://github.com/thisray/PTTChatBot_DL2017/tree/master/2_make_QA) to train the seq2seq model.



## Environment
* `lib` directory: code file
* `works` directory: storage corpus dataset, model file
(training corpus dataset put in: ./works/<model_name>/data/train) 
* `main.py`: execution file



## Execution Parameter
* `mode`: train / test / chat / fight
* `model_name`: set `model_name` directory in works directory



## How to use

run:
    
    $ python 1_make_QA.py  
    $ python 2_deal_text.py
    

## Reference (Codes credits)
* https://www.tensorflow.org/tutorials/seq2seq
* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/Marsan-Ma/tf_chatbot_seq2seq_antilm