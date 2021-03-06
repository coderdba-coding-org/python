import multiprocessing.dummy
import multiprocessing

def ping(ip):
   success = # Run the ping command here
   if success:
       print("{} responded".format(ip))
   else:
       print("{} did not respond".format(ip))
   return success

def ping_range(start, end):
    num_threads = 2 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    p.map(ping, [10.0.0.x for x in range(start,end)])

if __name__ == "__main__":
    ping_range(0, 255)
