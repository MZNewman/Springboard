# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Smogonpokemondata2021Item(scrapy.Item):
    pokemonName = scrapy.Field()
    pokemonData = scrapy.Field()
