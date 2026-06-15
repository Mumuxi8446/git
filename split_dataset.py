import os
import random
import shutil

# ========== 改这里（写完整路径）==========
root = r"D:\project\git_car"                          # 根目录
img_folder = r"D:\project\git_car\zjb_bb3-4"  # 图片文件夹完整路径
txt_folder = r"D:\project\git_car\zjb_labels_bb3-4"    # TXT文件夹完整路径
train_ratio = 0.8
# ========================================

# 获取所有图片
images = [f for f in os.listdir(img_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(images)

# 划分
split_idx = int(len(images) * train_ratio)
train_images = images[:split_idx]
val_images = images[split_idx:]

# 创建目标文件夹
train_img_dir = os.path.join(root, "images", "train")
val_img_dir = os.path.join(root, "images", "val")
train_txt_dir = os.path.join(root, "labels", "train")
val_txt_dir = os.path.join(root, "labels", "val")

for d in [train_img_dir, val_img_dir, train_txt_dir, val_txt_dir]:
    os.makedirs(d, exist_ok=True)

# 复制训练集
for img in train_images:
    shutil.copy2(os.path.join(img_folder, img), os.path.join(train_img_dir, img))
    
    txt_name = img.rsplit('.', 1)[0] + '.txt'
    src_txt = os.path.join(txt_folder, txt_name)
    if os.path.exists(src_txt):
        shutil.copy2(src_txt, os.path.join(train_txt_dir, txt_name))

# 复制验证集
for img in val_images:
    shutil.copy2(os.path.join(img_folder, img), os.path.join(val_img_dir, img))
    
    txt_name = img.rsplit('.', 1)[0] + '.txt'
    src_txt = os.path.join(txt_folder, txt_name)
    if os.path.exists(src_txt):
        shutil.copy2(src_txt, os.path.join(val_txt_dir, txt_name))

print(f"完成！训练集：{len(train_images)}，验证集：{len(val_images)}")