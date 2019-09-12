
import requests

# from HTMLTestRunner import HTMLTestRunner

#
# class Interface_test(unittest.TestCase):
#     def test_node_api(self):
        # url = "https://apijl-dev.gagogroup.cn/api/v4//user/login"
        # payload = {'username':'jilin','password':'6364d27ecb33ebccbd8ccc41dd5b91ee'}
        # response = requests.request("POST", url, data=payload).json()
        # self.assertEqual(response['name'],"吉林省")
        # self.assertEqual(response['id'],2744975532)
        # print(response.status_code)
        # print(response.text)

# payload = {'username':'jilin','password':'6364d27ecb33ebccbd8ccc41dd5b91ee'}
# r = requests.post("https://apijl-dev.gagogroup.cn/api/v4//user/login",data=payload)
# print(r.text)
# print(r.url)







# class V2exAPITestCase(unittest.TestCase):
#
#     def test_node_api(self):
#         url = "https://www.v2ex.com/api/nodes/show.json"
#         querystring = {"name":"python"}
#         response = requests.request("GET", url, params=querystring).json()
#         self.assertEqual(response['name'], 'python')
#         self.assertEqual(response['id'], 90)



# if __name__ == '__main__':
#     unittest.main()
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # filename = '/Users/chenjiawei/Desktop/desk/test' + now + 'test_restult.html'
    # fp = open(filename,"wb")
    # runner = HTMLTestRunner(stream = fp,
    #                         title = "接口测试报告",
    #                         descripyion = "测试用例执行情况：")
    # runner.run(discover)
    # fp.close()


url = 'https://apijl-dev.gagogroup.cn/api/v4//user/login'
files = (('username','jilin'),('password','6364d27ecb33ebccbd8ccc41dd5b91ee'))
r = requests.post(url,data=files)
# print(r.json())
# print(r.text)
r.text
r.encoding
# print(r.status_code)
if r.status_code == requests.codes.ok:
    print(r.status_code,"pass")
else:
    print("false")

print(requests.codes.ok)

print(r.raise_for_status(),"\n",r.cookies)
print(r.json)
print(r.url, "\n", r.text)
