from django.db import models


class Position(models.Model):
    name = models.CharField("Должность", max_length=120)
    is_active = models.BooleanField("Активна?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Employee(models.Model):
    full_name = models.CharField("ФИО", max_length=120)
    contacts = models.CharField("Контакты", max_length=200)
    start_date = models.DateTimeField("Дата начала работы")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
<<<<<<< HEAD
    salary = models.DecimalField("Оклад", default=0)

=======
    salary = models.DecimalField("Оклад", max_digits=6, decimal_places=2, default=0)
    
>>>>>>> 5bea44272223611e72a239f4bb7cb96e11acb03e
    def __str__(self):
        return self.full_name, self.position

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
