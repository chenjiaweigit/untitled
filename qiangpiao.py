# coding=utf-8
import requests
# ro1 = requests.get("https://www.baidu.com")com
# print( ro1.status_code)
# import json


# payload = {'key1':'name','key2':'sex'}

# r1 = requests.get('http://httpbin.org/get',params = payload)
# print(r1.url) #获取请求内容
# print(r1.text)#获取相应内容

# r = requests.get('https://baidu.com')
# print(r.headers['Server'])


# r = requests.get('http://httpbin.org/status/404')
#
# print(r.status_code)

# a=['10132','10131']
a = 10111
b = 2
c = 0

# while c < len(a):
while c < b:
    # print(a[c])
    d = (eval('test部门介绍') + c)
    print(d)
    url = 'http://funing.fm-dev.gagogroup.cn:31869/api/v1/article'
    headers = {
        'Accept': 'application/json, text/plain, */*'
    }
    data = {
        'title': {'test部门介绍', c},
        'type': a,
        'abstract': '十三五',
        'link': 'https://pchen66.github.io/Panolens/',
        'content': '<h2 style="margin: 2px 0px; padding: 0px; background: none; font-size: 20px; line-height: 36px; text-align: center;"><a>第一篇 指导思想、主要目标和发展理念</a></h2><p style="padding: 0px; line-height: 25.2px; font-size: 14px;"><br/></p><p style="margin: 20px; padding: 0px; line-height: 28px; font-size: 14px; color: rgb(51, 51, 51); font-family: 宋体; white-space: normal; background-color: rgb(255, 255, 255);">　　“十三五”时期是全面建成小康社会决胜阶段。必须认真贯彻党中央战略决策和部署，准确把握国内外发展环境和条件的深刻变化，积极适应把握引领经济发展新常态，全面推进创新发展、协调发展、绿色发展、开放发展、共享发展，确保全面建成小康社会。</p><p class="STYLE1" style="margin: 20px; padding: 0px; line-height: 28px; font-size: 14px; color: rgb(51, 51, 51); font-family: 宋体; white-space: normal; background-color: rgb(255, 255, 255);">　　<strong>第一章 发展环境</strong></p><p class="STYLE1" style="margin: 20px; padding: 0px; line-height: 28px; font-size: 14px; color: rgb(51, 51, 51); font-family: 宋体; white-space: normal; background-color: rgb(255, 255, 255);">　　“十二五”时期是我国发展很不平凡的五年。面对错综复杂的国际环境和艰巨繁重的国内改革发展稳定任务，党中央、国务院团结带领全国各族人民顽强拼搏、开拓创新，经济社会发展取得显著成就，胜利完成“十二五”规划确定的主要目标和任务。</p><p class="STYLE1" style="margin: 20px; padding: 0px; line-height: 28px; font-size: 14px; color: rgb(51, 51, 51); font-family: 宋体; white-space: normal; background-color: rgb(255, 255, 255);">　　积极应对国际金融危机持续影响等一系列重大风险挑战，适应经济发展新常态，不断创新和完善宏观调控，推动形成经济结构优化、发展动力转换、发展方式转变加快的良好态势。经济保持持续较快发展，经济总量稳居世界第二位，人均国内生产总值增至49351元（折合7924美元）。经济结构调整取得重大进展，农业稳定增长，第三产业增加值占国内生产总值比重超过第二产业，居民消费率不断提高，城乡区域差距趋于缩小，常住人口城镇化率达到56.1%，基础设施水平全面跃升，高技术产业、战略性新兴产业加快发展，一批重大科技成果达到世界先进水平。公共服务体系基本建立、覆盖面持续扩大，教育水平明显提升，全民健康状况明显改善，新增就业持续增加，贫困人口大幅减少，人民生活水平和质量进一步提高。生态文明建设取得新进展，主体功能区制度逐步健全，主要污染物排放持续减少，节能环保水平明显提升。全面深化改革有力推进，经济体制继续完善，人民民主不断扩大，依法治国开启新征程。全方位外交取得重大进展，国际地位显著提高，对外开放不断深入，成为全球第一货物贸易大国和主要对外投资大国，人民币纳入国际货币基金组织特别提款权货币篮子。中华民族伟大复兴的中国梦和社会主义核心价值观深入人心，国家文化软实力不断增强。中国特色军事变革成就显著，强军兴军迈出新步伐。全面从严治党开创新局面，党风廉政建设成效显著。我国经济实力、科技实力、国防实力、国际影响力又上了一个大台阶。</p><p class="STYLE1" style="margin: 20px; padding: 0px; line-height: 28px; font-size: 14px; color: rgb(51, 51, 51); font-family: 宋体; white-space: normal; background-color: rgb(255, 255, 255);">　　尤为重要的是，党的十八大以来，以习近平同志为总书记的党中央毫不动摇坚持和发展中国特色社会主义，勇于实践、善于创新，深化对共产党执政规律、社会主义建设规律、人类社会发展规律的认识，形成一系列治国理政新理念新思想新战略，为在新的历史条件下深化改革开放、加快推进社会主义现代化提供了科学理论指导和行动指南。</p><p><br/></p>'
    }
    r = requests.post(url=url, data=data, headers=headers)
    print(r.json())
    c += 1
