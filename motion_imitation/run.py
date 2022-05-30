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
from motion_imitation.envs import env_builder as env_builder
from motion_imitation.learning import imitation_policies as imitation_policies
from motion_imitation.learning import ppo_imitation as ppo_imitation




ENABLE_ENV_RANDOMIZER = True



def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--mode", dest="mode", type=str, default="train")
    arg_parser.add_argument("--motion_file", dest="motion_file", type=str,
                        default="motion_imitation/data/motions/dog_pace.txt")
    arg_parser.add_argument("--int_save_freq", dest="int_save_freq", type=int,
                            default=0)  # save intermediate model every n policy steps
    arg_parser.add_argument("--visualize", dest="visualize", action="store_true", default=False)
    args = arg_parser.parse_args()
    enable_env_rand = ENABLE_ENV_RANDOMIZER and (args.mode != "test")
    return

if __name__ =='__main__':
    main()