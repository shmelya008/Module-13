import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(5/power)
        print(f'Силач {name} поднял шар № {i}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    print('Старт соревнований')
    print('________________________________')
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await task_1
    await task_2
    await task_3

    print('________________________________')
    print('Соревнования закончены')

start = time.time()
asyncio.run(start_tournament())
end = time.time()
print(f'Время работы программы {end-start} sec')


