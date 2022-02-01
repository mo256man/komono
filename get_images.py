# https://github.com/Joeclinton1/google-images-download

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

list_keyword = ["猫", "犬"]
str_keyword = ','.join(list_keyword)    # "['猫', '犬']"という文字列

dic_args = {"keywords": str_keyword,
            "limit": 5,
            "silent_mode": True}

results = response.download(dic_args)

for keyword in list_keyword:
    print(keyword)
    for path in results[0][keyword]:
        print(path)

print("download miss:", results[1])
