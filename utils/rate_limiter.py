from functools import wraps
from fastapi import HTTPException, Request,status
import time


#custom rate limiter
def rate_limit(max_calls:int, time_frame:int):
    def decorator(func):
        calls=[]
        @wraps(func)
        async def wrapper(req:Request,*args,**kwargs):
            now=time.time()
            calls_in_time=[call for call in calls if call > now-time_frame]
            if len(calls_in_time)>=max_calls:
                raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail='Rate limit exceeded.')
            calls.append(now)
            return await func(req, *args, **kwargs)
        return wrapper
    return decorator
    
    