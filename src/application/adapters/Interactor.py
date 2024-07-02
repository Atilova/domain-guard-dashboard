from typing import Generic, TypeVar


InputDTO = TypeVar("InputDTO")
OutputDTO = TypeVar("OutputDTO")


class Interactor(Generic[InputDTO, OutputDTO]):
    """Interactor"""
    
    def __call__(self, data: InputDTO) -> OutputDTO:
        raise NotImplementedError