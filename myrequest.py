import requests as rq

# r = rq.get('https://api.github.com/events')
r = rq.post('https://httpbin.org/post', data={'key': 'value'})
print(r)