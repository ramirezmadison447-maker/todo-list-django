from django.db import models
from django.utils import timezone

class Priority(models.TextChoices):
    SIMPLE = 'simple', 'Simple (Blanco)'
    INTERMEDIO = 'intermedio', 'Intermedio (Amarillo)'
    URGENTE = 'urgente', 'Urgente (Rojo)'

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título de la tarea')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.SIMPLE,
        verbose_name='Prioridad'
    )
    completed = models.BooleanField(default=False, verbose_name='Completada')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_priority_color(self):
        """Retorna el color según la prioridad"""
        colors = {
            'urgente': '#dc3545',      # Rojo
            'intermedio': '#ffc107',   # Amarillo
            'simple': '#ffffff',       # Blanco
        }
        return colors.get(self.priority, '#ffffff')

    def get_priority_text_color(self):
        """Retorna el color del texto según la prioridad"""
        text_colors = {
            'urgente': '#ffffff',      # Blanco
            'intermedio': '#000000',   # Negro
            'simple': '#000000',       # Negro
        }
        return text_colors.get(self.priority, '#000000')
