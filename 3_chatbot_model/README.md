## ChatBot Model
Use the preprocess Chinese corpus dataset from [1_ptt_crawler](https://github.com/thisray/PTTChatBot_DL2017/tree/master/1_ptt_crawler), [2_make_QA](https://github.com/thisray/PTTChatBot_DL2017/tree/master/2_make_QA) to train the [seq2seq](https://www.tensorflow.org/tutorials/seq2seq) model.



## Environment
* `main.py`: execution file
* `/lib`: code file
* `/works`: storage corpus dataset, model file 
* `chat.txt.gz`: input corpus data, need to zip to `.gz` type
* `test_set.txt`: testing data  

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
* other setting: in `/lib/config.py` 


## How to use


    

## Reference (Codes credits)
* https://www.tensorflow.org/tutorials/seq2seq
* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/Marsan-Ma/tf_chatbot_seq2seq_antilm