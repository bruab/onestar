#!/usr/bin/python3

## Iterate through One Star chapters
## Output markdown file of full book
##   alphabetical by author, with footnotes

import os
import yaml

def get_contents(s):
    split_contents = s.split('---')
    return split_contents[2]

chapter_titles = []
chapters = {}

posts_dir = os.getcwd() + '/_posts'
for filename in os.listdir(posts_dir):
    with open(os.path.join(posts_dir, filename), 'r') as f: # open in readonly mode
        #print("Opening file: " + filename)
        filestring = f.read()
        #print(filestring)
        frontmatter = next(yaml.safe_load_all(filestring))
        #print(frontmatter)
        title = frontmatter['title']
        category = frontmatter['categories'][0].title()
        bio = frontmatter['bio']
        body = "# " + title + '\n\n'
        body += "_" + category + ' • ' + bio + '_\n'
        body += filestring.split('---')[2]
        #print(body)
        chapter_titles.append(title)
        chapters[title] = body

for title in sorted(chapter_titles):
    print(chapters[title])
