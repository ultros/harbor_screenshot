# harbor_screenshot
Concurrent website screenshot tool. Snap a screenshot of the initial webpage loaded.

This is useful when used with a port scanner.

### Formatting Wordlist for Program Argument
This method utilizes an active portscan database from the "harbor.py" portscanner.

This method dumps all port scan results where the port is equal to 80 to test.txt.

The data is formatted and saved to the clipboard.

    sqlite3 databases/harbor.db
    sqlite> .output test.txt
    sqlite> select ip from hosts where port == 80;
    cat test.txt|tr '\n' ' '|xclip -sel clip


### Example Screenshots  

![image](https://user-images.githubusercontent.com/2483361/201503029-72c45603-4d4a-41d3-974d-77ae9326a381.png)
![image](https://user-images.githubusercontent.com/2483361/201503032-8033c7a3-4342-462e-8395-53cf48fd3aba.png)