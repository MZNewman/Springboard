import scrapy
from smogonpokemondata2021.items import Smogonpokemondata2021Item
import re
import json

class Smogonpokemondata(scrapy.Spider):
    name = "my_scraper"

    #First Start Url
    start_urls = ["https://www.smogon.com/dex/ss/pokemon/"]

    def parse(self, response):
        pokemon_dex = response.xpath('//script[@type="text/javascript"]/text()').getall()
        pokemon_dex = re.sub('\n\s*dexSettings\s\W\s', '', pokemon_dex[0])
        pokemon_dex = re.sub('\n', '', pokemon_dex)
        pokemon_dict = json.loads(pokemon_dex)
        with open('scraped_data/pokedex_dict.json', 'w') as outfile:
            json.dump(pokemon_dict, outfile)
        pokemon_list = pokemon_dict['injectRpcs'][1][1]['pokemon']
        for pokemon in pokemon_list:
            pokemon_name = pokemon['name'].lower()
            url = response.url + pokemon_name
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = Smogonpokemondata2021Item()
        pokemon_info = response.xpath('//script[@type="text/javascript"]/text()').getall()
        pokemon_info = re.sub('\n\s*dexSettings\s\W\s', '', pokemon_info[0])
        pokemon_info = re.sub('\n', '', pokemon_info)
        pokemon_info_dict = json.loads(pokemon_info)
        item['pokemonName'] = eval(pokemon_info_dict['injectRpcs'][2][0])[2]['alias']
        item['pokemonData'] = str(pokemon_info_dict['injectRpcs'][2][1])
        yield item
