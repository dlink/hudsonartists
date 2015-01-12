hadb='mysql -uhudsonartists -pFireFlower5 -hlocalhost --database=hudsonartists'

hpwd=$PWD
cd $HOME/hudsonartists/sql;

cat _dangerous_drop_all.sql | $hadb && \
cat _create_all.sql         | $hadb -t --local-infile=1 > _create_all.log

cd $hpwd

