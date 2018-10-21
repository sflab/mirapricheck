

import bs4
import pandas as pd
import time
import urllib.request


class MiraPriRetriever:
    BASE_URL = 'https://mirapri.com'
    COLUMNS = ["image", "頭防具", "胴防具", "手防具", "脚防具", "足防具"]

    def __init__(self, interval):
        self.__df = pd.DataFrame(columns=self.COLUMNS)
        self.__interval = interval

    def get(self, index_list):
        for index in index_list:
            url = "{}/{}".format(self.BASE_URL, index)
            try:
                with urllib.request.urlopen(url) as response:
                    if 200 <= response.status <= 299:
                        data = response.read().decode('utf-8')
                        soup = bs4.BeautifulSoup(data, "html.parser")
                        images = self.__get_images(soup)
                        info = self.__get_info(soup)
                        for image in images:
                            self.__add_data(image, info)
                        print("{} is retrieved.".format(index))
                    else:
                        print("{} is not found.".format(index))
            except:
                print("{} is not found.".format(index))
            time.sleep(self.__interval)

    def to_csv(self, file_path):
        self.__df.to_csv(file_path)

    def __get_images(self, soup):
        return [element.get("src") for element in soup.select("#mainPhotos")[0].select(".slide_img")]

    def __get_info(self, soup):
        info = {}
        for item in soup.select(".mainText")[0].select(".rightContent")[0].select("tr"):
            key = item.th.getText()
            value = item.a.getText()
            info[key] = value
        return info

    def __add_data(self, image, info):
        data = {}
        data["image"] = image
        for key in info:
            if key in self.COLUMNS:
                data[key] = info[key]
        self.__df = self.__df.append(pd.Series(data=data), ignore_index=True)
