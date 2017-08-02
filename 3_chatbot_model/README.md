## ChatBot Model
Use the preprocess Chinese corpus dataset from [1_ptt_crawler](https://github.com/thisray/PTTChatBot_DL2017/tree/master/1_ptt_crawler), [2_make_QA](https://github.com/thisray/PTTChatBot_DL2017/tree/master/2_make_QA) to train the [seq2seq](https://www.tensorflow.org/tutorials/seq2seq) model.

## Model architecture
![Architecture pic](https://github.com/thisray/PTTChatBot_DL2017/blob/master/0_pic/Architecture.png)


## Environment
* python version: > 3.0
* requirement python package: tensorflow, numpy, jieba
* tensorflow version: 1.0 

degrade tensorflow into 1.0.1:

    #  for python 3.5
    $ pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.1-cp35-cp35m-linux_x86_64.whl
    
    #  for python 2.7
    $ pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.1-cp27-cp27m-linux_x86_64.whl

## Directory instruction
* `main.py`: execution file
* `/lib`: code files
* `/works`: storage corpus dataset and model file 
* `<model_name>`: the name of this directory is `model_name`
* `/data`: put training and testing data (directory) here
* `chat.txt.gz`: **input corpus data**, put in `/train` and need to zip to `.gz` type
* `test_set.txt`: testing data, put it in `/test` (you can write any Chinese sentence in this file to test)
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
      │         ├── data
      │         │     ├── train - chat.txt.gz
      │         │     └── test - test_set.txt
      │         └── nn_models      
      ...


## Data & Model download

### Training data:
* Gossiping training data: https://goo.gl/9yQXLQ
* WomenTalk training data: https://goo.gl/224rbR
* directly put `chat.txt.gz` in `/works/<model_name>/data/train/`

### Trained model:
* Gossiping trained model: https://goo.gl/WS1PVX
* WomenTalk trained model: https://goo.gl/xUdwys
* This is entire `<model_name>` dir, after unzip, put in `/works/` directly.
* If you use these trained models directly, you sould ensure the model settings (in `config.py`) are the same as [Model architecture](https://github.com/thisray/PTTChatBot_DL2017/tree/master/3_chatbot_model#model-architecture).

### Random sentence (optional):
* random_sent.txt: https://goo.gl/mP7qPV
* use in `mode: fight`, can type `> random()` to select a random sentence in `random_sent.txt` as input

## Execution parameters
* `mode`: train / test / chat / fight
* `model_name`: set `model_name` directory in works directory
* `gpu_usage`: 0 (CPU mode) / > 0.0 (GPU mode)
* other parameter setting: see `/lib/config.py` 


## How to use (example)

train model: prepare data in `/ptt_dataset` and run `train` mode: 

    # It is not recommended to train in CPU mode.
    $ python main.py --mode train --model_name ptt_dataset

after training: can run `test` / `chat` mode to chat with one chatbot:
    
    $ python main.py --mode test --model_name ptt_dataset
    $ python main.py --mode chat --model_name ptt_dataset

`fight` mode: select **Two** `trained models` and let them chat with each other:
    
    $ python main.py --mode fight --model_name Gossiping_dataset --model_2_name WomenTalk_dataset


## Some results
![some results](https://github.com/thisray/PTTChatBot_DL2017/blob/master/0_pic/pic.png)

## Reference (Codes credits)
* https://www.tensorflow.org/tutorials/seq2seq
* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/Marsan-Ma/tf_chatbot_seq2seq_antilm
