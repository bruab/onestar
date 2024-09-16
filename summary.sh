#!/bin/bash

# Summarize chapters, topics in the book

## Count chapters
echo "Total chapters: "
ls -A _posts | wc -l

## Count categories
for x in acting art film literature music philosophy science; do echo $x; grep "^categories.*"$x _posts/* | wc -l;  done

