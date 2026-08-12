from urllib.parse import urljoin
import requests
from io import BytesIO
from PIL import Image


base_url = "https://codeyad.com"
join_url = "_ipx/f_webp&q_90/codeyad/assets/images/Courses/72d3f52e-ed45-4a17-ab8c-c36ec1474589.webp"
url = urljoin(base_url, join_url)
response = requests.get(url)
content = response.content
path = BytesIO(content)


image = Image.open(path)
image.show()