# LangChain 实现闭源大模型的统一

本项目的目的是将闭源大模型，如科大星火 文心一言 通义千问等闭源大模型进行Langchain的实现，即继承了langchain的BaseChatModel的实现。

（仓库初步构建，欢迎贡献源码。）

## 背景

随着AIGC的快速发展，市面上出现了越来越多的大模型，其中包括开源大模型如qwen，baichuan,chatglm等，开源的模型已经有很好社区来支持openai格式的API接口，之所以使用openai格式的API接口，很重要的一个因素是可以轻松的使用langchain(目前最流行)。但是闭源大模型由于接口不统一，导致很难使用langchain提供的生态，因为我才有想法构建本项目。

## 支持的闭源模型

* [X] 讯飞星火
* [ ] 文心一言
* [ ] 通义千问
* [ ] 百川

## 安装

```sh
pip install --upgrade langchain_api
```

## 示例代码

```python

from langchain_api import ChatSpark
from dotenv import load_dotenv  # 加载 APP_ID 等配置
load_dotenv()

if __name__ == "__main__":
  
    llm = ChatSpark()
    # # 测试 string  ok
    ret = llm.predict("你是谁",stop=['科大讯飞'])
    print(ret)
    # 测试 message  ok
    # ret = llm.predict_messages([ChatMessage(role="user",content="你是谁")])
    # print(ret)
    # 测试 invoke  ok
    # ret = llm.invoke("你是谁")
    # print(ret)
    # 测试流式
    # for i in llm.stream("你是谁"):
    #     print(i)


```

## 致谢

**[spark-ai-python](https://github.com/iflytek/spark-ai-python)    参考并引用**

**[langchain](https://github.com/langchain-ai/langchain)    参考并引用**
