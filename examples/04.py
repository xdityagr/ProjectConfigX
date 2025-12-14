"""
Example 04 — Runtime incident response

ConfigX used to track an incident
during a live system failure.

Nothing is persisted — this is situational awareness.
"""

from configx import ConfigX
import time

cx = ConfigX()

incident_id = "INC_7781"

cx.resolve(f'incident.{incident_id}.status="investigating"')
cx.resolve(f'incident.{incident_id}.startedAt={int(time.time())}')

cx.resolve(f'incident.{incident_id}.signals.cpuSpike=true')
cx.resolve(f'incident.{incident_id}.signals.dbLatency=true')

cx.resolve(f'incident.{incident_id}.actions.restartService="auth-api"')
cx.resolve(f'incident.{incident_id}.actions.scaleUp="db-cluster"')

cx.resolve(f'incident.{incident_id}.status="mitigated"')

print("\nIncident snapshot:\n")
cx.print_tree()

print("\nIncident closed — state discarded.")
