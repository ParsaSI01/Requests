import requests

url = "https://caspian11.cdn.asset.aparat.com/aparat-video/1b590d5055378a480016cdc454fc97a658815809-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6Ijk1ZTQxNjFlMGZhMGJlNGU3N2RlMDllYTc4NjRiMGE2IiwiZXhwIjoxNzg2NTY4MzU3LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.nJ7SKqfmgA63o-PmTzCniSl-WmWbSS7mcBPL7sB_eoc"
response = requests.get(url, stream=True)


with open("videos/video.mp4", "wb") as video:
    for data in response.iter_content(chunk_size=20):
        video.write(data)