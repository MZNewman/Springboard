# coding: utf-8
charizard_text = response.xpath('//script[@type="text/javascript"]/text()').getall()
type(charizard_text)
type(charizard_text[0])
import re
import json
charizard_text_new = re.sub('\n\s*dexSettings\s\W\s', '', charizard_text[0])
charizard_text_new = re.sub('\n', '', charizard_text_new)
charizard_text_dict = json.loads(charizard_text_new)
type(charizard_text_dict)
with open('charizard_text_dict.json', 'w') as outfile:
    json.dump(charizard_text_dict, outfile)
    
