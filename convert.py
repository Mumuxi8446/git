import os

# 改成你的实际路径
folder_path = r"D:\project\git_car"

print(f"检查文件夹：{folder_path}\n")

xml_files = [f for f in os.listdir(folder_path) if f.endswith('.xml')]
jpg_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

print(f"XML文件 ({len(xml_files)}个):")
for f in xml_files[:10]:
    print(f"  {f}")

print(f"\n图片文件 ({len(jpg_files)}个):")
for f in jpg_files[:10]:
    print(f"  {f}")