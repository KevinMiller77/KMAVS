from abc import ABC, abstractmethod

class AlgoBase(ABC):
    @abstractmethod
    def draw(self, dt):
        pass

    @abstractmethod
    def frame_step(self):
        pass

    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def new_set(self):
        pass