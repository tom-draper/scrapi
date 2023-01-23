# ScrAPI

A REST API for simple web scraping operations.

## Links

To get a list of all links featured on a webpage:

```md
https://scrapi.vercel.app/api/links?<URL>
```

```py
import requests
response = requests.get('https://scrapi-five.vercel.app/api/links?url=https://www.google.com')
print(response.json())
# [{'href': 'https://www.google.com/imghp?hl=en&tab=wi'}, {'href': 'https://maps.google.com/maps?hl=en&tab=wl'}, {'href': 'https://play.google.com/?hl=en&tab=w8'}, ...]
```

## Image

To get a list of the images on a webpage:

```md
https://scrapi-five.vercel.app/api/images?url=<URL>
```

```py
import requests
response = requests.get('https://scrapi-five.vercel.app/api/img?url=https://www.google.com')
print(response.json())
# [{'src': '/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png', 'alt': 'Google'}]
```
