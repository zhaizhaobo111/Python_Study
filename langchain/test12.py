# import time
#
#
# def boil_water():
#     print("开始煮⽔...")
#     time.sleep(5) # 模拟阻塞等待5秒
#     print("⽔开了！")
# def send_message():
#     print("开始发短信...")
#     time.sleep(2) # 模拟阻塞等待2秒
#     print("短信发送成功！")
# # 主程序
# def main():
#     boil_water() # 先花5秒煮⽔，期间什么也不能做
#     send_message() # ⽔开后再花2秒发短信
#————————————————————————————————————————————————————————————————————————————————————————————————————————
# 异步 IO
import asyncio

# 协程
async def boil_water():
    print("开始煮⽔...")
    await asyncio.sleep(5) # 模拟阻塞等待5秒
    print("⽔开了！")
# 协程
async def send_message():
    print("开始发短信...")
    await asyncio.sleep(2) # 模拟阻塞等待2秒
    print("短信发送成功！")
# 主协程
async def main():
    task1=asyncio.create_task(boil_water()) # 先花5秒煮⽔，期间什么也不能做
    task2=asyncio.create_task(send_message()) # ⽔开后再花2秒发短信
    await task1
    await task2
asyncio.run(main())

