# Este programa obtiene el valor del SLP a dia de la fecha

import scrapy
from datetime import date


class SLPSpider(scrapy.Spider):
    name = "SLPdata"
    start_urls = [
        'https://www.coingecko.com/es/monedas/smooth-love-potion?__cf_chl_jschl_tk__=PlFKEmT4yhjisukWNW5WjIjD0yMpA.pMXm0lxpuOAu4-1639514581-0-gaNycGzNCD0']

    def parse(self, response):

        SLP = response.css('.tw-text-3xl .no-wrap::text').extract()
        fecha = date.today()

        yield {'Fecha': fecha, 'PrecioUSD': SLP}
