# 基于规则的简单聊天机器人
# # 基础版
# import random
#
# # 定义打招呼
# greetings = ['hello','hey','hi','你好']
# # 定义回复
# random_greetings = random.choice(greetings)
#
# # 定义"你怎么样"问题答复
# questions = ['how are you?','how are you doing?']
# responses =['OK','I am fine!','Fine!']
# # 随机一个答复
# random_responses = random.choice(responses)
#
# # 机器人运行
# while True:
#     userInput = input('请输入：')
#     if userInput in greetings:
#         print(random_greetings)
#     elif userInput in questions:
#         print(random_responses)
#     elif userInput == 'Bye!':
#         break
#     else:
#         print('小帅机器人无法识别！')

# 升级版
import random
import nltk
from nltk import word_tokenize
# nltk.download()

# 定义打招呼
greetings = ['hello','hey','hi','你好']
# 定义回复
random_greetings = random.choice(greetings)
# 定义假期话题关键词
questions = ['break','holiday','vocation','weekend']
responses =['Nice!','We went to Paris!','Not so good!']
# 随机一个答复
random_responses = random.choice(responses)
# 机器人运行
while True:
    userInput = input('请输入：')
    # 清理一下输入
    clean_input = word_tokenize(userInput)
    # 对比一下关键词
    if not set(clean_input).isdisjoint(greetings):
        print(random_greetings)
    elif not set(clean_input).isdisjoint(questions):
        print(random_responses)
    elif userInput == 'Bye!':
        break
    else:
        print('小帅机器人无法识别！')
