import jieba

input_data_path = './QA_file.txt'
output_data_path = './splited_QA_data.txt'

with open(input_data_path, 'r', encoding='utf-8') as dataset:
    with open(output_data_path, "w") as f:
        for line in dataset:
            seg_list = jieba.cut(line, cut_all=False)
            target_str = " ".join(seg_list)
            f.write(target_str)
    print('write ok')