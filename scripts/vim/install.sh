#!/bin/bash

curl -Lo ~/.vim/vimrc --create-dirs https://raw.githubusercontent.com/makosonm/notes/master/scripts/vim/vimrc

vim -es -u ~/.vim/vimrc -i NONE -c "PlugInstall" -c "qa"
