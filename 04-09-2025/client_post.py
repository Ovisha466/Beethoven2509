# pip install requests 

import requests 
baseUrl = 'https://jsonplaceholder.typicode.com'

# read all posts : GET /posts 
print('Consuming : Read All Posts...')
response = requests.get(f'{baseUrl}/posts')
posts = response.json()
print(posts)

# read by id : GET /posts/1
print('Consuming : Read Post By Id == 1...')
response = requests.get(f'{baseUrl}/posts/1')
post = response.json()
print(post)

# create post : POST /posts {"userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : create post...')
post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.post(f'{baseUrl}/posts', data = post)
createdPost = response.json()
print(createdPost)

# update post : PUT /posts/1 {"userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : update post...')
new_post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.put(f'{baseUrl}/posts/1', data = new_post)
updatedPost = response.json()
print(updatedPost)

# delete post : DELETE /posts/1
print('Consuming : delete post...')
response = requests.delete(f'{baseUrl}/posts/1')
if response.status_code == 200:
    print('Post Deleted Successfully')
else:
    print('Error in deletiing the post')