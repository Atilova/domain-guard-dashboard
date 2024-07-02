from injector import Module, singleton, provider

from integration.adapters.accounts.IAccountInteractor import IAccountInteractor
from integration.interactors.accounts import AccountInteractorFactory


class DIModule(Module):
    """DIModule"""
    
    @singleton
    @provider
    def account_interactor_factory(self) -> IAccountInteractor:
        return AccountInteractorFactory()