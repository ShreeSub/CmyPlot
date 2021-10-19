from utils.routes import navbar_toggle, handle_routes
from pages.home import home
from pages.bad_url import bad_url
from pages.upload import upload
from pages.table import table
from pages.graph import graph


def test_navbar_toggle():

    clicks = 0
    is_open = True
    expected = is_open
    output = navbar_toggle.__wrapped__(clicks, is_open)
    assert output == expected

    clicks += 1
    expected = not is_open
    output = navbar_toggle.__wrapped__(clicks, is_open)
    assert output == expected


def test_handle_routes():

    pathname = '/'
    output = handle_routes.__wrapped__(pathname)
    assert output == home.layout

    pathname = '/home'
    output = handle_routes.__wrapped__(pathname)
    assert output == home.layout

    pathname = '/upload'
    output = handle_routes.__wrapped__(pathname)
    assert output == upload.layout

    pathname = '/table'
    output = handle_routes.__wrapped__(pathname)
    assert output == table.layout

    pathname = '/graph'
    output = handle_routes.__wrapped__(pathname)
    assert output == graph.layout

    pathname = 'totally-fake-path'
    output = handle_routes.__wrapped__(pathname)
    assert output == bad_url.layout
