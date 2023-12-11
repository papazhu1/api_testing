
import random
from http import HTTPStatus
import dashscope

dashscope.api_key = "sk-b8c3a3b1e4844603af35db1a8c21827e"

str1 = "青少年可以使用平台来创作自己的诗词作品。通过输入关键词或主题，平台可以生成与之相关的诗句和韵脚，为青少年提供丰富的诗词资源，帮助拓展创作思路提高写作水平。仿造现有的诗句，下面是学生输入的题目："
def call_function(request_code, title):
    res = None
    if request_code == 1:
        res = creation_of_poem(title)
    elif request_code == 2:
        res = creation_of_story(title)
    elif request_code == 3:
        res = analysis_of_classical_chinese(title)
    elif request_code == 4:
        res = professional_planner(title)
    elif request_code == 5:
        res = psychological_counselor(title)
    return res

def creation_of_poem(title):
    context = "青少年可以使用平台来创作自己的诗词作品。通过输入关键词或主题，平台可以生成与之相关的诗句和韵脚，为青少年提供丰富的诗词资源，帮助拓展创作思路提高写作水平。下面是学生输入的题目："
    title, output = call_with_messages(context, title)
    return title, output

def creation_of_story(title):
    context = "该功能是通过对话的形式来生成一个小故事，汇集青少年零碎的奇思妙想，帮助他们更好地进行表达描述，将美好的想法形成一个完整的故事。下面是学生的输入："
    title, output = call_with_messages(context, title)
    return title, output

def analysis_of_classical_chinese(title):
    context = "青少年可以将日常用语转换为文言文，还能够和平台进行文言文对话。将语文学习中晦涩难懂的文言文与生活中的日常对话结合起来，帮助青少年更好地体会中华传统文化。下面是学生的输入："
    title, output = call_with_messages(context, title)
    return title, output

def professional_planner(title):
    context = "根据青少年设定的学习目标，指定合理的学习计划，激励其达成目标。在进行学业方向的决策时，平台可结合青少年目前情况提供阶段化建议，帮助青少年更为清晰地认知自我，认清前路。下面是学生的输入："
    title, output = call_with_messages(context, title)
    return title, output

def psychological_counselor(title):
    context = "在青少年情绪低落时，通过与平台的对话倾诉，让平台更好了解青少年的状况和经历，同时给出良好的建议帮助其摆脱情绪低谷。下面是学生的输入"
    title, output = call_with_messages(context, title)
    return title, output

def call_with_messages(context, title):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': context + title}]
    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        # set the random seed, optional, default to 1234 if not set
        seed=random.randint(1, 10000),
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
    return title, response.output.choices[0].message.content

if __name__ == '__main__':
    # request_code = 1-5 为调用5个函数中的一个函数
    request_code = 5
    title = "我这次考试没有考好，非常难过"
    title, output = call_function(request_code, title)
    print("request_code:", request_code)
    print("title")
    print(title)
    print("output")
    print(output)


