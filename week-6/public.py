from decouple import config
import mysql.connector
db1=mysql.connector.connect(
      pool_name='my_connection_pool',
      pool_size=3,
      host=config('host',default=''),
      database=config('database',default=''),
      user=config('user',default=''),
      password=config('password',default='')
    )
