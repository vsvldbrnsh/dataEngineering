#1
sudo docker run -it ubuntu bash
#2
sudo docker run -it python:3.9
#3 postgresql db
sudo docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /home/vsvld/Projects/dataEngZoomcamp/week_1_basics_n_setup/2_DOCKER_SQL/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
 postgres:13

#4
pip install pgcli

#5
pgcli -h localhost -p 5432 -u root -d ny_taxi

#6 entire dataset link
https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
# 6.1 Yellow Trips Data Dictionary
https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

#7 get link to one chunk
https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv

#8 head first 100 rows and write in file
head -n 100 yellow_tripdata_2021-01.csv > yellow_head100.csv

#9 count number of rows 
wc -l yellow_tripdata_2021-01.csv

#10 docker pull pgadmin
sudo docker run -it \
    -e 'PGADMIN_DEFAULT_EMAIL=admin@admin.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=root' \
    -p 8080:80 \
  dpage/pgadmin4

#11 we need to create a common network container and include both postgresql and pgadmin images
sudo docker network create pg-network

#12 for now we need to launch postgresql image with network option
sudo docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v /home/vsvld/Projects/dataEngZoomcamp/week_1_basics_n_setup/2_DOCKER_SQL/ny_taxi_postgres_data:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg-network \
--name pg-database \
postgres:13

#13 for now we need to launch pgadmin image with network option too
sudo docker run -it \
-e 'PGADMIN_DEFAULT_EMAIL=admin@admin.com' \
-e 'PGADMIN_DEFAULT_PASSWORD=root' \
-p 8080:80 \
--network=pg-network \
--name pgadmin \
dpage/pgadmin4

#14 execute python script with all params
URL="https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"

python data_ingest.py \
    --user=root \
    --password=root  \
    --host=localhost \
    --port=5432  \
    --db=ny_taxi  \
    --table_name=yellow_taxi_trips \
    --url=${URL}

#15
sudo docker build -t taxi_ingest:v001 .

#16
sudo docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
  --user=root \
  --password=root  \
  --host=pg-database \
  --port=5432  \
  --db=ny_taxi  \
  --table_name=yellow_taxi_trips \
  --url=${URL}
