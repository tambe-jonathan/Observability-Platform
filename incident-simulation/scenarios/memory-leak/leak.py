import time
import os

def simulate_leak():
    print("🚀 Starting Memory Leak Simulation...")
    # List to hold data in memory
    leak_storage = []
    
    try:
        while True:
            # Add 10MB of data every second
            leak_storage.append(' ' * 10**7) 
            print(f"📈 Allocated +10MB. Total chunks: {len(leak_storage)}")
            time.sleep(1)
    except MemoryError:
        print("💥 CRASH: System out of memory!")

if __name__ == "__main__":
    simulate_leak()
