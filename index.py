#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:52:16 2019

@author: madyward
"""
import subprocess, time, webbrowser

        
def openApps():
    print('1. Starting Docker & opening your daily browser tabs.')
    subprocess.Popen(['open', '../../Applications/Docker.app/'])
    
    listSites = [
        'https://mail.google.com/',
        'https://calendar.google.com',
        'https://120wateraudit.atlassian.net',
        'https://github.com'
    ]
    
    for site in listSites:
        webbrowser.open(site)
        
    time.sleep(3)
    print('2. Let\'s also check out what\'s new on Slack.')
    subprocess.Popen(['open', '../../Applications/Slack.app/'])
    
    time.sleep(15)
    print('3. What are you working on today? Opening VSCode to find out!')
    subprocess.Popen(['open', '../../Applications/VSCode.app/'])
    
    time.sleep(35)
    print('4. Now that Docker is running, we\'re opening Kitematic.')
    subprocess.Popen(['open', '../../Applications/Docker/Kitematic (Beta).app/'])
        
def startday():
    print('Good morning. Let\'s start your day!')
    openApps()
    print('Have a good one!')
    
openApps()