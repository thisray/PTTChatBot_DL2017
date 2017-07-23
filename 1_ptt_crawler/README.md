## PTT_crawler
To crawl Chinese articles from [PTT](https://www.ptt.cc/bbs/index.html) and save into multiple `json` files.

## How to use

the setting of `DL_ptt_crawer.py`:  

    save_dir_path: save directory (str)
    crawler_board: e.g. 'Gossiping', 'WomenTalk' (str)
    crawler_from, crawler_to: page index (int)
    (e.g. the index of [https://www.ptt.cc/bbs/Gossiping/index24972.html] is 24972)
    
run:  

    $ python DL_ptt_crawer.py


## Reference (Codes credits)
* https://github.com/zake7749/PTT-Chat-Generator
* https://github.com/wy36101299/PTTcrawler/blob/master/pttcrawler.py