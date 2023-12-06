# Efficient Comparison
import time

start_time = time.time()
    
def is_between1(x, y, L, R):
 return L < x ** y < R

print(is_between1(99,9,0,9999999999999999999))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

def is_between2(x, y, L, R):
 return x ** y > L and x ** y < R

print(is_between2(99,9,0,9999999999999999999))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

def is_between3(x, y, L, R):
 return x**y in range(L+1, R+1)

print(is_between3(99,9,0,9999999999999999999))

print("--- %s seconds ---" % (time.time() - start_time))

# outputs
# True
# --- 0.0 seconds ---
# True
# --- 0.0009999275207519531 seconds ---
# True
# --- 0.0009999275207519531 seconds ---