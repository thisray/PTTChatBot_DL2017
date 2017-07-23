## ChatBot Model
Use the preprocess Chinese corpus dataset from [1_ptt_crawler](https://github.com/thisray/PTTChatBot_DL2017/tree/master/1_ptt_crawler), [2_make_QA](https://github.com/thisray/PTTChatBot_DL2017/tree/master/2_make_QA) to train the [seq2seq](https://www.tensorflow.org/tutorials/seq2seq) model.



## Environment
* `main.py`: execution file
* `/lib`: code file
* `/works`: storage corpus dataset and model file 
* `chat.txt.gz`: **input corpus data**, need to zip to `.gz` type
* `test_set.txt`: testing data
* `/nn_models`: auto build when training model (save tensorflow `checkpoint` file) 

detail of `works` directory:  

    works
      ├── <model_name_1>
      │         ├── data
      │         │     ├── train - chat.txt.gz
      │         │     └── test - test_set.txt
      │         └── nn_models
      │      
      ├── <model_name_2>
      ...



## Execution Parameter
* `mode`: train / test / chat / fight
* `model_name`: set `model_name` directory in works directory
* other setting: see `/lib/config.py` 


## How to use

prepare data in `ptt_dataset` and run `train` mode:  

    $ python main.py --mode train --model_name ptt_dataset


after training mode can run `test` / `chat` mode:
    
    $ python main.py --mode test --model_name ptt_dataset
    $ python main.py --mode chat --model_name ptt_dataset

`fight` mode with two `pre-train model` (e.g. Gossiping_dataset and WomenTalk_dataset):
    
    $ python main.py --mode fight --model_name Gossiping_dataset -- model_2_name WomenTalk_dataset


## Reference (Codes credits)
* https://www.tensorflow.org/tutorials/seq2seq
* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/Marsan-Ma/tf_chatbot_seq2seq_antilm