"""
Example 03 — Persistent AI agent memory

ConfigX used as a long-term memory store
for an autonomous AI agent.

No schema. Memory grows organically.
"""

from configx import ConfigX
import time

cx = ConfigX(persistent=True)

print("\nAgent waking up...\n")

agent_id = "atlas"

# Initialize agent if new
try:
    cx.resolve(f'agents.{agent_id}.bootCount')
except Exception:
    cx.resolve(f'agents.{agent_id}.bootCount=0')
    cx.resolve(f'agents.{agent_id}.personality="curious"')

# Increment boot count
boots = cx.resolve(f'agents.{agent_id}.bootCount')
cx.resolve(f'agents.{agent_id}.bootCount={boots + 1}')

# Store a memory
cx.resolve(
    f'agents.{agent_id}.memory.lastObservation="User asked about persistence"'
)
cx.resolve(
    f'agents.{agent_id}.memory.timestamp={int(time.time())}'
)

print("Agent memory:\n")
cx.print_tree()

cx.close()
print("\nAgent going dormant — memory preserved.")
