from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from callboard.models import Review, Post


@receiver(post_save, sender=Post)
def my_handler(sender, instance, created, **kwargs):
    if not created:
        return
    mail = instance.author.authorUser.email
    send_mail(
        'New post added',
        f'Title: {instance.title}\n'
        f'Text: {instance.text}\n'
        f'Link to post: http://127.0.0.1:8000{instance.get_absolute_url()}',
        'host@mail.ru',
        [mail],
        fail_silently=False,
    )


@receiver(post_save, sender=Review)
def my_handler(sender, instance, created, **kwargs):
    if not created:
        return
    elif instance.status:
        mail = instance.reviewUser.email
        send_mail(
            'Your review received',
            f'Your feedback received. Link to post: http://127.0.0.1:8000{instance.reviewPost.get_absolute_url()}',
            'host@mail.ru',
            [mail],
            fail_silently=False,
        )
    mail = instance.reviewPost.author.authorUser.email
    send_mail(
        'New post review',
        f'New feedback to your post has been sent to the site. Link to post: http://127.0.0.1:8000{instance.reviewPost.get_absolute_url()}',
        'host@mail.ru',
        [mail],
        fail_silently=False,
    )
