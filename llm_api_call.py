# 【伪代码】基于通义千问API的推广话术生成工具
# 说明：此为核心逻辑伪代码，展示API调用与话术生成的核心思路

import requests
import json

# 1. 配置大模型API参数（以通义千问为例）
API_KEY = "your_api_key"  # 注：实际使用时替换为个人API Key
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# 2. 定义推广话术生成函数
def generate_promotion_text(scene, product, customer_type):
    """
    生成适配不同场景的推广话术
    :param scene: 推广场景（如朋友圈、私信、群聊）
    :param product: 推广产品名称
    :param customer_type: 客户类型（如新手、老客户）
    :return: 生成的推广话术
    """
    # 构造结构化Prompt（核心Prompt工程思路）
    prompt = f"""
    你是一名专业的线上推广专员，请根据以下信息生成适配的推广话术：
    1. 推广场景：{scene}
    2. 推广产品：{product}
    3. 客户类型：{customer_type}
    要求：
    - 话术简洁，不超过50字
    - 贴合对应场景的语言风格
    - 突出产品核心卖点
    - 避免夸大、虚假宣传
    """
    
    # 构造API请求参数
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    # 调用API（核心逻辑，实际需处理异常、重试等）
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return "话术生成失败，请重试"

# 3. 测试函数（示例调用）
if __name__ == "__main__":
    # 测试场景：朋友圈推广AI工具给新手客户
    text = generate_promotion_text("朋友圈", "AI推广话术工具", "新手客户")
    print("生成的推广话术：", text)