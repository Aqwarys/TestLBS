from django.db import models

# Create your models here.
class Transactions(models.Model):
    sender = models.ForeignKey('user.BankAccount', on_delete=models.CASCADE, related_name='sent_transactions')
    recipient = models.ForeignKey('user.BankAccount', on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.sender.owner.username} sent {self.amount} to {self.recipient.owner.username}"