import concurrent.futures
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import ipaddress
import re


def screencapture():
    ips = ["37.9.1.60", "37.9.0.16", "37.9.0.2", "37.9.0.4"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []

        for ip in ips:
            futures.append(executor.submit(query_ip, ip))

        for future in concurrent.futures.as_completed(futures):
            data = future.result()
            print(data)


def query_ip(ip):
    profile = webdriver.ChromeOptions()
    profile.accept_insecure_certs = True
    profile.headless = True
    profile.set_capability("http.response.timeout", 30)
    driver = webdriver.Chrome(options=profile)

    try:
        driver.get(f"http://{ip}")
    except WebDriverException as e:
        if re.search("ERR_CONNECTION_REFUSED", str(e)):
            return f"Connection Refused ({ip})"

    time.sleep(3)

    driver.save_screenshot(ip + ".png")


def main():
    screencapture()


if __name__ == "__main__":
    main()
