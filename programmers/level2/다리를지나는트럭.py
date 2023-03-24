from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
     
    bridge = deque([0]*bridge_length)

    truck_weights = deque(truck_weights)
    
    bridge_sum = 0

    while bridge:
        answer += 1
        truck = bridge.pop()
        bridge_sum -= truck
        
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge_sum += truck
                bridge.appendleft(truck)
            else:
                bridge.appendleft(0)
        
    return answer

    