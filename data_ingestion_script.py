import requests
import psycopg2


api_url = "https://api.opencagedata.com/geocode/v1/json"
response = requests.get(api_url)
data = response.json()


conn = psycopg2.connect(
    user="docker",
    password="kelompok9",
    database="mahasiswa",
    host="database",
    port="5432",
)

cur = conn.cursor()


for item in data:
    cur.execute("INSERT INTO mahasiswa (column1, column2) VALUES(nama, alamat)", (item['ines'], item['bali']))

conn.commit()


cur.close()
conn.close()