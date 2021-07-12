# coding: utf-8
absol_text = response.xpath('//script[@type="text/javascript"]/text()').getall()
type(absol_text)
type(absol_text[0])
import re
import json
absol_text_new = re.sub('\n\s*dexSettings\s\W\s', '', absol_text[0])
absol_text_new = re.sub('\n', '', absol_text_new)
absol_text_dict = json.loads(absol_text_new)
type(absol_text_dict)
with open('absol_text_dict.json', 'w') as outfile:
    json.dump(absol_text_dict, outfile)
    
