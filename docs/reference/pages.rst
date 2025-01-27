.. _page-object-api:

===============
Page object API
===============

Product
=======

.. autoclass:: zyte_common_items.BaseProductPage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.ProductPage(**kwargs)
   :show-inheritance:


Product list
============

.. autoclass:: zyte_common_items.BaseProductListPage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.ProductListPage(**kwargs)
   :show-inheritance:

Product navigation
==================

.. autoclass:: zyte_common_items.BaseProductNavigationPage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.ProductNavigationPage(**kwargs)
   :show-inheritance:

Article
=======

.. autoclass:: zyte_common_items.BaseArticlePage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.ArticlePage(**kwargs)
   :show-inheritance:


Article list
============

.. autoclass:: zyte_common_items.BaseArticleListPage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.ArticleListPage(**kwargs)
   :show-inheritance:


Article navigation
==================

.. autoclass:: zyte_common_items.BaseArticleNavigationPage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.ArticleNavigationPage(**kwargs)
   :show-inheritance:


Business place
==============

.. autoclass:: zyte_common_items.BaseBusinessPlacePage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.BusinessPlacePage(**kwargs)
   :show-inheritance:

Real estate
===========

.. autoclass:: zyte_common_items.BaseRealEstatePage(**kwargs)
   :show-inheritance:

.. autoclass:: zyte_common_items.RealEstatePage(**kwargs)
   :show-inheritance:


Custom page objects
===================

Subclass :class:`~zyte_common_items.Page` to create your own page object
classes that rely on :class:`~web_poet.page_inputs.http.HttpResponse`.

If you do not want :class:`~web_poet.page_inputs.http.HttpResponse` as input,
you can inherit from :class:`~zyte_common_items.BasePage` instead.

Your subclasses should also inherit generic classes
:class:`web_poet.pages.Returns` and :class:`zyte_common_items.HasMetadata` to
indicate their item and metadata classes.

.. autoclass:: zyte_common_items.BasePage(**kwargs)
   :show-inheritance:
   :members: no_item_found

   Base class for page object classes that has
   :class:`~web_poet.page_inputs.http.RequestUrl` as a dependency.

   .. data:: metadata

      Data extraction process metadata.

      :attr:`~zyte_common_items.Metadata.dateDownloaded` is set to the current
      UTC date and time.

      :attr:`~zyte_common_items.Metadata.probability` is set to ``1.0``.

   .. data:: url
      :type: str

      Main URL from which the data has been extracted.

.. autoclass:: zyte_common_items.Page(**kwargs)
   :show-inheritance:
   :members: no_item_found

   Base class for page object classes that has
   :class:`~web_poet.page_inputs.http.HttpResponse` as a dependency.

   .. data:: metadata
      :type: zyte_common_items.Metadata

      Data extraction process metadata.

      :attr:`~zyte_common_items.Metadata.dateDownloaded` is set to the current
      UTC date and time.

      :attr:`~zyte_common_items.Metadata.probability` is set to ``1.0``.

   .. data:: url
      :type: str

      Main URL from which the data has been extracted.

.. autoclass:: zyte_common_items.HasMetadata

.. autodata:: zyte_common_items.MetadataT
