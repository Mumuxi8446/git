# RoboMaster 装甲板检测 - YOLO 训练全流程

> 从 LabelImg 标注到 YOLO 训练部署的完整记录

## 📁 项目结构

D:\project\git_car
│
├── dataset.yaml # 数据集配置文件
├── README.md # 本文件
├── split_dataset.py #数据集转化为训练集和检测集
├── convert.py    #XML转化txt
├── 2026-06-16-032143.mp4 
├── 20260615-1858-50.2877111.mp4                                               #原视频
│
│
├── images/ # 图片文件夹
│ ├── train/ # 训练图片 (80%)
│ └── val/ # 验证图片 (20%)
│
├── labels/ # YOLO标注文件夹
│ ├── train/ # 训练标注
│ └── val/ # 验证标注
│
├── runs/ # 训练结果
│ └── detect/
│ └── train-12/ # 训练12次的结果
│ └── weights/
│ ├── best.pt # 最佳模型
│ └── last.pt # 最后模型
│└── detect\predict#识别后视频
 

最佳模型"git_car\runs\detect\train-12"

yolo detect predict model=D:\project\git_car\runs\detect\train-12\weights\best.pt source="D:\project\git_car\2026-06-16-032143.mp4" show=True save=true conf=0.3
####清晰视频置信度以0.7为好 快速运动且较模糊置信度需≤0.3


## 🛠️ 环境配置

### 1. 创建 Conda 环境

```bash
conda create -n yolo_car python=3.13 -y
conda activate yolo_car

###2. 安装 YOLO

```bash
pip install ultralytics


###3. 安装 GPU 版 PyTorch（RTX 5070 用）

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

⚠️ 重要：RTX 5070 需要 CUDA 12.8+，使用 cu128 版本

###4. 验证 GPU
```bash
python -c "import torch; print(torch.cuda.is_available())"
# 应输出：True



##📕🏷️数据标注（LabelImg）
标注流程：
打开 LabelImg

切换格式：点击 PascalVOC 切换到 YOLO

打开图片文件夹

框选装甲板，填写类别名称

保存（自动生成 .txt 文件）
每个图片对应一个 .txt 文件：

🐖若如本人一般不慎忘记切换到yolo，可使用convert.py文件转化


##📊 数据集配置

dataset.yaml
path: D:/project/git_car
train: images/train
val: images/val
nc: 3  # 改成你的类别数量
names: ['red3-4', 'blue3-4', '狙击手']  # 改成你的类别名称

🚀 模型训练

#基础训练命令
conda activate yolo_car
cd D:\project\git_car

最佳模型"git_car\runs\detect\train-12"

yolo detect predict model=D:\project\git_car\runs\detect\train-12\weights\best.pt source="D:\project\git_car\2026-06-16-032143.mp4" show=True save=true conf=0.3
##如
#展示#保存#置信度为0.3#
####清晰视频置信度以0.7为佳 快速运动且较模糊置信度需≤0.3

完整参数
bash
yolo detect predict model=runs/detect/train-12/weights/best.pt source="视频路径.mp4" show=True save=True conf=0.5 iou=0.5


场景	conf 推荐值	说明
误检多	0.6-0.7	提高置信度，过滤错误检测
漏检多	0.3-0.4	降低置信度，检出更多目标
平衡	0.5	默认值


###训练参数说明
参数	说明	推荐值
epochs	训练轮数	100-300
imgsz	输入图片尺寸	640
batch	批次大小	16（GPU） / 4（CPU）
device	训练设备	（GPU） / （CPU）

输出位置
text
runs/detect/predict/视频名称.mp4


⚠️ 常见问题与解决
1. 文件名有空格导致报错
❌ 错误：

bash
source=2026-06-16 032143.mp4  # 被拆成两个参数
✅ 正确：

bash
source="2026-06-16 032143.mp4"

2. GPU 不可用
bash
python -c "import torch; print(torch.cuda.is_available())"
# 返回 False 则重装 GPU 版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 --force-reinstall


3. AMP 检查卡住
RTX 5070 新显卡兼容性问题，等待几分钟或使用 CPU 训练：

bash
yolo detect train data=dataset.yaml model=yolov8n.pt epochs=100 device=cpu


4. 找不到图片或标注
检查 dataset.yaml 中的路径是否正确：

path 是项目根目录

train/val 是相对于 path 的路径

5. 电脑自动睡眠中断训练
bash
# 禁止睡眠
powercfg /change standby-timeout-ac 0

# 训练完成后恢复
powercfg /change standby-timeout-ac 60


📈 训练效果
指标	数值
训练图片数	158 张
验证图片数	40 张
类别数	3 种
训练轮数	100 轮
训练时间（GPU）	~15 分钟
训练时间（CPU）	~2小时

🔗 参考链接
Ultralytics YOLO 文档
https://docs.ultralytics.com/

LabelImg GitHub
https://github.com/HumanSignal/labelImg

PyTorch 官网 
https://github.com/Mumuxi8446/git
# git

Project repository.

