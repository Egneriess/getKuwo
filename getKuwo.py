import time
import requests
import os


def downloadMusic(url, name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
        "csrf": "RUJ53PGJ4ZD",
        "Cookie": "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD",
    }

    mid = url.split("/")[-1]
    save_mp3_url = (
        "http://www.kuwo.cn/api/v1/www/music/playUrl?mid=%s&type=mp3&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269"
        % mid
    )
    mp3_response = requests.get(save_mp3_url, headers=headers)
    mp3_url = mp3_response.json().get("data").get("url")
    with open(name + ".mp3", "wb") as file:
        music = requests.get(mp3_url, headers=headers)
        file.write(music.content)
        file.flush()
        file.close()
        print("视频下载成功")

    return name + ".mp3"


def play(path, volume):
    os.system("ffplay " + path + " -noborder -nodisp -loop -1 -volume " + volume)


def main():
    url = input("输入一首歌曲的播放地址下载歌曲:")
    name = input("请输入音乐名字:")
    volume = input("声音响度:")
    try:
        play(downloadMusic(url, name), volume)
    except KeyboardInterrupt or EOFError:
        main()


if __name__ == "__main__":
    main()
