#!/bin/bash
#----colors----#
red='\033[1;31m'
green='\033[1;32m'
blue='\033[1;36m'
yellow='\033[1;33m'

PREFIX='/data/data/com.termux/files/usr'
dir='/data/data/com.termux/files/usr/share/doc/calcupy/'

if [ -d "$dir" ];
then
    echo -e "${blue}[◉] A directory calcupy was found! Do you want to replace it? [Y/n]:"
    read usr
    if [ $usr == "Y" ];
    then
      rm -rf "$dir"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/tonmoy-islam/calcupy.git $dir;
cd $dir
echo '''#!/bin/bash
python $PREFIX/share/doc/calcupy/calc.py''' > calc;
chmod +x *
cp calc $PREFIX/bin/;
rm calc;


if [ -d "$PREFIX/share/doc/calcupy" ] ;
   then
      echo "";
      echo "[✔]Tool istalled with success![✔]";
      echo "";
      echo "[✔]====================================================================[✔]";
      echo "[✔] ✔✔✔  All is done!! You can execute tool by typing crips  !     ✔✔✔ [✔]";
      echo "[✔]====================================================================[✔]";
      echo "";
else
  echo "[✘] Installation failed![✘] ";
  exit
fi
