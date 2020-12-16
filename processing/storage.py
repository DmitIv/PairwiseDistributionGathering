from typing import Any, NoReturn


class Storage:
    def store(self, data: Any) -> NoReturn:
        raise NotImplementedError


class AStorage:
    async def store(self, data: Any) -> NoReturn:
        raise NotImplementedError
