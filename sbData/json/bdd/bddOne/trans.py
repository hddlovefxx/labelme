"""Convert coco to Scalabel format."""

import argparse
import json
import os
from itertools import groupby
from multiprocessing import Pool
from typing import Dict, Iterable, List, Optional, Tuple, TextIO

def open_read_text(filepath: str) -> TextIO:
    """Open a text file for reading and return a file object."""
    return open(filepath, mode="r", encoding="utf-8")

def write_json_data(dict,path):
    #写入json文件

    with open(path,'w') as r:
    # 定义为写模式，名称定义为r
        json.dump(dict,r)
        #将dict写入名称为r的文件中
        
    r.close()
    #关闭json写模式
    

input="E:/paper_exm/labelme/sbData/json/bdd/bddOne/one.json"
with open_read_text(input) as fp:
    oneJson=json.load(fp)
    for i,frame in enumerate(oneJson['frames']):
        newLabels=[]
        for i,label in enumerate(frame['labels']):
            label['id']=label['index']
            if label['category']=='area' or label['category']=='line':
                del label['box2d']
            else:
                del label['poly2d']
            newLabels.append(label)
        frame['labels']=newLabels
        cur=oneJson
        cur['frames']=frame
        path="E:/paper_exm/labelme/sbData/json/bdd/bddScatter"
        savePath=os.path.join(path,frame['name']).replace(".png", ".json")
        write_json_data(cur,savePath)
        print("hello")
print("hello")