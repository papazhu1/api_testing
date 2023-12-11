# 文心一言
# -*- coding: utf-8 -*
import wenxin_api # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.free_qa import FreeQA
wenxin_api.ak = "hRjxr3SMWnFTIeAkb2WcddpetC3A5rhe" #输入您的API Key
wenxin_api.sk = "iakkrwL4GfFA3s8SKMNSSYRLxikcY2LL" #输入您的Secret Key
input_dict = {
    "text": "问题：将下面的文字转化为文言文：文心一言是百度打造出来的人工智能大语言模型，具备跨模态、跨语言的深度语义理解与生成能力，文心一言有五大能力，文学创作、商业文案创作、数理逻辑推算、中文理解、多模态生成，其在搜索问答、内容创作生成、智能办公等众多领域都有更广阔的想象空间。\n回答：",
    "seq_len": 512,
    "topp": 0.5,
    "penalty_score": 1.2,
    "min_dec_len": 2,
    "min_dec_penalty_text": "。?：！[<S>]",
    "is_unidirectional": 0,
    "task_prompt": "qa",
    "mask_type": "paragraph"
}
rst = FreeQA.create(**input_dict)
print(rst)