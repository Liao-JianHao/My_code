# import random
#
# def fun():
#     yield from [random.randrange(0, 10) for _ in range(10)]  # 构造出一个10位随机数的生成器
#
# for _ in fun():
#     print(_)


# import random
#
# iteration = [random.randrange(0, 10) for _ in range(10)]
#
# async def func(iteration: list='Iter') -> list:
#     pass


import asyncio,aiofiles,re,os
from collections import Counter
from tqdm import tqdm



file = os.path.getsize('test.txt')


async def read_file(file):

    async with aiofiles.open(file, mode='r') as f:
        contents = await f.read()
        word = Counter(re.findall(r'\w+', contents)).items()
        bar = tqdm(list(word))
        for _ in bar:
            bar.set_description("已加载：")

    return word


def func_count(rf):
    """统计"""
    yield from rf


if __name__ == '__main__':
        rfile = read_file('test.txt')
        loop = asyncio.get_event_loop()
        task = loop.create_task(rfile)
        rf = loop.run_until_complete(task)


        for i in func_count(rf):

            print(i)