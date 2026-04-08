"""
Cheapest Flights Within K Stops
---------------------------------
There are n cities connected by some number of flights. You are given an array
flights where flights[i] = [from_i, to_i, price_i] and three integers src, dst,
and k.

Return the cheapest price from src to dst with at most k stops. If there is no
such route, return -1.

Example:
    Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
            src=0, dst=3, k=1
    Output: 700   (0→1→3)

    Input:  n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1
    Output: 200

    Input:  n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=0
    Output: 500

Constraints:
    - 1 <= n <= 100
    - 0 <= flights.length <= (n * (n - 1) / 2)
    - 0 <= src, dst, from_i, to_i < n
    - src != dst
    - 1 <= price_i <= 10^4
    - There are no duplicate flights
    - 0 <= k < n
"""

def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert find_cheapest_price(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
    assert find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
    assert find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500
    assert find_cheapest_price(3, [[0,1,100],[1,2,100]], 0, 2, 0) == -1
    print("All tests passed!")
