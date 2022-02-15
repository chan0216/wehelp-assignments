from decouple import config
import mysql.connector

db=mysql.connector.connect(
      pool_name='my_connection_pool',
      pool_size=2,
      host=config('host',default=''),
      database=config('database',default=''),
      user=config('user',default=''),
      password=config('password',default=''),
    )
