import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json

class BookingSpider(scrapy.Spider):
    name = "booking_spider"
    
    city_list = ['Aix en Provence', 'Carcassonne', 'Cassis', 'Marseille', 'Saintes Maries de la mer']
    
    
    def start_requests(self):
 
        for city in self.city_list:
            city_encoded = city.replace(' ', '+')
            url = f"https://www.booking.com/searchresults.fr.html?ss={city_encoded}"
            yield scrapy.Request(url=url, callback=self.parse, meta={"city": city})

    def parse(self, response):

        city = response.meta["city"]

        # Extraction des URLs des hôtels (max 20 par ville)
        hotel_links = response.css("[class='a78ca197d0']").css("a[href]::attr(href)").getall()[:20]

        for hotel_link in hotel_links:
            hotel_url = response.urljoin(hotel_link)  # Ajoute le domaine si nécessaire
            yield scrapy.Request(
                url=hotel_url,
                callback=self.parse_details,
                meta={"city": city, "hotel_url": hotel_url}
            )

    def parse_details(self, response):

        yield {
            "city": response.meta["city"],
            "hotel_lat" : response.css('a#map_trigger_header::attr(data-atlas-latlng)').get().split(",")[0],
            "hotel_lon" : response.css('a#map_trigger_header::attr(data-atlas-latlng)').get().split(",")[1],
            "hotel_name": response.css("[class='d2fee87262 pp-header__title']::text").get(),
            "hotel_review" : response.css("[class='a3b8729ab1 d86cee9b25']::text").get(),
            "hotel_nbr_review" : response.css("[class='a3b8729ab1 f45d8e4c32 d935416c47']::text").getall()[1],
            "hotel_address" : response.css("[class='a53cbfa6de f17adf7576']::text").get(),
            "hotel_facilities" : response.css("[class='a5a5a75131']::text").getall(),
            "hotel_desc" : response.css("[class='a53cbfa6de b3efd73f69']::text").get(),
            "hotel_url": response.meta["hotel_url"],
        }

filename = "scrap_booking.csv"


# If file already exists, delete it before crawling (because Scrapy will concatenate the last and new results otherwise)

if filename in os.listdir(r'C:\Users\ambri\Desktop\vscodetraining\Training\FullStack\Kayak_Project/'):
        os.remove(r'C:\Users\ambri\Desktop\vscodetraining\Training\FullStack\Kayak_Project/' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'Kayak_Project_' + filename : {"format": "csv"},
    }
})

process.crawl(BookingSpider)
process.start()