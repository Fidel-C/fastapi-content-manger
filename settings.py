from decouple import config,Csv



SECRET=config('SECRET')
ALLOWED_ORIGINS=config('ALLOWED_ORIGINS',cast=Csv())
EXPIRY=config('EXPIRY',cast=int)


