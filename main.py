import pyttsx3
from bs4 import BeautifulSoup
import requests

# 朗读文本
def speak(text):
    engine = pyttsx3.init() # 初始化
    # 人声类型
    voices = engine.getProperty('voices') 
    engine.setProperty('voices', voices[0].id)
    # 语速, 范围在0-500之间
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    # 音量, 范围在0-1之间
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 0.8)

    engine.save_to_file(text, 'news.mp3') # 先保存音频到本地
    engine.say(text) # 朗读
    engine.runAndWait()
    engine.stop()

def main():
    try:
        url = 'https://cc-times.com/' # 柬中时报最新消息
        resp = requests.get(url)
        resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
        soup = BeautifulSoup(resp.text, 'html.parser') # 通过html dom解析器采集数据
        
        data = []
        ret = soup.select(".general-post > div.row")
        for item in ret: # 逐条取出
            title = item.select_one('.title').getText(strip=True)
            if title != '': # 标题为空则略过
                data.append(title)
        text = ' '.join(data) # 将列表转字符串, 并以空隔作分隔

        speak(text) # 朗读新闻
        print('操作成功')
    except:
        print('操作失败')

if __name__ == '__main__': # 主入口
    main()