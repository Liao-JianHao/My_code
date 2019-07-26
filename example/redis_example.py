from redis import StrictRedis


r = StrictRedis.from_url('redis://127.0.0.1:6379/0')  # redis connection config(ip/port/db)

pl = r.pipeline()  # create pipeline
pl.set('a', 1)  # add date
pl.get('a')  # get date
result = pl.execute()  # execute pipeline command ==> return result
print(result)

