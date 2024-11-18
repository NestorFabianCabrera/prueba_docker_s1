FROM mysql

WORKDIR /app

COPY . .
# Establezca el usuario predeterminado para la imagen MySQL
USER mysql 

# Establezca las variables de entorno para el nuevo usuario
ENV MYSQL_USER=external_user 
ENV MYSQL_PASSWORD=password 
ENV MYSQL_DATABASE=my_database 

EXPOSE 3306

CMD [ "mysqld" ]

