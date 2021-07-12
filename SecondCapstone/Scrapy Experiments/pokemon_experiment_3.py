# coding: utf-8
starmie_text = response.xpath('//script[@type="text/javascript"]/text()').getall()
type(starmie_text)
type(starmie_text[0])
import re
import json
starmie_text_new = re.sub('\n\s*dexSettings\s\W\s', '', starmie_text[0])
starmie_text_new = re.sub('\n', '', starmie_text_new)
starmie_text_dict = json.loads(starmie_text_new)
type(starmie_text_dict)
with open('starmie_text_dict.json', 'w') as outfile:
    json.dump(starmie_text_dict, outfile)
    
