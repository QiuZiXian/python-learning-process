from apscheduler.schedulers.blocking import BlockingScheduler

import os



def audio_synthesis():
    try:

        ds = [{'d':'dasdasdas','ds':'hudahdas'},{'d':'无敌','ds':'宿舍的'}]

        yu = ds['ds']

        ui = ds['d']

        iis = ds['data']
        global stop
        stop = True
        return yu + ui + iis
    except:
        scheduler.shutdown(wait=False)
        scheduler.start()
        return

def loop():
    count = 0
    while(count < 3):
        try:
            return audio_synthesis()
        except (KeyboardInterrupt, SystemExit):
            print("报错的次数为：",count)
            count += 1


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(loop, 'interval', seconds=15, id='audio_synthesis') # 每隔5分钟执行一次
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    scheduler.start()
# def start():
#     scheduler.start()
#     if stop:
#         return
#
#     print("报错的次数为：",count)
#
#
# if __name__ == '__main__':
#
#     stop = False
#     scheduler = BlockingScheduler()
#
#     scheduler.add_job(audio_synthesis, 'interval', seconds=2, id='audio_synthesis') # 每隔5分钟执行一次
#
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
#
#     count = 1
#
#     while(count < 4):
#
#         start()
#         print("报错的次数为：",count)
#         count += 1



