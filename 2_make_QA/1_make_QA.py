from responsesEvaluate import Evaluator
import match
import json
import os
import random
import logging

# reference:
# https://github.com/zake7749/PTT-Crawler

## input files (json)
base_path = './'
input_path = 'crawler_save/'
data_path = base_path + input_path   

## output file name & path
output_file_name = 'QA_file'
output_file = './' + output_file_name + '.txt'

## load all json path
json_file_list = []
for file in os.listdir(data_path):
    if file.endswith(".json"):
        json_file_path = data_path + file
        json_file_list.append(json_file_path)

evaluator = Evaluator()

i = 0
total_len = len(json_file_list)

with open(output_file, 'w', encoding='utf-8') as output:
    for json_file in json_file_list:
        i = i +1
        print('Now deal: ', json_file, '  (', i, '/', total_len, ')')

        with open(json_file, 'r', encoding='utf-8') as data:
            json_dict = json.load(data)

            for article in json_dict:
                temp_title = ''
                
                try:
                    temp_title = article["Title"]
                    if '[' in temp_title and ']' in temp_title:
                        temp_title = temp_title.split(']')[-1]
                    if temp_title[0] == ' ':
                        temp_title = temp_title[1:]
                except:
                    temp_title = ''
                    continue
                try:
                    all_response = article["Responses"]
                    best_response = evaluator.getBestResponse(all_response, topk=1)
                    best_response = best_response[0][0]
                    if best_response[0] == ' ':
                        best_response = best_response[1:]
                except:
                    all_response = []
                    continue

                output.write(temp_title + '\n')
                output.write(best_response + '\n')
