class CoreSettings:
    max_workers = 5  # The total number of workers (concurrent connections)
    page_load_timeout = 30  # Total amount of time to wait before timeout of page load
    headless = True  # Start browser(s) as headless or not
    insecure_certs = True  # Accept insecure certificates
    wait_page_load = 3  # This sleep timer is issued before attempting a screenshot.
