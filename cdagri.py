import time
from playwright.sync_api import sync_playwright


with sync_playwright() as b:
    browser = b.chromium.launch(
        headless=False,    # 是否为无头浏览器
        slow_mo=1000,
        ignore_default_args=['--enable-automation'],    # 浏览器出现`Chrome正受到自动测试软件的控制`
        args=[
            '--disable-blink-features=AutomationControlled',    # 跳过对WebDriver的监控,解决反爬
        ],
        executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe"    # 本地Chrome安装路径
    )

    # 打开新的窗口
    page = browser.new_page()
    # 设置屏幕大小
    page.set_viewport_size({'width': 1920, 'height':1080})

    cdagri_url = "http://cdagri.chengdu.gov.cn/nyxx/c148018/cdnyxx_list.shtml"
    page.goto(cdagri_url)
    # page.wait_for_url(cdagri_url, timeout=60)
    url_list = page.query_selector_all(".list_msg>.list_item")
    for url_ele in url_list:
        img_ele = url_ele.wait_for_selector("a")
        span_ele = url_ele.wait_for_selector("span")
        print(img_ele.get_attribute("href"), "+++", img_ele.get_attribute("title"))
        print(span_ele.text_content())
        print("=========================")

    page_title = page.title()
    print("网页的名字：", page_title)

    time.sleep(600)
