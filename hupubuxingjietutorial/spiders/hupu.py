# -*- coding: utf-8 -*-
import re
import time
import scrapy

from hupubuxingjietutorial.items import HupubuxingjietutorialItem


class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/bxj']
    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         }
    # }
    def parse(self, response):


        #单页面上所有的帖子迭代器
        posts = response.css('ul.for-list li')
        for post in posts:
            item = HupubuxingjietutorialItem()
            #标题
            title=post.css('.titlelink .truetit::text').extract_first()
            #亮帖数
            light_count=post.css('.titlelink .light_r a::attr(title)').extract_first(default='0')

            light_count=re.sub("\D",'',light_count).strip()

            #帖子url
            url=post.css('.titlelink a.truetit::attr(href)').extract_first()
            post_id=re.sub('\D','',url).strip()
            post_url = response.urljoin(url)

            #po主名
            author=post.css('.author .aulink::text').extract_first()
            #po主主页
            author_url=post.css('.author .aulink::attr(href)').extract_first()
            #创建时间
            try:
                create_date=post.css('div.author a')[1].css('::text').extract_first()
            except Exception as e:
                create_date=post.css('div.author').css('::text').extract_first()
            # #回复数
            # reply_num=post.css('span.ansour::text').extract_first().strip()
            # 回复数量
            reply_num = post.css('span.ansour::text').extract_first().split('/')[0].strip()
            # 浏览量
            page_views = post.css('span.ansour::text').extract_first().split('/')[1].strip()
            #最后回复时间
            last_reply_time=post.css('div.endreply a::text').extract_first()
            #最后回复人
            last_reply_user=post.css('div.endreply span::text').extract_first()

            item['title'] = title
            item['light_count'] = light_count
            item['post_id'] = post_id
            item['post_url'] = post_url
            item['author'] = author
            item['author_url'] = author_url
            item['create_date'] = create_date
            item['reply_num'] = reply_num
            item['page_views'] = page_views
            item['last_reply_time'] = last_reply_time
            item['last_reply_user'] = last_reply_user
            yield item
        # next_url=response.css('div#container div.showpage div.page div a.nextPage::attr(href)').extract_first()
        # next_url=response.urljoin(next_url)
        # print('next_url:',next_url)
        for i in range(2,500):
            #time.sleep(1)
            next_url='https://bbs.hupu.com/bxj-%s'%i
            yield scrapy.Request(url=next_url,callback=self.parse,cookies={'_dacevid3': '19cb4e0d.0d25.b32d.e2b9.d2ec7391c63b', ' __gads': 'ID', ' _HUPUSSOID': '9f341d1e-b9aa-460c-a6fc-a4b8ce13570b', '_CLT': '918ebe7bb324d8673460f7af1d701a5c', ' AUM': 'dga8cu1OnV5mB-VFu_CeV3y3jN5nt-yqlWtWpTno5j7lw', ' u': '19047383|5bCP5bCP5qKF6KW/5qKF|1cf4|f9885d67395e47f2f420ad7135db85d7|395e47f2f420ad71|5bCP5bCP5qKF6KW/5qKF', ' us': '1192d7fc8b7914c78efce925520b3a42012808a0930ebd0e672f2fc60ab52cfc18bdb36826c245f9dbfb8d4c5dcf04cd3776b54963840aa197b4a76ae95c1c8a', ' ipfrom': '5169a4176d36bec1a050d2f0b8fca77f%09Unknown', ' PHPSESSID': '99166124fc651a240fdbf676b4ec0b5e', '_cnzz_CV30020080': 'buzi_cookie%7C19cb4e0d.0d25.b32d.e2b9.d2ec7391c63b%7C-1', ' lastvisit': '1913%091533694560%09%2Fajax%2Fcard.php%3Fuid%3D19164340%26ulink%3Dhttps%253A%252F%252Fmy.hupu.com%252F277116433534759%26fid%3D34%26_%3D1533694560799', ' Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e': '1533625064,1533693253,1533693447,1533705855', 'ua': '18258437', ' _fmdata': 'MgQrIv4kS%2FjjJsM%2BslrluREYnSz7XVlcD6TUnnq3%2FEOSsa3lt2LXkBJWoq6smZq8rXDi9LlUugj9%2F0f2RbxrYG1vDlIwWaQWFTdqElvwJAM%3D', ' __dacevst': '32bde05a.5045a771|1533714672472'},dont_filter=True)
