def topKFrequent(words, k):
    # 1. 统计频率
    count = Counter(words)

    # 2. 维护大小为 k 的最小堆
    #    堆元素: (-频率, 字符串)
    #    为什么是负频率？因为 Python 是最小堆，负频率让频率高的排前面
    #    频率相同时，按字典序升序（Python 默认行为）
    heap = []
    for word, freq in count.items():
        heapq.heappush(heap, (-freq, word))
        if len(heap) > k:
            heapq.heappop(heap)  # 弹出最小的（频率最低或字典序最大）

    # 3. 从堆中弹出并排序
    #    堆中元素: (-freq, word)
    #    弹出顺序: 频率从高到低，字典序从小到大
    result = []
    while heap:
        neg_freq, word = heapq.heappop(heap)
        result.append((word, -neg_freq))

    # 注意：堆弹出的顺序已经是按 -freq 升序，即 freq 降序
    # 但 Python 堆弹出时，相同 -freq 的会按 word 升序弹出
    # 最后反转一下，让频率最高的在最前面
    result.reverse()
    return result