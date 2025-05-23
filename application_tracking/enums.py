from django.db import models

EmploymentType = [
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("Contract", "Contract")
]


ExperienceLevel = [
    ("Entry Level", "Entry Level"),
    ("Mid Level", "Mid Level"),
    ("Senior", "Senior"),
]


LocationTypeChoice = [
    ("Onsite", "Onsite"),
    ("Hybrid", "Hybrid"),
    ("Remote", "Remote"),
]


class ApplicationStatus(models.TextChoices):
    APPLIED = ("APPLIED", "APPLIED")
    REJECTED = ("REJECTED", "REJECTED")
    INTERVIEW = ("INTERVIEW", "INTERVIEW")