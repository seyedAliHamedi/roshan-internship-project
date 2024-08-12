import scrapy


class ZoomitSpider(scrapy.Spider):
    name = 'zoomit'
    start_urls = ['https://www.zoomit.ir/sitemap.xml']

    def parse(self, response):
        sitemap_urls = response.xpath(
            '//s:sitemap/s:loc/text()', namespaces={'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}).getall()
        for url in sitemap_urls:
            if 'article' in url:
                yield scrapy.Request(url, callback=self.parse_article_sitemap)

    def parse_article_sitemap(self, response):
        article_urls = response.xpath(
            '//s:url/s:loc/text()', namespaces={'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}).getall()
        for url in article_urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        title = response.xpath(
            '//h1[@class="typography__StyledDynamicTypographyComponent-t787b7-0 fzMmhL"]/text()').get()

        description = response.xpath(
            '//meta[@name="description"]/@content').get()
        categories = response.xpath(
            '//div[@class="flex__Flex-le1v16-0 kDyGrB"]/a/span[@class="typography__StyledDynamicTypographyComponent-t787b7-0 cHbulB"]/text()').getall()

        yield {
            'url': response.url,
            'title': title.strip() if title else None,
            'description': description.strip() if description else None,
            'categories': [cat.strip() for cat in categories] if categories else None
        }
