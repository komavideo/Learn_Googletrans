from googletrans import Translator

translator = Translator()

def detect(str):
    result = translator.detect(str)
    print(result)

# detect('how are you')
# detect('こんにちは')
# detect('你好')

def translate(str, dest="zh-CN"):
    trans_result = translator.translate(str, dest)
    print(trans_result.text)

# translate('how are you')
# translate('what is your name?')
# translate('こんにちは')
# translate('你好')


translate("GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.")
translate("GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.", dest="ja")
