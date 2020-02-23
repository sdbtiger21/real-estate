import time
import os

#----Define
dpt_on = 1

#----Debug function

def dpt(var_name, tap = 0):
    global dpt_on
    if dpt_on == 1:
        space = '   ' * tap
        print(space + str(var_name))
    else :
        pass

def start_timer():
    global start_time
    start_time = time.time()
    return start_time

def end_timer():
    ms_time = time.time() - start_time
    return print('Measured Time : ', round(ms_time, 6))

def get_path(add_dir_path = None, out_path = None) :
    cur_path = os.getcwd() #현재 위치(main파일이 있는 곳들)
    input_path = cur_path + add_dir_path #현재 위치 + input 파일이 있는 하위 위치
    if not out_path is None :
        output_path = cur_path + out_path  # 현재 위치 + output을 저장하고 싶은 위치
        if not os.path.isdir(output_path):
            os.mkdir(log_out_loc)
    else :
        output_path = None
    return cur_path, input_path, output_path


def make_dir(dir_path) :
    if not os.path.isdir(dir_path) :
        os.mkdir(dir_path)

