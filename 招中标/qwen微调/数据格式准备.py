# -*- coding: utf-8 -*-

import json

import pandas as pd






if __name__ == '__main__':
    # 读取数据
    data_path = 'C:/Users/admin/Desktop/kedaxunfei/qwen2.5-3b数据集构建/微调数据.xlsx'
    data = pd.read_excel(data_path)
    # 问题	提取的实体	问题分类	意图分类
    take_data_question = data['问题'].tolist()
    take_data_entity = data['提取的实体'].tolist()
    take_data_class = data['问题分类'].tolist()
    # take_data_intent = data['意图分类'].tolist()


    for_data_list = []
    for question, entity, class_ in zip(take_data_question, take_data_entity, take_data_class):
        # print('原始数据：', question, entity, class_)
        # 更改格式，先做成参考格式
        data_dict = {}
        template = f"""你是一名实体提取、意图识别和分类领域专家，请严格遵循以下任务和工作流程的指示输出结果。\n\n任务：\n1-分析用户输入问题的语义信息和语法结构。\n2-根据分析结果，将问题中的停用词、无意图词、语气词和符号剔除。\n3-检查是否存在剔除遗漏，是否存在错误剔除，并进行矫正。\n4-将保留的文本进行实体、关键词、意图词、主语词、设备词识别。\n5-识别出的词以逗号分隔。\n6-根据分析结果、实体提取结果和给出的意图分类标签进行问题的意图分类。\n7-根据输出格式输出。\n\n意图标签：商品数据，招标中标信息，政策内容，政策文件信息，日常问题。\n\n请根据分类结果与要求的输出格式对比，存在格式问题则进行矫正后输出。\n\n输出格式：\n实体识别结果：实体，实体\n意图分类：意图标签\n\n请注意输出结果严格按照输出格式进行，不需要输出分析过程。不要输出实体结果。\n\n问题：{question}"""
        data_dict['instruction'] = template
        data_dict['input'] = ''
        data_dict['output'] = f"""实体识别结果：{entity}\n意图分类：{class_}"""
        # print('调整数据训练结构：', data_dict)
        for_data_list.append(data_dict)
        # 保存数据
    with open('C:/Users/admin/Desktop/kedaxunfei/qwen2.5-3b数据集构建/微调数据.json', 'a', encoding='utf-8') as f:
        json.dump(for_data_list, f, ensure_ascii=False, indent=4)

