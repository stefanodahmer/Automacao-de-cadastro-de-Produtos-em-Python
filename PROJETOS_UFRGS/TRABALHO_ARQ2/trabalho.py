from collections import defaultdict, OrderedDict

class CacheLRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.hits = 0
        self.misses = 0

    def access(self, block):
        if block in self.cache:
            self.hits += 1
            # move to the end (mais recentemente usado)
            self.cache.move_to_end(block)
        else:
            self.misses += 1
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # remove o menos recente
            self.cache[block] = True


class CacheLFU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(int)
        self.hits = 0
        self.misses = 0

    def access(self, block):
        if block in self.cache:
            self.hits += 1
            self.freq[block] += 1
        else:
            self.misses += 1
            if len(self.cache) >= self.capacity:
                # remove o menos frequentemente usado
                lfu_block = min(self.cache.keys(), key=lambda b: self.freq[b])
                del self.cache[lfu_block]
                del self.freq[lfu_block]
            self.cache[block] = True
            self.freq[block] = 1


def simulate(accesses, capacity):
    lru = CacheLRU(capacity)
    lfu = CacheLFU(capacity)

    for block in accesses:
        lru.access(block)
        lfu.access(block)

    return {
        "LRU": {"hits": lru.hits, "misses": lru.misses},
        "LFU": {"hits": lfu.hits, "misses": lfu.misses}
    }


# -------------------------
# Exemplos de cenários
# -------------------------

# 1) Alta localidade temporal (favorece LRU)
scenario1 = [1,2,3,1,2,3,1,2,3,1,2,3]
# Localidade temporal: os mesmos blocos 1,2,3 ficam voltando rápido.
# LRU mantém esses blocos frescos e tem mais hits.


# 2) Acesso repetitivo a um subconjunto pequeno (favorece LFU)
scenario2 = [1,1,1,1,2,2,2,2,3,4,5,6,7,8,9]
# Blocos 1 e 2 são usados MUITAS vezes.
# LFU reconhece que são muito frequentes e evita tirá-los.
# LRU pode descartar cedo se eles não forem usados logo em seguida.


# 3) Híbrido
scenario3 = [1,2,3,4,1,2,5,6,1,2,7,8,1,9,2,10,1,2]

for i, sc in enumerate([scenario1, scenario2, scenario3], start=1):
    print(f"\n--- Cenário {i} ---")
    results = simulate(sc, capacity=3)
    print("LRU:", results["LRU"])
    print("LFU:", results["LFU"])
