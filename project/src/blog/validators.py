from django.core.exceptions import ValidationError
# Create your models here.
def publish_email_validation(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Not a valid email")

def check_string_validation(value):
    if "amit" in value:
        return value
    else:
        raise ValidationError("Not in Amit")