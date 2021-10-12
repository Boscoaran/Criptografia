for im in ./Imagen/*.jpg                                                #recorre todos los archivos jpg de la carpeta
do 
    IMHASH=$(md5sum $echo"$im")                                         #calcula el hash del archivo con MD5
    IMHASH2=$(echo $IMHASH | cut -d " " -f1)                            #md5sum devuelve hash nombrearchivo con cut " " se queda solo con la primera palabra
    if [ $(echo $IMHASH2) = "e5ed313192776744b9b93b1320b5e268" ];       #compara el hash del archivo con el hash buscado
    then
        stegosuite "$im"                                                #usa stegosuite con el archivo
        break                                                           #como puede haber varios archivos iguales hace un break porque los demás tendran el mismo mensaje
    fi
done   
        
