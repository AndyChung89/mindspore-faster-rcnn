#----------------------------------------------------#
#   获取测试集的ground-truth
#   具体视频教程可查看
#   https://www.bilibili.com/video/BV1zE411u7Vw
#----------------------------------------------------#
import os
import shutil
'''
！！！！！！！！！！！！！注意事项！！！！！！！！！！！！！
# 这一部分是当xml有无关的类的时候，下方有代码可以进行筛选！
'''
#---------------------------------------------------#
#   获得类
#---------------------------------------------------#
def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

save_file = "./input/ground-truth/"

if not os.path.exists("./input"):
    os.makedirs("./input")
if os.path.exists(save_file):
    shutil.rmtree(save_file)
    os.makedirs(save_file)
else:
    shutil.rmtree(save_file)
    os.makedirs(save_file)

with open('all_data_test.txt', 'r') as f:
    image_ids = f.readlines()

for image_id in image_ids:
    image_path = image_id.split(' ')[0]
    content = image_id.split(' ')
    with open(save_file+os.path.basename(image_path)[:-4]+".txt", "w") as new_f:
        for i in range(1, len(content)):
            label_content = content[i].replace('\n', '').split(',')
            obj_name = label_content[4]
            left = label_content[0]
            top = label_content[1]
            right = label_content[2]
            bottom = label_content[3]

            print(obj_name, left, top, right, bottom)
            new_f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))

print("Conversion completed!")
