from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


potlako = Navbar(name='potlako')

potlako.append_item(
    NavbarItem(
        name='eligible_subject',
        label='Subject Screening',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')))

potlako.append_item(
    NavbarItem(
        name='endpoint_recordings',
        label='Endpoint Recordings',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('endpoint_listboard_url')))

potlako.append_item(
    NavbarItem(
        name='potlako_subject',
        label='Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))

site_navbars.register(potlako)
