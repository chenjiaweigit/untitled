# coding=utf-8
import requests
import unittest


def login_token():
    # 写法1：
    login_url = 'http://58.242.186.52:7005/nybdata/login?user_name=15200808387&pwd=1'
    header1 = {
        "Content-Type": 'application/json',
    }
    login = requests.post(url=login_url, headers=header1)
    token1 = login.json()["datas"]["token"]
    header = {
        'token': token1,
        "Content-Type": 'application/json',
    }
    # print(login.json())
    name1 = login.json()["datas"]["name"]
    # return name1
    # return login.json()["datas"]["token"]
    # return token1
    json1 = login.json()
    return json1
    # login_token()

if __name__ == '__main__':
    login_token()
    # print(login_token())
    # print("获取token成功:"" "+login_token())
    # time.sleep(5)


# unittest中TestCase方法判定
# class test_json(unittest.TestCase):
#     def test_json(self):
#         self.assertEqual(login_token()["datas"]["name"],"刘宇琳")
#
# if __name__ == '__main__':
#     unittest.main()




def Sample_analysis():
    new_token = login_token()["datas"]["token"]
    header2 = {
        "token": new_token,
        "Content-Type": 'application/json',
    }
    Sample_analysis_url = 'http://58.242.186.52:7005/nybdata/getSoilListPage?corp=&soil_plot_name=&col_point_code=&batch=&act_date_beg=&act_date_end=&pageNum=1&pageSize=10'
    Sample_analysis_get = requests.get(url=Sample_analysis_url, headers=header2)

    # print(Sample_analysis_get)
    return Sample_analysis_get.json()

    # return ybfx1


if __name__ == "__main__":
    Sample_analysis()
    # print(Sample_analysis())

# def test_new():
#     get_token=login_token()
#     # return get_token
#
#     # print(get_token)
#
#
# if __name__ == '__main__':
#     test_new()
# # print(test_new())


# unittest中TestCase方法判定
class test_json(unittest.TestCase):
    def test_json(self):
        self.assertEqual(login_token()["datas"]["name"], "刘宇琳")

    def test_Sample_analysis(self):
        self.assertTrue(Sample_analysis()["success"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
