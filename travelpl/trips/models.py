from django.db import models

class TravelProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    start_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def update(self):
        has_places = self.places.exists()
        all_visited = not self.places.filter(is_visited=False).exists()
        if has_places and all_visited:
            self.is_completed = True
        else:
            self.is_completed = False
        self.save()

    def __str__(self):
        return self.name

class Place(models.Model):
    project = models.ForeignKey(TravelProject, on_delete=models.CASCADE, related_name='places')
    external_id = models.IntegerField()
    notes = models.TextField()
    is_visited = models.BooleanField(default=False)

    class Meta:
        unique_together = ('project', 'external_id')

    def __str__(self):
        return f"place {self.external_id} in {self.project.name}"

