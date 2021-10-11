for im in ./Imagen/*.jpg
do 
    IMHASH=$(md5sum $echo"$im")
    IMHASH2=$(echo $IMHASH | cut -d " " -f1)
    if [ $(echo $IMHASH2) = "e5ed313192776744b9b93b1320b5e268" ];
    then
        stegosuite "$im"
        break
    fi
done   
        