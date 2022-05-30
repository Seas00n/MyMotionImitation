# MyMotionImitation
## Training Example
python3 motion_imitation/run.py --mode train --motion_file motion_imitation/data/motions/dog_pace.txt --int_save_freq 10000000 --visualize 
### --mode: 训练或者测试
### --motion_file: 需要模仿的数据
### --int_save_freq:
specifies the frequency for saving intermediate policies every n policy steps.
### --visualize:是否可视化