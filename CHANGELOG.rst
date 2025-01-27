=========
Changelog
=========

0.7.0 (2023-07-11)
==================

* Now requires ``zyte-parsers``.

* Added navigation classes: :class:`~zyte_common_items.ArticleNavigation`,
  :class:`~zyte_common_items.ProductNavigation`, the page classes that produce
  them, and other related classes.

* Improved the metadata field handling, also fixing some bugs:

  * Added :ref:`item-specific metadata classes <components-metadata>`. The
    ``metadata`` item fields were changed to use them.
  * **Backwards incompatible change**: the ``DateDownloadedMetadata`` class was
    removed. The item-specific ones are now used instead.
  * **Backwards incompatible change**:
    :class:`~zyte_common_items.ArticleFromList` no longer has a ``probability``
    field and instead has a ``metadata`` field like all other similar classes.
  * **Backwards incompatible change**: while in most items the old and the new
    type of the ``metadata`` field have the same fields, the one in
    :class:`~zyte_common_items.Article` now has ``probability``, the one in
    :class:`~zyte_common_items.ProductList` no longer has ``probability``, and
    the one in :class:`~zyte_common_items.ProductFromList` no longer has
    ``dateDownloaded``.
  * The default ``probability`` value is now ``1.0`` instead of ``None``.
  * Added the :class:`~zyte_common_items.HasMetadata` mixin which is used
    similarly to :class:`~web_poet.pages.Returns` to set the page metadata
    class.
  * Metadata objects assigned to the ``metadata`` fields of the items or
    returned from the ``metadata()`` methods of the pages are now converted to
    suitable classes.

* Added :func:`zyte_common_items.processors.breadcrumbs_processor` and enabled
  it for the ``breadcrumbs`` fields.

0.6.0 (2023-07-05)
==================

* Added :class:`~zyte_common_items.Article` and
  :class:`~zyte_common_items.ArticleList`.

* Added support for Python 3.11 and dropped support for Python 3.7.

0.5.0 (2023-05-10)
==================

* Now requires ``itemadapter >= 0.8.0``.

* Added :class:`~zyte_common_items.RealEstate`.

* Added the :meth:`zyte_common_items.BasePage.no_item_found` and
  :meth:`zyte_common_items.Page.no_item_found` methods.

* Improved the error message for invalid input.

* Added :class:`~zyte_common_items.ZyteItemKeepEmptyAdapter` and documented how
  to use it and :class:`~zyte_common_items.ZyteItemAdapter` in custom
  subclasses of :class:`itemadapter.ItemAdapter`.

0.4.0 (2023-03-27)
==================

* Added support for business places.


0.3.1 (2023-03-17)
==================

* Fixed fields from :class:`~zyte_common_items.BasePage` subclasses leaking
  across subclasses.
  (`#29 <https://github.com/zytedata/zyte-common-items/pull/29>`_,
  `#30 <https://github.com/zytedata/zyte-common-items/pull/30>`_)

* Improved how the :meth:`~zyte_common_items.Item.from_dict` and
  :meth:`~zyte_common_items.Item.from_list` methods report issues in the input
  data. (`#25 <https://github.com/zytedata/zyte-common-items/pull/25>`_)


0.3.0 (2023-02-03)
==================

* Added :ref:`page object classes <page-objects>` for e-commerce product detail
  and product list pages.


0.2.0 (2022-09-22)
==================

* Supports ``web_poet.RequestUrl`` and ``web_poet.ResponseUrl`` and
  automatically convert them into a string on URL fields like
  ``Product.url``.
* Bumps the ``web_poet`` dependency version from ``0.4.0`` to ``0.5.0``
  which fully supports type hints using the ``py.typed`` marker.
* This package now also supports type hints using the ``py.typed`` marker.
  This means mypy would properly use the type annotations in the items
  when using it in your project.
* Minor improvements in tests and annotations.


0.1.0 (2022-07-29)
==================

Initial release.
