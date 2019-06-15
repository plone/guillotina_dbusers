
from guillotina.catalog.catalog import DefaultSearchUtility


def is_default_catalog(catalog):
    return isinstance(catalog, DefaultSearchUtility)

