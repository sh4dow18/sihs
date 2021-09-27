# Sh4dow18 Chrome-History Hack Script
from platform import system
from getpass import getuser
import sqlite3 
from re import findall


def ObtainUserPath(what_platform):
    user_path = None
    if what_platform == "Windows":
        user_path = "C:\\Users\\" + getuser()
    elif  what_platform == "Linux":
        user_path = "/home/" + getuser()
    return user_path


def ObtainChromeHistory(what_platform, user_path):
    chrome_history = None
    chrome_history_path = None
    if what_platform == "Windows":
        chrome_history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    elif what_platform == "Linux":
        chrome_history_path = user_path + "/.config/google-chrome/Default/History"
    while chrome_history is None:
        try:
            connection = sqlite3.connect(chrome_history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            chrome_history = cursor.fetchall()
        except sqlite3.OperationalError:
            print("Error, retrying...")
    return chrome_history


def ObtainYoutubeChannels(chrome_history):
    channels_visited = []
    for url_information in chrome_history:
        results = findall("https://www.youtube.com/c/([A-Za-z0-9]+)", url_information[2])
        if len(results) != 0:
            if results[0] not in channels_visited:
                channels_visited.append(results[0])
    return channels_visited


def main():
    what_platform = system()
    user_path = ObtainUserPath(what_platform)
    chrome_history = ObtainChromeHistory(what_platform, user_path)
    channels_visited = ObtainYoutubeChannels(chrome_history)
    print(channels_visited)


if __name__ == "__main__":
    main()

