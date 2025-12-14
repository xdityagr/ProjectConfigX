"""
Example 01 — Runtime-only usage (non-persistent)

ConfigX used as an in-memory parameter engine.
Nothing is written to disk.
All state disappears when the process exits.
"""

from configx import ConfigX

# Start ConfigX (non-persistent)
cx = ConfigX()

print("\nBuilding runtime state...\n")

# Build structured parameters dynamically
cx.resolve('ui.theme="dark"')
cx.resolve('ui.language="en"')

cx.resolve('user.id="u123"')
cx.resolve('user.loginCount=1')

cx.resolve('features.newSidebar.enabled=true')
cx.resolve('features.newSidebar.rollout=50')

# Read values
print("Theme:", cx.resolve('ui.theme'))
print("User ID:", cx.resolve('user.id'))
print("Sidebar enabled:", cx.resolve('features.newSidebar.enabled'))

# Inspect entire structure
print("\nCurrent ConfigX state:\n")
cx.print_tree()

print("\nProgram exiting — no data is persisted.")
