from django.contrib.gis.db import models


class Track(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.LineStringField()

    def __str__(self):
        return self.name


class Cable(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.LineStringField()

    def __str__(self):
        return self.name


class Manhole(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='manholes')

    def __str__(self):
        return self.name


class Segment(models.Model):
    cable = models.ForeignKey(Cable, on_delete=models.CASCADE, related_name='segments')
    start_manhole = models.ForeignKey(Manhole, on_delete=models.CASCADE, related_name='start_segments')
    end_manhole = models.ForeignKey(Manhole, on_delete=models.CASCADE, related_name='end_segments')
    geometry = models.LineStringField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Segment from {self.start_manhole} to {self.end_manhole}"


class Duct(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='ducts')
    geometry = models.LineStringField()

    def __str__(self):
        return f"Duct in {self.track}"


class SubDuct(models.Model):
    duct = models.ForeignKey(Duct, on_delete=models.CASCADE, related_name='subducts')
    geometry = models.LineStringField()

    def __str__(self):
        return f"SubDuct in {self.duct}"
