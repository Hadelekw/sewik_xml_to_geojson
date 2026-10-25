COORDINATE_FIELDS = ['WSP_GPS_X', 'WSP_GPS_Y']

# TODO: translate all fields
PASCAL_PL_TO_SNAKE_EN = {
    'DataUtworzenia': 'creation_date',
    'DataMod': 'modification_date',
    'SzkicZdarzenia': 'is_sketch',
    'ID': 'id',
    'JEDNOSTKA_MIEJSCA': 'administrative_unit',
    'WOJ': 'voivodeship',
    'POWIAT': 'county',
    'GMINA': 'municipality',
    'ULICA_ADRES': 'street_name',
    'NUMER_DOMU': 'house_number',
    'ZSSD_KOD': 'zssd_code',
    'DATA_ZDARZENIA': 'event_datetime',
    'DATA_ZDARZ': 'event_date',
    'GODZINA_ZDARZ': 'event_time'
}


FIELD_MAP = PASCAL_PL_TO_SNAKE_EN
