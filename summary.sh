#!/bin/bash

# Summarize chapters, topics in the book

## Count chapters
echo "Total chapters: "
ls -A _posts | wc -l

## Count categories
for x in art film literature music science; do echo -n "$x: "; grep "^categories.*"$x _posts/* | wc -l;  done

