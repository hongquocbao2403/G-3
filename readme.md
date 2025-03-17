docker start aapanel

docker pull aapanel/aapanel

docker run -d -p 8886:7800 -p 22:21 -p 443:443 -p 8000:80 -p 889:888 -v D:/GIAIDOAN3/website:/www/wwwroot -v D:/GIAIDOAN3/mysql_data:/www/server/data -v D:/GIAIDOAN3/vhost:/www/server/panel/vhost aapanel/aapanel:lib
