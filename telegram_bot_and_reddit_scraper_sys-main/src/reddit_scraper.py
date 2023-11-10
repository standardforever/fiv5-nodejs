import os
import time
import requests
import praw
from datetime import datetime

# https://www.reddit.com/dev/api
# https://github.com/reddit-archive/reddit/wiki
# https://www.reddit.com/prefs/apps/
# https://www.section.io/engineering-education/telegram-bot-python/

class RedditScraper:
	
	def __init__(self, client_id=None, client_secret=None, user_agent_name=None, acc_username=None, acc_password=None):
		self.client_id = client_id if client_id is not None else "DcrkPn5z-cQwYLhALNMaWQ"
		self.client_secret = client_secret if client_secret is not None else "cib3qCNPQ4B2EpH7h7jNp0B9aMeciw"
		self.user_agent_name = user_agent_name if user_agent_name is not None else "agent_name"
		self.base_url = "https://www.reddit.com/api/v1"
		reddit = praw.Reddit(
				client_id=self.client_id,
				client_secret=self.client_secret,
				user_agent=self.user_agent_name,
				)
		self.acc_username = acc_username if acc_username is not None else "username"
		self.acc_password = acc_password if acc_password is not None else "password"
		

		self.authorized_reddit = praw.Reddit(client_id=self.client_id,
											 client_secret=self.client_secret,
											 password=self.acc_password,
											 user_agent=self.user_agent_name,
											 username=self.acc_username,)
		
		self.authorized_reddit.read_only = True
		
		self.subreddits = ["datascience", "MachineLearning", "dataviz", "bigdata", "datasets", "AI", "dataengineering",
					  "dataisbeautiful", "analytics", "algorithms", "deeplearning", "TimeSeries", "tensorflow",
					  "PyTorch", "artificialintelligence", "textdatamining", "ChatGPT", "transformers", "gpt3", "bert",
					  "NLP", "computervision", "reinforcementlearning", ]
		
		self.subreddit_posts_set = []
		self.submissions_collection = {}
		
	def scrape_subreddit_posts(self, top_num_x=3, subreddits_cutoff_num=None):
		retrieval_dt = datetime.now()
		subreddits_2_scrape = self.subreddits[:subreddits_cutoff_num] if subreddits_cutoff_num is not None else self.subreddits
		for subreddit_i_name in subreddits_2_scrape:
			subreddit_i = self.authorized_reddit.subreddit(subreddit_i_name)
			subreddit_i_top_x_posts = subreddit_i.top(time_filter="week", limit=top_num_x)
			subreddit_i_top_posts = [i for i in subreddit_i_top_x_posts]
			submission_i_submissions = {}
			for submission_i in subreddit_i_top_posts:
				weighted_score = submission_i.score / subreddit_i.subscribers
				submission_i_submissions[submission_i.id] = {"title": submission_i.title,
															 "weighted score": weighted_score,
															 "score": submission_i.score,
															 "url": submission_i.url}
				# submission_i_submissions[submission_i.id]["retrieved datetime"] = retrieval_dt.strftime("%Y-%m-%d_%H-%M")
				submission_i_submissions[submission_i.id]["found datetime"] = retrieval_dt.strftime("%Y-%m-%d_%H-%M")
				submission_i_submissions[submission_i.id]["updated datetime"] = retrieval_dt.strftime("%Y-%m-%d_%H-%M")
				submission_i_submissions[submission_i.id]["shared"] = False
				submission_i_submissions[submission_i.id]["shared datetime"] = None
				submission_i_submissions[submission_i.id]["subreddit name"] = subreddit_i_name
				submission_i_submissions[submission_i.id]["subreddit subscribers"] = subreddit_i.subscribers
				submission_i_submissions[submission_i.id]["rdan reddit rank"] = None
				self.subreddit_posts_set.append(submission_i)
			self.submissions_collection[subreddit_i_name] = submission_i_submissions
			# delay = (60/len(subreddit_i_top_posts))+1
			delay = ((60 / 10) * len(subreddit_i_top_posts))
			print(f"Delay: {delay} seconds")
			time.sleep(delay)
		return self.submissions_collection


if __name__ == "__main__":
	reddit_scraper = RedditScraper()
	res = reddit_scraper.scrape_subreddit_posts(subreddits_cutoff_num=2)
	print(res)
	