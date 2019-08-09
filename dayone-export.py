# Script to extract data from a Day One JSON export. Journal entries and metadata are printed in individual text files.

import json
import datetime

input_filename = ""
output_directory = 'out'

input = open(input_filename, 'r')
entries = json.load(input)["entries"]

# Not sure why these backslashes are present
def cleanup(text):
    text = text.replace(r'\.', '.')
    text = text.replace(r'\(', '.')
    text = text.replace(r'\)', '.')
    text = text.replace(r'\!', '.')
    text = text.replace(r'\-', '.')
    text = text.replace(r'\[', '.')
    text = text.replace(r'\]', '.')   
    return text

for entry in entries:
    creation_date = datetime.datetime.fromisoformat(entry['creationDate'].replace("Z", "+00:00"))
    output_filename = creation_date.strftime('%Y%m%d %H%M.txt')

    file = open(output_directory + '/' + output_filename, mode='w')
    print(cleanup(entry['text']), file=file)
    print('', file=file)
    print('***', file=file)
    print(creation_date.strftime('%d %B %Y  '), file=file) # N.B. two spaces for Markdown line break
    
    l = entry.get('location')
    if l is not None:
        l = l['localityName'] + ', ' + l['administrativeArea'] + ', ' + l['country']
        print(l, file=file)