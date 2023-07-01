from pytz import timezone

from apscheduler.schedulers.background import BackgroundScheduler

from .cafe_info import update_kakao_local_cafe

scheduler = BackgroundScheduler(timezone = timezone('Asia/Seoul'))

scheduler.add_job(
    update_kakao_local_cafe, 
    trigger     = 'cron', 
    day_of_week = '1',
    id          = 'update_kakoa_local_cafe' 
)

