# NLP文本处理:分词、提取文本向量、语义理解
# 文本处理方法Onehot:将类别变量转换为数字型变量(稀疏)

# Word2Vec:用神经网络把词转成向量的模型
# Cbow根据给定上下文来预测input word
# Skip-Gram给定input word来预测上下文
# Word2Vec不足:使用了唯一的词向量,对于多义词没有很好的效果,
#              context很小,没有使用全局的cooccur 对cooccur的利用少

import gzip
import gensim
import logging
logging.basicConfig(format="",level=logging.INFO)

