from sklearn.feature_extraction.text import TfidfVectorizer

tf_idf = TfidfVectorizer()

corpus = ['今天 下雪 了','小明 每天 骑车 上班','我 爱 中国']
result = tf_idf.fit_transform(corpus).toarray()
print(result)

# 统计关键词
word = tf_idf.get_feature_names_out()
print(word)

# 统计关键词出现的位置
for k,v in tf_idf.vocabulary_.items():
    print(k,v)