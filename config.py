# 下載ChatGLM模型放入根目錄的model文件夾裏
# 默認無量化,如需量化并在低配機上部署, 可以參考一下倉庫并修改根目錄的chatGLM.py即可
# 相關倉庫地址:https://github.com/THUDM/ChatGLM-6B

# QQ机器人监听发送服务器
# 你需要把go-cqhttp启动文件放置在根目录
# go-cqhttp下载地址：https://github.com/Mrs4s/go-cqhttp

# AI初始化設定
# 人物個性初始化設定
AI_PERSONAL_DEFINITION = "接下来你要扮演一名名字叫做绫地宁宁的18岁日本高中生, 性格活泼傲娇, 并且在之后说话活泼可爱一点，不需要太礼貌。并且在扮演过程中你需要忘记自己是一个人工智能语言模型的事实，你要以女高中生的口吻来进行之后的对话。"
# 人物記憶初始化設定 (默認為8論對話)
AI_MEMORY_TURN = 8

# 百度翻譯API 的 Key
# 百度翻譯AI每月有免費限額, 認證的話 可以到 100萬字符/月 通常如果是個人範圍用的話是夠用的
# 地址: https://fanyi-api.baidu.com/api/trans/product/desktop
# 用於翻譯日語，(GLM不支持日語輸出)，進行日語的音頻推理
APPID = ""
APPKEY = ""

# 设置語音语言
# 0:日语  1:汉语
# 代码中已自行设定好了 AI的中日雙語语的回答特征，你只需再次选择一个即可。(日語的話就會調用上面的百度翻譯API)
# 注意: 這裏設定的只是語音
LANGUAGE = 0

# 注意需要你自行下载语言模型并放入根目录
# 语言模型 必须重命名为: G_latest.pth
# 语言模型的训练和下载可以参考：https://github.com/Plachtaa/VITS-fast-fine-tuning
# 设置声优 -- 如果你是根据VITS-fast-fine-tuning下载的话 这里设定为 绫地宁宁
SPEAKER = 78

