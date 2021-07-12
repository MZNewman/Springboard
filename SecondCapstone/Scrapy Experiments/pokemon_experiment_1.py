# coding: utf-8
response.xpath('//div/@class).getall()
response.xpath('//div/@class').getall()
response.xpath('//div/@id').getall()
response.xpath('//div[contains(@class, "DexBody")]/header/@class').getall()
response.xpath('//div[contains(@class, "DexBody")]').getall()
response.xpath('//div[contains(@class, "Dex")]').getall()
response.xpath('//div').getall()
response.xpath('//div').get()
response.xpath('//div[contains(@id, "container")]').getall()
response.xpath('//div[@id="container")]').getall()
response.xpath('//div[@id="container"]').getall()
response.xpath('//div[@class="DexBody"]').getall()
response.xpath('//div/div[@class="DexBody"]').getall()
response.xpath('//div/div').getall()
response.xpath('//div[@id="container"]/div[@class="DexBody"]').getall()
response.xpath('//div[@id="container"]//div[@class="DexBody"]').getall()
response.xpath('//div[@id="container"].//div[@class="DexBody"]').getall()
response.xpath('//div[@id="container"]').getall()
response.xpath('//div[@id="container"].//div').getall()
response.xpath('//div[@id="container"]/div').getall()
response.xpath('//div[@id="container"]/*').getall()
response.xpath('*/div[@id="container"]').getall()
response.xpath('//div[@id="container"]/div[1]').getall()
response.xpath('//div[@id="container"]/@class').getall()
response.xpath('//div[@id="container"]/div/@class').getall()
response.xpath('//main[@class="DexContent"]').getall()
response.xpath('//div').getall()
for p in response.xpath('//div').getall():
    print(p)
    
response.xpath('//div[@class="spinner"]').getall()
response.xpath('//div[@data-reactid=".0.0"]').getall()
response.xpath('/html/body/div[1]').getall()
response.xpath('/html/body/div[1]/div[1]').getall()
response.xpath('/html/body/div[3]/div[1]').getall()
response.xpath('/html/body/div[2]/div[1]').getall()
response.css('a::attr(href)').getall()
response.xpath('//script').getall()
response.xpath('//script[type="text/javascript"]').getall()
response.xpath('//script[@type="text/javascript"]').getall()
response.xpath('//script[@type="text/javascript"]/text()').getall()
pokemon_text = response.xpath('//script[@type="text/javascript"]/text()').getall()
type(pokemon_text)
type(pokemon_text[0])
type(pokemon_text[1])
for pokemon in pokemon_text[0].split('['):
    print pokemon
for pokemon in pokemon_text[0].split('['):
    print(pokemon)
    
for pokemon in pokemon_text[0].split('['|']'):
    print(pokemon)
    
import re
for pokemon in re.split('{}[],', pokemon_text[0]):
    print(pokemon)
    
for pokemon in re.split('[],', pokemon_text[0]):
    print(pokemon)
    
for pokemon in re.split('[|]', pokemon_text[0]):
    print(pokemon)
    
for pokemon in re.split('[ | ]', pokemon_text[0]):
    print(pokemon)
    
for pokemon in re.split('[ | ]', pokemon_text[0].strip('\n')):
    print(pokemon)
    
pokemon_text
dict(pokemon_text[0])
dir(re)
pokemon_text_new = re.sub('\n\s*dexSettings\s\W\s', '', pokemon_text)
pokemon_text_new = re.sub(r'\n\s*dexSettings\s\W\s', '', pokemon_text)
pokemon_text_new = re.sub('\n\s*dexSettings\s\W\s', '', pokemon_text[0])
pokemon_text_new
re.findall('\n', pokemon_text_new)
pokemon_text_new = re.sub('\n', '', pokemon_text_new)
pokemon_text_new
dict(pokemon_text_new)
import json
pokemon_text_dict = json.loads(pokemon_text_new)
type(pokemon_text_dict)
pokemon_text_dict
pokemon_text_dict.keys()
pokemon_text_dict['injectRpcs'].keys()
pokemon_text_dict['injectRpcs']
type(pokemon_text_dict['injectRpcs'])
pokemon_text_dict['injectRpcs'][0]
type(pokemon_text_dict)
with open('pokemon_text_dict.json', 'w') as outfile:
    json.dump(pokemon_text_dict, outfile)
    
