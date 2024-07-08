from abc import ABC, abstractmethod
from playwright.sync_api import Page

class BaseResolver(ABC):
    @abstractmethod
    def resolve(self, page: Page) -> bool:
        pass
