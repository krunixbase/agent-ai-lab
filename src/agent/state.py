from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentState:
    user_input: str
    plan: Optional[Dict[str, Any]] = None
    steps: List[Dict[str, Any]] = field(default_factory=list)
    last_result: Optional[str] = None
    finished: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
