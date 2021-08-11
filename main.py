from re import sub
import time
start = time.time()
import praw
import random
class PrawSpammer:
    times = 0
    url = ""
    score = 0
    def __init__(self, url, times):
        self.url = url
        self.times = times+1
        for i in range(0, times):
            reddit = praw.Reddit(f"bot{i}")
            submission = reddit.submission(url=f"{self.url}")
            print(f"bot{i}")
            try:
                submission.downvote()
                time.sleep(0.6)
            except Exception as e:
                print(f"bot{i} is banned")
            try:
                submission.upvote()
                self.score = submission.score
                print("success")
                time.sleep(1.4)
            except Exception as e:
                print(f"bot{i} is banned")
            time.sleep(1.8)
print("Enter the url: ")
url = input()
print("How many Votes do you want (eg:100): ")
times = input()

user = PrawSpammer(url, int(times))
end = time.time()
print(f"Successfully spammed {user.score} Upvotes in {end-start} seconds")

# https://www.reddit.com/user/happybot989/comments/p27mr2/oooo_yes/