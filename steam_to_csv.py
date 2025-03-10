import requests
import csv

# 请将下面的 API_KEY 和 STEAM_ID 替换成你自己的
API_KEY = 'DB47FF9CA53B2DE243CD8D8B56F6D7F2'
STEAM_ID = '76561199339956907'

# 构造 API 请求 URL，include_appinfo=1 表示返回游戏名称信息
url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={STEAM_ID}&format=json&include_appinfo=1"

# 发送请求并解析返回的 JSON 数据
response = requests.get(url)
data = response.json()

# 从返回数据中提取游戏列表
games = data.get('response', {}).get('games', [])

if not games:
    print("没有找到任何游戏数据，请确认 API key 和 SteamID 是否正确，或确保你的游戏库是公开的。")
else:
    # 将游戏名称和游玩时长写入 CSV 文件
    with open('steam_games.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'playtime_forever']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for game in games:
            writer.writerow({'name': game.get('name', '未知游戏'), 'playtime_forever': game.get('playtime_forever', 0)})

    print("CSV 文件 'steam_games.csv' 已生成！")
