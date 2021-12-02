class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name:
            return not typed
        if len(name)>len(typed):
            return False
        if name[0] == typed[0]:
            return self.isLongPressedName(name[1:],typed[1:]) or self.isLongPressedName(name,typed[1:])
