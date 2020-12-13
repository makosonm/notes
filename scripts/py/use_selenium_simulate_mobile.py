# <author> makosonm@gmail.com

from time import sleep

from selenium import webdriver


def main():
    """
    分别使用 device name 模式和 指定分辨率及UA标识方式
    """
    mobiles = [
        {
            "deviceMetrics": {"width": 320, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.\
                    1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
        },
        {"deviceName": "iPhone X"},
    ]
    options = webdriver.ChromeOptions()

    for mobile in mobiles:
        options.add_experimental_option("mobileEmulation", mobile)
        driver = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver",
            chrome_options=options,
            service_args=["--verbose", "--log-path=qc1.log"],
        )
        driver.get("http://m.dianping.com")

        sleep(10)
        driver.close()


if __name__ == "__main__":
    main()
