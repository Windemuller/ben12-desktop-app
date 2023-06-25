from django.db import models


# Create your models here.

def get_last_client_id():
    last = Client.objects.order_by('id').last()
    return last.id if last is not None else 0


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default="No name", max_length=50)
    date_of_birth = models.DateTimeField("Date of Birth")
    date_created = models.DateTimeField("Date of account creation")
    last_measurement = models.DateTimeField("DateTime of last record", null=True)
    last_time_alcohol_consumed = models.DateTimeField("Last alcohol consumption", null=True)
    address = models.CharField(default="No address", max_length=50)

    def __str__(self):
        return f"Client {self.id} name: {self.name}"


class Record(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    heartbeat = models.FloatField(default=-1)
    blood_oxygen_level = models.FloatField(default=-1)
    alcohol_level = models.FloatField(default=-1)
    date_time_recording = models.DateTimeField("Time of data recording")
    date_time_sent = models.DateTimeField("Time of data transmission")

    def __str__(self):
        return f"Record for {self.client}, recorded {self.date_time_recording}, sent {self.date_time_sent}"


class RunningAverageDay(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    alcohol_level = models.FloatField(default=-1)
    blood_oxygen_level = models.FloatField(default=-1)
    heartrate = models.IntegerField(default=-1)
    num_records = models.IntegerField(default=0)
    date_last_updated = models.DateTimeField("Date of last update")

    def __str__(self):
        return f"Day average, last update {self.date_last_updated}, {self.client}"


class RunningAverageWeek(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    alcohol_level = models.FloatField(default=-1)
    blood_oxygen_level = models.FloatField(default=-1)
    heartrate = models.IntegerField(default=-1)
    num_records = models.IntegerField(default=0)
    date_last_updated = models.DateTimeField("Date of last update")

    def __str__(self):
        return f"Week average, last update {self.date_last_updated}, client {self.client}"


class RunningAverageMonth(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    alcohol_level = models.FloatField(default=-1)
    blood_oxygen_level = models.FloatField(default=-1)
    heartrate = models.IntegerField(default=-1)
    num_records = models.IntegerField(default=0)
    date_last_updated = models.DateTimeField("Date of last update")

    def __str__(self):
        return f"Month average, last update {self.date_last_updated}, client {self.client}"
