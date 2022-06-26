import phonenumbers

from numb import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

gb_number = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(gb_number))