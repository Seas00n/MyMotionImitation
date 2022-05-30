import os
import inspect
currentdir = '/home/wangyuxuan/MyMotionImitation'
parentdir = '/home/wangyuxuan'
# 动态修改搜索路径优先级，优先在parentdir中搜索
os.sys.path.insert(0, parentdir)
import numpy as np
import os
import random
import tensorflow as tf
import time
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--mode", dest="mode", type=str, default="train")
    arg_parser.add_argument("--motion_file", dest="motion_file", type=str,
                        default="MyMotionImitation/data/motions/dog_pace.txt")
    arg_parser.add_argument("--int_save_freq", dest="int_save_freq", type=int,
                            default=0)  # save intermediate model every n policy steps
    arg_parser.add_argument("--visualize", dest="visualize", action="store_true", default=False)
    
    return

if __name__ =='__main__':
    main()