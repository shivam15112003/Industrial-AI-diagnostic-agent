# Safety boundary

This repository exposes **read-only analysis concepts only**.

Not provided: control writes, sequence start/stop, setpoint changes, alarm acknowledgement, recipe modification, configuration changes, service control, historical-data modification, credential handling, or remote-machine management.

A production deployment should enforce authorization outside the LLM, use explicit tool allowlists, log tool calls, constrain query sizes, and require human approval for any future write capability.
