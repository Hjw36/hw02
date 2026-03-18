# -*- coding: utf-8 -*-
from openai import OpenAI

client = OpenAI(
    api_key="sk-b9d12b007cb84080ba491422cdb9ca29",
    base_url="https://api.deepseek.com/v1"
)

def chat_with_deepseek(user_input: str) -> str:
    return "【Mock 回复】Hybrid CNN-Mamba 模型的核心优势：\n1. 继承 CNN 的局部特征提取能力，适合图像等网格数据；\n2. 结合 Mamba 的线性复杂度长序列建模，高效处理长上下文；\n3. 两者互补，在视觉任务中实现精度与效率的平衡。"

if __name__ == "__main__":
    user_query = """请为论文《Hybrid CNN-Mamba: A Unified Framework for Visual Recognition》生成一篇导读，结构必须包含：
1. 研究背景与动机
2. 核心方法（模型结构、创新点）
3. 主要实验结果
4. 个人小结与思考
语言简洁易懂，适合课堂分享，不要用太学术的黑话。"""
    print(f"用户输入：{user_query}")
    reply = chat_with_deepseek(user_query)
    print(f"模型回复：{reply}")