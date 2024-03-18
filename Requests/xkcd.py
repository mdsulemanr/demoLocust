import requests


class NavigateCategory:
    def __init__(self):
        self.session = requests.Session()

    def view_page_via_session(self):
        response = self.session.get('https://moodle-dev.litmustest.io/')
        print(response.cookies.values()[0])

    # def view_page(self):
    #     with requests.get('https://xkcd.com/353/') as response:
    #         print(response.status_code)
    #
    # def get_headers(self):
    #     with requests.get('https://xkcd.com/353/') as response:
    #         print(response.headers)
    #
    # def download_image(self):
    #     response = requests.get('https://imgs.xkcd.com/comics/python.png')
    #     if response.ok:
    #         with open('comic.png', 'wb') as file:  # wb=write byte
    #             file.write(response.content)  # content provides image bytes


ViewPages = NavigateCategory()
# ViewPages.download_image()
