import peewee

# db connection to be initialized and used around the system
db = None

# max number of inserts that can be done in a single bulk
SQLITE_MAX_VARIABLE_NUMBER = 2 ** 16


class Agency(peewee.Model):
    agency_id = peewee.FixedCharField(
        max_length=3, null=False, primary_key=True)
    agency_name = peewee.CharField(max_length=40, null=False)
    agency_url = peewee.CharField(max_length=60, null=False)
    agency_timezone = peewee.CharField(max_length=20, null=False)

    agency_lang = peewee.CharField(max_length=10, null=True)
    agency_phone = peewee.CharField(max_length=20, null=True)
    agency_fare_url = peewee.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'agency'


class Stop(peewee.Model):
    stop_id = peewee.CharField(primary_key=True)
    stop_code = peewee.CharField()
    stop_name = peewee.CharField(max_length=50, null=False)

    stop_lat = peewee.CharField(null=False)
    stop_lon = peewee.CharField(null=True)
    stop_url = peewee.CharField(max_length=60)
    wheelchair_boarding = peewee.CharField(null=True)

    class Meta:
        db_table = 'stops'


class Route(peewee.Model):
    route_id = peewee.CharField(primary_key=True)
    agency_id = peewee.ForeignKeyField(Agency)

    route_short_name = peewee.CharField(max_length=10, null=False)
    route_long_name = peewee.CharField(max_length=40, null=False)
    route_type = peewee.CharField(max_length=10, null=False)
    route_url = peewee.TextField()
    route_color = peewee.CharField(max_length=6)
    route_text_color = peewee.CharField(max_length=6)

    class Meta:
        db_table = 'routes'


class Trip(peewee.Model):
    id = peewee.PrimaryKeyField()
    route_id = peewee.ForeignKeyField(Route)
    service_id = peewee.CharField(null=False)
    trip_id = peewee.CharField(max_length=20, null=False)

    trip_headsign = peewee.CharField(max_length=50)
    direction_id = peewee.CharField()
    shape_id = peewee.CharField(max_length=15)
    wheelchair_accessible = peewee.CharField()
    note_fr = peewee.CharField(max_length=255)
    note_en = peewee.CharField(max_length=255)

    class Meta:
        db_table = 'trips'


class StopTime(peewee.Model):
    trip_id = peewee.ForeignKeyField(Trip, null=False)
    arrival_time = peewee.CharField(max_length=8, null=False)
    departure_time = peewee.CharField(max_length=8, null=False)
    stop_id = peewee.ForeignKeyField(Stop, null=False)
    stop_sequence = peewee.CharField(null=False)

    class Meta:
        db_table = 'stop_times'


class CalendarDate(peewee.Model):
    calendar_id = peewee.PrimaryKeyField()
    service_id = peewee.CharField(null=False)
    date = peewee.DateField(null=False)
    exception_type = peewee.CharField(null=False)

    class Meta:
        db_table = 'calendar_dates'
