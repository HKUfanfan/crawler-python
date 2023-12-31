import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = "qiubai"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.qiushibaike.com/text/"]

    '''def parse(self, response):
        #解析作者的名称加上段子的内容
        div_list = response.xpath("//div[@id='content-left']/div")
        all_data = [] #存储所有解析到的数据
        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath("./div[1]/a[2]/h2/text()")[0].extract()
            #author = div.xpath("./div[1]/a[2]/h2/text()").extract_first()
            #如果extract_first()括号中不写索引，则默认取第一个

            #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = "".join(content)
            #返回的是一个列表

            dic = {
                'author': author,
                'content': content
            }

            all_data.append(dic)

            #print(author, content)
        return all_data'''
    
    def parse(self, response):
        #解析作者的名称加上段子的内容
        div_list = response.xpath("//div[@id='content-left']/div")
        all_data = [] #存储所有解析到的数据
        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath("./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()")[0].extract()
            #author = div.xpath("./div[1]/a[2]/h2/text()").extract_first()
            #如果extract_first()括号中不写索引，则默认取第一个

            #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = "".join(content)
            #返回的是一个列表

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item #将item提交给了管道

"""存储: scrapy crawl qiubai -o ./qiubai.csv"""

#糗事百科已经改版，所以这个代码已经失效了，但是思路还是可以借鉴的
