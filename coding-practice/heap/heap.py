import heapq
#by default it creates min heap

arr = [3,1,4,1,5,9,2,]
print(arr)

heapq.heapify(arr) #heapify
print("Peek after heapify in max heap:", arr)
print("Peek after heapify in min heap:", arr[0]) #peek

heapq.heappush(arr,0) #push
print("Peek after push in min heap:", arr[0])

heapq.heappush(arr,-1)
print("Peek after push in min heap:", arr[0])

min_element = heapq.heappop(arr) #pop
print("Popped element in min heap:", min_element)

#max heap 
max_arr = [-x for x in arr] #negating beacuse smallest negative num is the largest positive num
# so now arr = [-3, -1, -4, -1, -5, -9, -2]
print(max_arr)
heapq.heapify(max_arr)
print("Peek after heapify in max heap:", max_arr) #peek

heapq.heappush(max_arr,-11) #push
print("Peek after push in max heap:", max_arr[0])

print("Peek element of max heap", max_arr[0])

heapq.heappop(max_arr) #pop
print("Peek after pop in max heap:", max_arr[0])

print("Printing peek element of max heap in positive form:", -max_arr[0]) #negating to get the original value









