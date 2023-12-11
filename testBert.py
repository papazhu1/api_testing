import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
from transformers import BertTokenizer, BertForSequenceClassification

# 加载预训练模型
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# 输入关键词
keyword = "love"

# 生成诗句和韵脚
def generate_poem(keyword):
    # 使用关键词生成诗句
    poem = model.generate(keyword)
    # 使用关键词生成韵脚
    rhyme = model.generate(keyword)
    return poem, rhyme

# 生成诗句和韵脚
poem, rhyme = generate_poem(keyword)

# 打印结果
print("Poem: ", poem)
print("Rhyme: ", rhyme)