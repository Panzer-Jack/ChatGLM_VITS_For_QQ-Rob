<div align="center">

<p align="center">
    <img src="https://user-images.githubusercontent.com/81006731/227700420-8083b21d-4518-4546-a956-2f68d92bd28e.png" alt="" width="300px">
</p>
    
# QQ 群聊美少女语音AI（ChatGLM 本地化版本）
    
_✨ 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 以及 [VITS-fast-fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning) + [ChatGLM](https://github.com/THUDM/ChatGLM-6B)  实现 ✨_  
    
Combination of ChatGLM and VITs anime girl AI voice and used in QQ robot
    
</div>  

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="license">
</p>

#### 介绍
 ChatGLM 和 VITS 二次元美少女AI语音 结合 并用于 QQ聊天机器人 | Combination of ChatGLM and VITs anime girl AI voice and used in QQ robot
 
#### 由于ChatGPT 对国内上墙了且訪問不太快，因此该项目会利用开源模型ChatGLM 做本地化版本
ChatGPT版本：[ChatGPT_VITS_For_QQ-Rob](https://github.com/Panzer-Jack/ChatGPT_VITS_For_QQ-Rob)


<h2 style="color:red">注意: </h2>
<ul style="color:red">
    <li>1· 你的python版本为 3.8</li>
    <li>2· 你需要下载你操作系统相對的go-cqhttp文件并放置到根目录里，你可以在后面索引1中去下载</li>
    <li>3· 你需要安装的requirements中的依赖库</li>
    <li>4· 你需要将语音模型放置到根目录中, 并重命名为: G_latest.pth, 这里你可以参考后面的索引2</li>
    <li>5. 你需要将ChatGLM模型放置到根目录的model文件夾裏, 这里你可以参考后面的索引3</li>
    <li>6. 你需要在百度翻譯API平臺上申請免費API鑰匙</li>
</ul>

### 索引：
1. [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 

2. [VITS-fast-fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning)

3. [ChatGLM](https://github.com/THUDM/ChatGLM-6B)


#### 软件架构说明
1. config.py 设置机器人语言、声音模型等包括注意中的一切重要配置，均可在注釋中找

那麽具體你可以在`config.py` 中什麽？
   - 你可以設置AI語音的语言
   - 你可以設置AI語音声音模型
   - 你可以自定義AI的初始化人物個性設定如貓娘、美少女JK等等
   - 你可以設定AI的記憶生命（《可塑性記憶》）
2. run_server.py 为启动主文件


#### 安装教程

1.  安装go-cqhttp相应系统版本并将其放置到 项目文件夹根目录 中
2.  将你的 语言模型重命名为: G_latest.pth 放置到 项目文件夹根目录 中
3.  你需要将ChatGLM模型放置到根目录的model文件夾裏
4.  安装相关依赖库
5.  注册一个百度翻譯API账号来得到百度翻譯接口的Appid和AppKey并将其填写到 config.py 中
(地址: https://fanyi-api.baidu.com/api/trans/product/desktop# )
(百度翻譯AI每月有免費限額, 認證的話 可以到 100萬字符/月 通常如果是個人範圍用的話是夠用的)
(用於翻譯日語，(GLM不支持日語輸出)，進行日語的音頻推理)


#### 使用说明

· 安装好相关运行环境。                   

· 在项目根目录的config.py中设定声音模型和语言以及ChatGPT身份令牌

· 开启go-cqhttp 来监听QQ消息

· 打开控制台 移动到项目文件夹更目录输入:
1.  ```pip3 install -r requirements.txt```
2.  ```python3 run_server ```

#### 项目现状

1. 在QQ群聊中你可以通过@机器人 来让机器人来读取你的信息
<img width="530" alt="1" src="https://user-images.githubusercontent.com/81006731/236200085-73d585fd-bf27-4c13-ae42-4ebf6ee4687d.png">
2. 可以通過指令 `宁宁酱听我指令:语音功能切换` 來開關QQ AI 的語音功能
<img width="376" alt="2" src="https://user-images.githubusercontent.com/81006731/236200133-f012480d-b930-4c85-84f5-ac255b2a18e1.png">



