# Natural Language Processing(NLP)
# 文本朗读、语音合成、语音识别、中文自动分词、词性标注、句法分析、自然语言生成
# 文本分类、信息检索、信息抽取、文字校对、问答系统、机器翻译、自动摘要、文字蕴涵

# NLP研究难点:单词的边界界定、词义的消歧、不规范的输入、句法的模糊性、语言行为与计划

# 词处理:分词、词性标注、实体识别、词义消歧
# 语句处理:句法分析、语义分析、机器翻译、语音合成
# 篇章处理:自动文摘

# 统计语言模型:N-Gram统计模型、马尔科夫模型、隐马尔可夫模型

# 语料:语言材料
# import nltk
# sentence = " At eight o'clock on Thursday morning Jack didn't feel so good."
# tokens = nltk.word_tokenize(sentence)
# print(tokens)
#
# tagged = nltk.pos_tag(tokens)
# print(tagged)


# 词性标注:给每个词或词语打词类标签,如形容词、动词、名词。NLTK jieba(中文分词库)
# 基于规则的词性标注
# 基于隐马尔科夫模型HMM的词性标注
# 基于转移的词性标注
# 基于转移与隐马尔科夫模型相结合的词性标注

# import nltk
# text = nltk.word_tokenize("And now for something completely different")
# print(text)
# print(nltk.pos_tag(text))

import jieba.posseg as pseg
words = pseg.cut('我爱丰小帅！')
for word,flag in words:
    print('%s %s' % (word,flag))


