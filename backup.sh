d=$(date | cut -d " " -f2)                    #fechas de hoy y de ayer
da=$(date -d yesterday | cut -d " " -f2)
m=$(date | cut -d " " -f3)
ma=$(date -d yesterday | cut -d " " -f3)
a=$(date | cut -d " " -f4)
aa=$(date -d yesterday | cut -d " " -f4)
f=$d-$m-$a
mkdir /var/tmp/backup/$f          
fa=$da-$ma-$a
u=$(logname)
if [ -d /var/tmp/backup/$fa ]                 #existe la carpeta con la fechad e ayer
then
    mysqldump -u root -p sgssi > /home/$u/multimedia/UPV/3/3.1/Sistemas-de-Gestión-de-Seguridad-de-Sistemas-de-Información/sgssi.sql      #hacer copia de seguridad
    rsync -avhb -d --compare-dest=/var/tmp/backup/$fa /home/$u/multimedia/UPV/3/3.1/Sistemas-de-Gestión-de-Seguridad-de-Sistemas-de-Información/ /var/tmp/backup/$f  #comparar con lo que esta guardado en la copia de seguridad del dia anterior
else
    mysqldump -u root -p sgssi > /home/$u/multimedia/UPV/3/3.1/Sistemas-de-Gestión-de-Seguridad-de-Sistemas-de-Información/sgssi.sql      #hacer copia de seguridad
    rsync -av /home/$u/multimedia/UPV/3/3.1/Sistemas-de-Gestión-de-Seguridad-de-Sistemas-de-Información/ /var/tmp/backup/$f               #no hay copia de seguridad del dia anterior
fi
