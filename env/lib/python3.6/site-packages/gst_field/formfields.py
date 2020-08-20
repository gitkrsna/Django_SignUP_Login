# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports
from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _

# Project imports
from gst_field.validators import gstin_check, pan_check


class GSTField(CharField):
    default_error_messages = {"invalid": _("Enter a valid GST number.")}
    default_validators = [gstin_check]

    def __init__(self, **kwargs):
        super().__init__(strip=True, **kwargs)


class PANField(CharField):
    default_error_messages = {"invalid": _("Enter a valid PAN number.")}
    default_validators = [pan_check]

    def __init__(self, **kwargs):
        super().__init__(strip=True, **kwargs)
