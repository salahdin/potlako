from datetime import datetime
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT


style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'potlako'


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='potlako_subject.subjectvisit',
            appt_type='hospital')]


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP132'
    protocol_name = 'Potlako Plus'
    protocol_number = '132'
    protocol_title = ''
    study_open_datetime = datetime(
        2020, 3, 1, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Potlako Plus'
    institution = 'Botswana-Harvard AIDS Institute'



class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '132'


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'potlako_subject': ('subject_visit', 'potlako_subject.subjectvisit')}
    


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                             slots=[100, 100, 100, 100, 100, 100, 100]),
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])}


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):

    reason_field = {'potlako_subject.subjectvisit': 'reason'}
    other_visit_reasons = [
        'off study', 'deferred', 'Lost to follow-up', 'Death',
        'Missed quarterly visit']
    other_create_visit_reasons = [
        'Quarterly visit/contact', 'Unscheduled visit/contact']
    create_on_reasons = [SCHEDULED, UNSCHEDULED] + other_create_visit_reasons
    delete_on_reasons = [LOST_VISIT] + other_visit_reasons
