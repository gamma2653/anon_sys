from collections import Counter

from enum import Enum
import threading
import multiprocessing

from abc import ABC, abstractmethod

from typing import List, Type, Mapping, Union, NamedTuple, Iterable, Any



class Named(ABC):
    _name: str = None

    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name_):
        self._name = name_
    

class Factory(ABC):

    @abstractmethod
    def register_module(self, Mod: Type[Named]):
        ...

    @abstractmethod
    def make(self, Mod: Type[Named]):
        ...


class CountFactory(Factory):
    counts = Counter()

    def register_module(self, Named_: Type[Named]):
        
        self.counts[Named_] = 0

    def make(self, Named_: Type[Named]):
        
        try:
            self.counts[Named_]+=1
        except IndexError:
            self.counts[Named_]=1

        return Named_(name=Named_.__name__+self.counts[Named_])

class Module(Named):

    running: bool = False
    workers: multiprocessing.Pool

    def __init__(self, name, *args, **kwargs):
        self._name = name
    
    @abstractmethod
    def run(self, *args, **kwargs) -> None:
        self.running = True
    
    @abstractmethod
    def stop(self) -> None:
        self.running = False
    
    def is_running(self) -> bool:
        return self.running

class Sensor(Named):

    def __init__(self, name, *args, **kwargs):
        self._name = name
    
    @abstractmethod
    def read(b: int = 0):
        pass

    @abstractmethod
    def config(*args, **kwargs):
        pass


class Actuator:
    
    @abstractmethod
    def __init__(self, name, *args, **kwargs):
        self._name = name

    @abstractmethod
    def get_actions() -> Type[Enum]:
        pass

    @abstractmethod
    def do(action: Enum, *args, **kwargs):
        pass

class SubsystemData(NamedTuple):
    class_: Type[Named]
    count: int
    args: Iterable
    kwargs: Mapping[str, Any]
    factory: Factory


SYS_CONFIG: Mapping[str, Union[str, Mapping[str, Mapping[str, NamedTuple[]]]]] = {
    'name': 'Anon_sys',
    'subsystems': {
        'modules': {
            'facial_recognition': SubsystemData(Module, 1, [], {}, CountFactory())
        },
        'sensors': {
            'camera': SubsystemData(Sensor, 1, ['/dev/'], {}, CountFactory())
        },
        'actuators': {
            'servo1': SubsystemData(Actuator, 1, [], {'pin': 4}, CountFactory())
        }
    },
    'actions': {
        '[grpc_request]': lambda: None # IMPLEMENTLATER: map requests to these
    }
    
}

class System:
    modules: List[Module] = []
    sensor_listeners: List[Sensor] = []
    actuators: List[Actuator] = []
    subsystem_map = {}

    factories: Mapping[Factory] = {}
    config: Mapping[str, Union[str, Mapping[str, Mapping[str, SubsystemData]]]] = {}

    __default_config = {}

    def __init__(self, config: Mapping):
        self.load_config(config)
        self.subsystem_map = {
            'modules': self.modules,
            'sensors': self.sensor_listeners,
            'acuators': self.actuators
        }

    def load_config(self, config: Mapping = None):
        if config is None:
            config = self.__default_config
        self.config = config

    def load_subsystems(self, *subsystems: str):
        if not subsystems:
            subsystems = self.config['subsystems'].keys()        
        for subsystem in subsystems:
            for subsystem_name, subsystem_data in self.config['subsystems'][subsystem].items():
                self.modules.extend((subsystem_data.factory.make(subsystem_data['class']) for _ in range(subsystem_data['count'])))


    
    @classmethod
    def set_default_config(self, config: Mapping):
        self.__default_config = config



