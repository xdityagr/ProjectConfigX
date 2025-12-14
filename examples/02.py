"""
Example 02 — Persistent application state

ConfigX persists evolving application state across runs.
Uses:
- Write-Ahead Log (WAL)
- Snapshots
- Automatic recovery on startup

About Example : 
A smart factory that adjusts its behavior
based on sensor readings and past decisions.

State persists across runs.

"""
from configx import ConfigX
import random

cx = ConfigX(persistent=True) # Creates .configx in your cwd as your own directory's mini-db

print("\nFactory booting...\n")

# Factory identity
cx.resolve('factory.id="F-204"')
cx.resolve('factory.mode="auto"')

# Machine baseline
cx.resolve('machines.cutter.temperature=70')
cx.resolve('machines.cutter.maxSafeTemp=90')

# Read last alert count (or initialize)
try:
    alerts = cx.resolve('factory.alertCount')
except Exception:
    alerts = 0
    cx.resolve('factory.alertCount=0')

# Simulate sensor reading
current_temp = random.randint(60, 100)
cx.resolve(f'machines.cutter.temperature={current_temp}')

# Decision logic
if current_temp > cx.resolve('machines.cutter.maxSafeTemp'):
    alerts += 1
    cx.resolve(f'factory.alertCount={alerts}')
    cx.resolve('factory.lastAlert="OVERHEAT"')
    cx.resolve('factory.mode="safe"')

print("\nFactory state:\n")
cx.print_tree()

cx.close()
print("\nFactory shutdown — state saved.")
