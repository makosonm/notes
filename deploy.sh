#!/bin/bash

main() {
    DATE=`date`
    find . -name .DS_Store  -exec rm -f '{}' \;
    git pull origin main
    git add --all
    git commit -m"${DATE}"
    git push https://makosonm@github.com/makosonm/notes.git

    git checkout master
    git merge main
    git push https://makosonm@github.com/makosonm/notes.git
}

main
