from pydelicious import get_popular,get_userposts,get_urlposts
import time
# print get_popular(tag='programming')
def initializeUserDict(tag,count=5):
	user_dict={}
	for p1 in get_popular(tag=tag)[0:count]:
		for p2 in get_urlposts(p1['url']):
			user=p2['user']
			user_dict[user]={}
	return user_dict
def fillItems(user_dict):
	all_item={}
	for user in user_dict:
		for i in xrange(3):
			try:
				posts=get_userposts(user)
			except:
				print 'Failed user'+user+',retring'
				time.sleep(4)

		for post in posts:
			url=post['url']
			user_dict[user][url]=1.0
			all_item[url]=1
	for rating in user_dict.values():
		for item in all_item:
			if item not in rating:
				rating[item]=0.0

if __name__ == '__main__':
	delusers=initializeUserDict('programming')
	delusers['tsegaran']={}
	fillItems(delusers)