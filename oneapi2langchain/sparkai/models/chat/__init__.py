from typing import List
import json
from sparkai.memory import ChatMessageHistory


class Header():

    def __init__(self, code: int, message: str, sid: str, status: str):
        self.code = code
        self.message = message
        self.sid = sid
        self.status = status


class Message():

    def __init__(self, content: str, role: str, index: int):
        self.content = content
        self.role = role
        self.index = index


class Choices():

    def __init__(self, status: int, seq: int, text: List[Message]):
        self.status = status
        self.seq = seq
        tmp = []
        if text:
            for m in text:
                tmp.append(Message(**m))
        self.text = tmp


class Text():
    def __init__(self, completion_tokens: int, prompt_tokens: int, total_tokens: int, question_tokens: int):
        self.completion_tokens: int = completion_tokens
        self.prompt_tokens: int = prompt_tokens
        self.total_tokens: int = total_tokens
        self.question_tokens: int = question_tokens


class Usage():
    def __init__(self, text: Text):
        if isinstance(text, Text):
            self.text = text
        else:
            self.text = Text(**text)


class Payload():

    def __init__(self, choices: Choices = None, usage: Usage = None):
        if isinstance(choices, dict):
            self.choices = Choices(**choices)
        else:
            self.choices = choices
        if usage:
            if isinstance(usage, Usage):
                self.usage = usage
            elif isinstance(usage, dict):
                self.usage = Usage(**usage)


class ChatResponse():
    def __init__(self, header: dict, payload: dict = None):
        self.header = Header(**header)
        if payload:
            self.payload = Payload(**payload)
        else:
            self.payload = None


class ChatBody():
    def __init__(self, app_id, question, uid="12345", domain="plugin", random_threshold=0, max_tokens=2048,
                 memory: ChatMessageHistory = None,top_k=1, temperature=0.4):
        self.memory = memory
        use_memory = False
        self.req_data = {
            "header": {
                "app_id": app_id,
                "uid": uid
            },
            "parameter": {
                "chat": {
                    "domain": domain,
                    "random_threshold": random_threshold,
                    "max_tokens": max_tokens,
                    "auditing": "default",
                    "temperature": temperature,
                    "top_k": top_k
                }
            },
            "payload": {
                "message": {
                    "text": [{
                        "role": "user",
                        "content": question
                    }]
                }
            }
        }
        if memory:
            use_memory = True

        if isinstance(question, list):
            # 如果用户传递自己的上下history list 则忽略memory todo need argument
            use_memory = False
            self.req_data['payload']['message']['text'] = question
        else:
            self.req_data['payload']['message']['text'][0]['content'] = question

        if use_memory:
            self.memory.add_user_message(question)
            # self.memory.to_list()
            self.req_data['payload']['message']['text'] = self.memory.to_list()

    def json(self):
        return json.dumps(self.req_data)


if __name__ == '__main__':
    a = {'header': {'code': 0, 'message': 'Success', 'sid': 'cht000c0e9c@dx187bb529b75a173541', 'status': 1},
         'payload': {
             'choices': {'status': 1, 'seq': 6, 'text': [{'content': '智能服务。', 'role': 'assistant', 'index': 0}]}}}
    c = ChatResponse(**a)
    print(c.payload.choices)
