import requests

REQUESTS_STATUS_CODE = 200
mp3_link = '' # add link to file here

if __name__ == '__main__':
    req = requests.get(mp3_link, stream=True)
    if = req.status_code == REQUESTS_STATUS_CODE:
        with open('my_song.mp3', wb) as f:
            f.write(req.content)