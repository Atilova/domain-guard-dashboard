from config import conf

from injector import Module, singleton, provider

from integration.adapters.accounts.IAccountInteractor import IAccountInteractor
from integration.interactors.accounts import AccountInteractorFactory

from infrastructure.redis.main import get_redis_factory


class DIModule(Module):
    """DIModule"""

    def __init__(self):
        self.__redis_client = get_redis_factory(conf.redis, 3)        
    
    @singleton
    @provider
    def account_interactor_factory(self) -> IAccountInteractor:
        return AccountInteractorFactory(redis_client=self.__redis_client)