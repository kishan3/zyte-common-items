from datetime import datetime

import attrs
from web_poet import ItemPage, RequestUrl, Returns, WebPage, field
from web_poet.pages import ItemT

from .components import Metadata
from .items import (
    Article,
    ArticleList,
    BusinessPlace,
    Product,
    ProductList,
    ProductNavigation,
    RealEstate,
)
from .util import format_datetime


def _date_downloaded_now():
    return format_datetime(datetime.utcnow())


class _BasePage(ItemPage[ItemT]):
    @field
    def metadata(self) -> Metadata:
        return Metadata(
            dateDownloaded=_date_downloaded_now(),
            probability=1.0,
        )

    def no_item_found(self) -> ItemT:
        """Return an item with the current url and probability=0,
        indicating that the passed URL doesn't contain the expected item.

        Use it in your .validate_input implementation.
        """
        return self.item_cls(  # type: ignore
            url=self.url,  # type: ignore[attr-defined]
            metadata=Metadata(probability=0, dateDownloaded=_date_downloaded_now()),
        )


@attrs.define
class BasePage(_BasePage):
    request_url: RequestUrl

    @field
    def url(self) -> str:
        return str(self.request_url)


class BaseArticlePage(BasePage, Returns[Article]):
    pass


class BaseArticleListPage(BasePage, Returns[ArticleList]):
    pass


class BaseBusinessPlacePage(BasePage, Returns[BusinessPlace]):
    pass


class BaseProductPage(BasePage, Returns[Product]):
    pass


class BaseProductListPage(BasePage, Returns[ProductList]):
    pass


class BaseRealEstatePage(BasePage, Returns[RealEstate]):
    pass


class BaseProductNavigationPage(BasePage, Returns[ProductNavigation]):
    pass


@attrs.define
class Page(_BasePage, WebPage):
    @field
    def url(self) -> str:
        return str(self.response.url)


class ArticlePage(Page, Returns[Article]):
    pass


class ArticleListPage(Page, Returns[ArticleList]):
    pass


class BusinessPlacePage(Page, Returns[BusinessPlace]):
    pass


class ProductPage(Page, Returns[Product]):
    pass


class ProductListPage(Page, Returns[ProductList]):
    pass


class RealEstatePage(Page, Returns[RealEstate]):
    pass


class ProductNavigationPage(Page, Returns[ProductNavigation]):
    pass
