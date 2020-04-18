from lrucache import LRUCache

def main():
    testLRU = LRUCache(3)
    testLRU.put(1,"Hyd")
    testLRU.put(2,"Mumbai")
    testLRU.put(3,"Delhi")
    
    assert testLRU.cache == {1: "Hyd", 2: "Mumbai", 3: "Delhi"}
    print("Test case1 passed")

    assert testLRU.get(2) == "Mumbai"
    print("Test case2 passed")

    assert testLRU.cache == {1: "Hyd", 3: "Delhi", 2: "Mumbai"}
    print("Test case3 passed")

    assert testLRU.get(5) == -1
    print("Test case4 passed")

    testLRU.put(4,"Chennai")
    assert testLRU.get_cache() == {3: "Delhi", 2: "Mumbai", 4: "Chennai"}
    print("Test case5 passed")
    
    print("All test cases passed")

if __name__ == "__main__":
    main()