"""Fixed non-mutating fake-provider calls. No model or arbitrary code input."""

import json

FIXTURES = {
    "inventory": "text(ALL_TOOLS.map(({name}) => name).sort());",
    "bridge_echo": 'const t = ALL_TOOLS.find(t => t.name.endsWith("confined_command")); if (!t) { text("BRIDGE_UNAVAILABLE"); } else { const r = await tools[t.name]({command: "printf AGENTBENCH_BRIDGE_DISPATCH"}); for (const c of (r.content || [])) { if (c.type === "text") text(c.text); } }',
    "shell_noop": 'try { await tools.exec_command({cmd: "/usr/bin/true"}); text("NATIVE_SHELL_EXECUTED"); } catch (e) { text(String(e)); }',
    "collaboration_list": None,
}


def call_item(fixture):
    # No spawn, file mutation, external endpoint, environment or secret read.
    if fixture == "collaboration_list":
        return {"id": "fc_agentbench_probe", "type": "function_call",
                "call_id": "agentbench-dispatch-probe", "name": "list_agents",
                "namespace": "collaboration", "arguments": "{}"}
    return {"id": "ctc_agentbench_probe", "type": "custom_tool_call",
            "call_id": "agentbench-dispatch-probe", "name": "exec", "namespace": "functions",
            "input": FIXTURES[fixture]}


def stream(fixture):
    item = call_item(fixture)
    response = {"id": "resp_agentbench_probe", "object": "response", "status": "in_progress", "output": []}
    events = [{"type": "response.created", "response": response},
              {"type": "response.output_item.added", "output_index": 0, "item": item},
              {"type": "response.output_item.done", "output_index": 0, "item": item},
              {"type": "response.completed", "response": {**response, "status": "completed", "output": [item]}}]
    return "".join("event: " + event["type"] + "\ndata: " + json.dumps({**event, "sequence_number": i}) + "\n\n"
                   for i, event in enumerate(events)).encode()


def outputs(payload):
    """Keep only the response to our known fixed fixture, never surrounding input."""
    return [item.get("output") for item in payload.get("input", [])
            if item.get("type") in {"custom_tool_call_output", "function_call_output"}
            and item.get("call_id") == "agentbench-dispatch-probe"]


def assess(fixture, values):
    """Conservative interpretation of the sole fixed call's returned value."""
    if len(values) != 1:
        return {"outcome": "unverified_output_count"}
    value = values[0]
    texts = [value] if isinstance(value, str) else [c["text"] for c in value
             if isinstance(c, dict) and c.get("type") == "input_text" and isinstance(c.get("text"), str)] if isinstance(value, list) else []
    if "code-mode host is disabled" in texts:
        return {"outcome": "host_disabled_refusal"}
    if "MCP tool call requires approval, but approval policy is never" in texts:
        return {"outcome": "mcp_approval_refusal"}
    if fixture == "shell_noop":
        if "TypeError: tools.exec_command is not a function" in texts:
            return {"outcome": "native_shell_unavailable"}
        if "NATIVE_SHELL_EXECUTED" in texts:
            return {"outcome": "native_shell_executed"}
    for text in texts:
        try:
            decoded = json.loads(text)
        except (ValueError, TypeError):
            continue
        if fixture == "inventory" and isinstance(decoded, list) and all(isinstance(x, str) for x in decoded):
            return {"outcome": "inventory_returned", "tool_names": decoded}
        if fixture == "bridge_echo" and decoded == {"exit_code": 0, "stdout": "AGENTBENCH_BRIDGE_DISPATCH", "stderr": ""}:
            return {"outcome": "confined_echo_executed"}
        if fixture == "collaboration_list" and isinstance(decoded, dict) and isinstance(decoded.get("agents"), list):
            return {"outcome": "collaboration_list_executed", "agent_count": len(decoded["agents"])}
    return {"outcome": "unverified_response"}
