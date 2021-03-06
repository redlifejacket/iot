#!/usr/bin/python
# Shyam Govardhan
# 26 December 2018
# Coursera: Interfacing with the Raspberry Pi
# Week 3 Assignment

from twython import Twython
from twython import TwythonStreamer

execfile("tweet_init.py")

tweetCount = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global tweetCount
        if 'text' in data:
            tweetCount += 1
            print("Found it: tweetCount(%d)" % tweetCount)
        if (tweetCount >= 3):
            print("Ian G. Harris is popular!")

stream = MyStreamer(c_k, c_s, a_t, a_s)
stream.statuses.filter(track="Ian G. Harris")
