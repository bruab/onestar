#!/usr/bin/python3

## Iterate through One Star chapters
## Output markdown file of full book
##   alphabetical by author, with footnotes

import os
import yaml

def get_contents(s):
    split_contents = s.split('---')
    return split_contents[2]

posts_dir = os.getcwd() + '/_posts'
for filename in os.listdir(posts_dir):
   with open(os.path.join(posts_dir, filename), 'r') as f: # open in readonly mode
      filestring = f.readlines()
      print(filestring)
      the_yaml = yaml.safe_load_all(f)
      #frontmatter = next(the_yaml) ## TODO this fails
      #print(frontmatter)
      #print(get_contents(filestring))

