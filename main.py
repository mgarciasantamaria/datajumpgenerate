#!/usr/bin/env python
#_*_ codig: utf8 _*_
import datetime, boto3, psycopg2, time, os
from dateutil.relativedelta import relativedelta
from humanize import naturalsize
from Modules.Constants import *
from Modules.functions import *

if Flag_Status('r'):
    mgarcia_session=boto3.Session(profile_name='pythonapps')
    s3=mgarcia_session.client('s3')
    psql_db=psycopg2.connect(db_data_connect)
    psql_cursor=psql_db.cursor()
    date_now=datetime.datetime.now()
    date=date_now-relativedelta(days=1)
    date_sql=str(datetime.datetime.strftime(date, "%Y-%m-%d"))

    file_name=f"Segmentosv2_{date_sql}.csv"
    file_path=f"{jumpsdata_Path}/{file_name}"

    csv_file=open(file_path, 'w')
    SQL=f"COPY (SELECT datetime,client,contentid,mediaid,ip,duration,type FROM new_segmentos WHERE DateTime LIKE '%{date_sql}%') TO STDOUT WITH CSV HEADER"
    psql_cursor.copy_expert(SQL, csv_file)
    csv_file.close()
    psql_cursor.close()
    psql_db.close()
    time.sleep(10)
    s3.upload_file(file_path, bucket, file_name)

    file_size=naturalsize(os.path.getsize(file_path))
    mail_subject=f'Data Jumps Generate {file_name}'
    texto=f"{file_name} ({file_size}) Archivo de datos generado y subido al bucket jumpdata en AWS S3"
    Send_Mail(texto, mail_subject)
    time.sleep(60)
    os.remove(file_path)
else:
    Send_Mail('etltoolbox application failure not recognized', 'etltoolbox application failure not recognized')