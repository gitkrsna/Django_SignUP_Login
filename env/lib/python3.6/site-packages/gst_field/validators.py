# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python imports
import re

# Django imports
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Project imports
from gst_field.constants import GSTIN_MAX_LENGTH, PAN_MAX_LENGTH


PAN_REGEX = "[A-Z]{3}[CPHFATBLJGE]{1}[A-Z]{1}\d{4}[A-Z]{1}"  # noqa

GSTIN_REGEX = "(3[0-7]|[1-2][0-9]|0[1-9])%s\d[Z]{1}[A-Z\d]{1}" % PAN_REGEX  # noqa


def gstin_check(value):
    """Checks a values validates as a GST Number.

    NOTE:
        A GST number is 15 digit alphanumeric.
        eg. 24 AAACB5343E 1 Z 7
        - First 2 digits are state code ranges 01-37
        - Next 10 digits is PAN Card number
            * First 3 are alphabets ranges from AAA-ZZZ
            * Next alphabet is either C,P,H,F,A,T,B,L,J,G,E
            * Next alphabet of Surname or Name
            * Next 4 digits range from 0001 to 9999
            * Next alphabetic check digit
        - 13th alphabets assigned based on the no. of reg. within a state
        - 14th alphabets will be Z by default
        - Last digit will be for check code. It may be an alphabet or a number.
    """
    pattern = re.compile(GSTIN_REGEX)
    if pattern.match(value) is None:
        raise ValidationError(
            _("Invalid GSTIN"), code="invalid_gst_number"
        )


def pan_check(value):
    """Checks a values validates as a PAN Number.

    NOTE:
        A PAN number is 10 digit alphanumeric.
        eg. AAA C B 5343 E
        - First 3 are alphabets ranges from AAA-ZZZ
        - Next alphabet is either C,P,H,F,A,T,B,L,J,G,E
        - Next alphabet of Surname or Name
        - Next 4 digits range from 0001 to 9999
        - Next alphabetic check digit
    """
    pattern = re.compile(PAN_REGEX)
    if pattern.match(value) is None:
        raise ValidationError(
            _("Invalid PAN"), code="invalid_pan_number"
        )
