#!/bin/bash

curl -fLo ~/.vim/vimrc --create-dirs https://raw.githubusercontent.com/makosonm/notes/master/scripts/vim/vimrc

cd ~/.vim
vim -es -u vimrc -i NONE -c "PlugInstall" -c "qa"
