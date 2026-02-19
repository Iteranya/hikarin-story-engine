from typing import Any, Dict, List
from . import actions

class VNBuilder:
    def __init__(self):
        self.stack: List[Dict[str, Any]] = []

    def _add(self, data: Dict[str, Any]):
        self.stack.append(data)
        return data

    def say(self, character: Any, content: str, voice: str = None):
        # Resolve name from your SQLAlchemy Character model or string
        name = character.name if hasattr(character, 'name') else str(character)
        return self._add(actions.say(name, content, voice))

    def show(self, character: Any, sprite_name: str, position: str = "CENTER"):
        """
        Finds the sprite metadata and path directly from the database model.
        """
        # 1. Find the specific sprite for this character by name
        # We look through the 'sprites' relationship on your Character model
        sprite_entry = next(
            (s for s in character.sprites if s.sprite_name == sprite_name),
            None
        )

        if not sprite_entry:
            raise ValueError(f"Character {character.name} has no sprite named '{sprite_name}'")

        # 2. Get the path from the linked Asset object
        # This is the 'path' column from your Asset table
        asset_path = sprite_entry.asset.path

        # 3. Build the FSM dict using the real DB data
        return self._add(actions.show_sprite(
            char_slug=character.slug,
            path=asset_path,
            position=position
        ))


    def label(self, name: str):
        return self._add({"type": "label", "action": "label", "label": name})

    def choice(self, options: Dict[str, str]):
        return self._add(actions.choice(options))

    def if_equal(self, var_name: str, value: Any, branch_func):
        """
        Graceful nesting:
        vn.if_equal("gold", 10, lambda: (
            vn.say("Guard", "You may pass.")
        ))
        """
        # Create a temporary builder for the sub-actions
        sub_builder = VNBuilder()
        branch_func(sub_builder)

        return self._add({
            "type": "conditional",
            "action": "conditional",
            "condition": "equal",
            "var": var_name,
            "value": value,
            "actions": sub_builder.export()
        })

    def export(self) -> List[Dict[str, Any]]:
        return self.stack
