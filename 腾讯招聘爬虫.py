# Author:ycz
# -*- coding: utf-8 -*-
import requests
import json
import time
import random

class TencentSpider(object):
    def __init__(self):
        self.headers = {'user-agent':'mozilla/5.0'}
        self.one_url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1748260290598&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1748260401563&postId={}&language=zh-cn'

    def get_page(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        return json.loads(res.text)

    def get_data(self,html):
        # 解析一级页面html
        job_info={}
        # 依次遍历10个职位，再通过postid的值拼接二级页面的地址
        for job in html['Data']['Posts']:
            # 职位名称
            job_info['job_name']=job['RecruitPostName']
            post_id = job['PostId']
            two_url=self.two_url.format(post_id)
            # 发请求，解析出职责和要求
            job_info['job_duty'],job_info['require']=self.parse_two_page(two_url)
            print(job_info)

    # 解析二级页面
    def parse_two_page(self,two_url):
        two_html=self.get_page(two_url)
        # 职责
        duty=two_html['Data']['Responsibility']
        # 要求
        require=two_html['Data']['Requirement']
        return duty,require

    def main(self):
        for index in range(1,11):
            url=self.one_url.format(index)
            one_html=self.get_page(url)
            self.get_data(one_html)
            time.sleep(random.uniform(0.5,2))



if __name__ == '__main__':
    spider=TencentSpider()
    spider.main()
