"""
ConfigXQL - Interpreter (v0.1)

Executes ConfigXQL AST nodes against a ConfigTree instance.
This is the semantic layer that connects the language to the engine.

Design principles:
- No parsing logic here
- No storage logic here
- Pure AST -> Engine mapping

Current Version Supports :

`GET` 
GetNode(path=["app", "ui", "theme"], safe=False)
→ tree.get("app.ui.theme")

`SAFE GET`
GetNode(path=[...], safe=True)
→ returns None if missing

`SET`
SetNode(path=["app", "ui", "theme"], value="dark")
→ tree.set("app.ui.theme", "dark")

`DELETE`

DeleteNode(path=[...])
→ tree.delete("app.ui.theme")

"""

from typing import Any

from configx.qlang.parser import GetNode, SetNode, DeleteNode
from configx.core.tree import ConfigTree
from configx.core.errors import ConfigPathNotFoundError


class ConfigXQLInterpreter:
    """
    Executes ConfigXQL AST nodes against a ConfigTree.
    """

    def __init__(self, tree: ConfigTree):
        self.tree = tree

    def execute(self, node) -> Any:
        """
        Execute a single AST node.
        Returns the result of execution (if any).
        """

        if isinstance(node, GetNode):
            return self._exec_get(node)

        if isinstance(node, SetNode):
            return self._exec_set(node)

        if isinstance(node, DeleteNode):
            return self._exec_delete(node)

        raise TypeError(f"Unsupported AST node: {type(node)}")

    # ------------------------------------------------------------------
    # Execution helpers
    # ------------------------------------------------------------------

    def _exec_get(self, node: GetNode):
        path = ".".join(node.path)

        try:
            return self.tree.get(path)
        except ConfigPathNotFoundError:
            if node.safe:
                return None
            raise

    def _exec_set(self, node: SetNode):
        path = ".".join(node.path)
        return self.tree.set(path, node.value)

    def _exec_delete(self, node: DeleteNode):
        path = ".".join(node.path)
        return self.tree.delete(path)
