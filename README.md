
# Welcome to the social media site. 
## these are a couple of the basic commands you will need
|commands: | arguments|
| -| -|
|follow| your username, friends name|
|newuser|your desired username, email,password|
|post|your username, message|
|feed|your username, number of posts you want to see|
|bacon-feed|your username, number out you want to go (i.e. how many levels of friends of friends you want to see), number of posts you want to see|
|search-feed|your username, search term, number of posts you want to see|


## to run the tests run these commands:
- you can run all the tests bu runnung <code> make tests-all</code>
- <code>python3 social_media.py --TEST-add-user 1 </code>
- <code>python3 social_media.py --TEST-add-post 1 </code>
- <code>python3 social_media.py --TEST-following  1 </code>
- <code>python3 social_media.py --TEST-feed  1 </code>
- <code>python3 social_media.py --TEST-feed-bacon  1 </code>
- <code>python3 social_media.py --TEST-feed-search  1 </code>
- <code>python3 social_media.py --TEST-delete-user 1 </code>
- Tip: You can run social_media.py as a script <code>./social_media --h</code>
- You can also run commands on make 
  - ex) <code> make follow </code>
