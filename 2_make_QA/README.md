## Make Q&A
To make PTT articles from [PTT_crawler](https://github.com/thisray/PTTChatBot_DL2017/tree/master/1_ptt_crawler) into Q&A corpus type (one `.txt` file).

## Environment
* python version: > 3.0

## Code instruction

* `1_make_QA.py`: read all `json` files from the `input_path` directory, and make `QA_corpus` data.
* `2_deal_text.py`: use `jieba` library to split text of `QA_corpus` data.

## How to use

run:

    $ python 1_make_QA.py  
    $ python 2_deal_text.py


## Reference (Codes credits)
* https://github.com/fxsjy/jieba
* https://github.com/zake7749/PTT-Chat-Generator
* https://github.com/wy36101299/PTTcrawler/blob/master/pttcrawler.py