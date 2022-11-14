import concurrent.futures
import os
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import re
import argparse
import pathlib


def process_ips(ips, port):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = []

        for ip in ips:
            futures.append(executor.submit(take_screenshot, ip, port))

        for future in concurrent.futures.as_completed(futures):
            data = future.result()
            if data:  # if error, print error
                print(data)


def take_screenshot(ip, port):
    if not os.path.exists(os.getcwd() + "/screenshots/" + ip + ".png"):
        profile = webdriver.ChromeOptions()
        profile.accept_insecure_certs = True
        profile.headless = False
        driver = webdriver.Chrome(options=profile)
        driver.set_page_load_timeout(30)

        print(f"Trying: {ip}")
        match port:
            case 80:
                try:
                    driver.get(f"http://{ip}")
                except WebDriverException as e:
                    if re.search("ERR_CONNECTION_REFUSED", str(e)):
                        return f"Connection Refused ({ip})"

                finally:
                    time.sleep(3)  # ensure page loads
                    driver.save_screenshot(os.getcwd() + "/screenshots/" + ip + ".png")

            case 443:
                try:
                    driver.get(f"https://{ip}")
                except WebDriverException as e:
                    if re.search("ERR_CONNECTION_REFUSED", str(e)):
                        return f"Connection Refused ({ip})"
                finally:
                    time.sleep(3)  # ensure page loads
                    driver.save_screenshot(os.getcwd() + "/screenshots/" + ip + ".png")




def main():
    parser = argparse.ArgumentParser(description="Screenshot Taker")
    parser.add_argument('-i', '--ip', nargs='+', required=True, type=str,
                        default=None, dest="ip",
                        help="Specify IP address or IP range to scan.")
    parser.add_argument('-p', '--port', required=True, type=int,
                        default=None, dest="port",
                        help='Specify port (E.g. 80 or 443)')

    args = parser.parse_args()

    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    process_ips(args.ip, args.port)


if __name__ == "__main__":
    main()
