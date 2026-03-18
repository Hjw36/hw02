# HW02 作业提交

## 任务一：论文导读
### 论文标题：Hybrid CNN-Mamba: A Unified Framework for Visual Recognition

#### 1. 研究背景与动机
近年来，卷积神经网络（CNN）凭借强大的局部特征提取能力，长期主导视觉任务；而 Mamba 作为新型状态空间模型（SSM），能以线性复杂度高效建模长序列，在 NLP 领域表现突出。但纯 Mamba 模型在图像这类网格数据上，局部特征捕捉能力不足，而纯 CNN 模型又难以处理长距离依赖。因此，本文提出 Hybrid CNN-Mamba，旨在结合两者优势，构建一个统一高效的视觉识别框架。

#### 2. 核心方法
模型整体架构分为两大模块：
- **CNN 局部特征提取模块**：沿用经典卷积层，负责捕获图像的局部纹理、边缘等基础特征，保留空间位置信息。
- **Mamba 长序列建模模块**：将 CNN 输出的特征图展平为序列，通过 Mamba 高效建模全局依赖，捕捉长距离语义关联。
- **特征融合层**：通过注意力机制加权融合两类特征，使模型同时具备局部精细感知和全局上下文理解能力。

![模型结构](hybrid_cnn_mamba_arch.png)
*图注：Hybrid CNN-Mamba 模型整体架构，左侧为 CNN 特征提取，右侧为 Mamba 序列建模，底部为特征融合*

#### 3. 主要实验结果
在 ImageNet-1K 图像分类任务中：
- 相比纯 CNN 模型（如 ResNet50），Top-1 准确率提升 2.3%，参数量减少 15%；
- 相比纯 Mamba 视觉模型（如 Vision Mamba），推理速度提升 18%，小样本场景下泛化性更好；
- 在目标检测（COCO）和语义分割（ADE20K）任务中，均取得了优于基线模型的性能。

![实验结果](hybrid_cnn_mamba_result.png)
*图注：ImageNet-1K 上不同模型的 Top-1 准确率与参数量对比*

#### 4. 个人小结
Hybrid CNN-Mamba 证明了「卷积 + 状态空间模型」的融合思路在视觉任务中的可行性，既保留了 CNN 的归纳偏置，又发挥了 Mamba 的长序列效率。未来可进一步探索轻量化结构和多模态扩展，为端侧视觉应用提供更高效的方案。

---

## 任务二：Chatbot 示例代码
### 功能说明
实现了一个简单的 Chatbot，通过 OpenAI 兼容接口调用 DeepSeek 模型，支持发送问题并获取模拟回复（Mock 模式）。

### 运行方式
1. 安装依赖：`pip install openai`
2. 替换代码中的 `api_key` 为你的 DeepSeek API Key
3. 运行：`python chatbot_deepseek.py`

### 代码文件
- `chatbot_deepseek.py`：主程序代码
