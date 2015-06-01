dhadb='mysql -uhudsonartists -pFireFlower5 -hlocalhost --database=dev_hudsonartists'

hpwd=$PWD
cd $HOME/hudsonartists/sql;

cat _dangerous_drop_all.sql | $dhadb && \
cat _create_all.sql         | $dhadb -t --local-infile=1 > _create_all.log

cd $hpwd

