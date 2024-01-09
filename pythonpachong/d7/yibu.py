import time
from multiprocessing import Process


def get_request(url):
    print("请求网址数据:", url)
    time.sleep(2)
    print("请求完毕", url)


if __name__ == "__main__":
    start = time.time()
    urls = ['a.com', 'b.com', 'c.com']
    # 存储创建的的子进程
    p_list = []
    for url in urls:
        p = Process(target=get_request, args=(url,))
        p_list.append(p)
        p.start()

    for pp in p_list:
        pp.join() #意味着：主进程需要等待所有执行了join操作的子进程结束后再结束

    end = time.time()
    print( "总耗时是:", end-start)
