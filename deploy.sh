#!/bin/bash

set -xeo

main() {
  DATE=$(date)
  find . -name .DS_Store -exec rm -f '{}' \;
  git add --all
  git commit -m"${DATE}"
  git push https://makosonm@github.com/makosonm/notes.git
  git pull
}

main
