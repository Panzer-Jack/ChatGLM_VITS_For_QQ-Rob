from config import SPEAKER
from Vits_vioce_API import vits_voice
from translateBaidu import translate


# par_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(par_dir)

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model = model.eval()


def chatGLM_ask(askText, history, lang=0, isVoice=0):
	response, history = model.chat(tokenizer, askText, history=history)
	print(response)
	if not isVoice:
		pass
	else:
		if lang == 0:
			resJap = translate(response)
			vits_voice(txt=resJap, speaker=SPEAKER, language=lang)
		elif lang == 1:
			vits_voice(txt=response, speaker=SPEAKER, language=lang)
	print("out")
	return history, response


# 78 柚子社-宁宁
# 测试用：
# vits_voice(txt='FTPサーバーを構成するための機能が組み込まれています。', speaker=79, language=0)

# 測試用
if __name__ == '__main__':
	history = []
	while 1:
		msg = input('请输入：')
		chatGLM_ask(msg, history=history)
