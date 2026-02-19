from typing import Any, Dict

def say(name: str, content: str, voice: str = None) -> Dict[str, Any]:
    return {
        "type": "dialogue",
        "action": "say",
        "label": name,
        "content": content,
        "voice": voice
    }

def show_sprite(char_slug: str, path: str, position: str = "CENTER") -> Dict[str, Any]:
    return {
        "type": "show_sprite",
        "action": "show",
        "sprite": char_slug,
        "location": path,
        "position": position,
        "wRatio": 16, "hRatio": 9, "wFrameRatio": 4, "hFrameRatio": 8,
        "column": 7, "row": 1
    }

def choice(options: Dict[str, str]) -> Dict[str, Any]:
    return {
        "type": "choice",
        "action": "choice",
        "choice": [{"label": k, "display": v} for k, v in options.items()]
    }
