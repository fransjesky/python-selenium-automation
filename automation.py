# this is a task from automation class by Aria Suseno - session 5.
# with selenium, automate the process to get title of each webpage in the list, use looping.

from selenium import webdriver


def main():
    # variables init
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    webList = [
        "https://tiket.com",
        "https://tokopedia.com",
        "https://orangsiber.com",
        "https://idejongkok.com",
    ]
    webTitle = []

    # drivers init
    driver = webdriver.Chrome(options=options)
    for website in webList:
        driver.get(website)
        webTitle.append(driver.title)

    driver.close()

    for index in range(len(webList)):
        print(f"{webList[index][8:]} - {webTitle[index]}")


main()
