from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from callboard.models import Review, Post


@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, created, **kwargs):
    if created:
        author = instance.author.authorUser

        msg = EmailMultiAlternatives(
            subject=instance.title,
            body=instance.text,
            from_email='',
            to=[author.email],
        )

        html_content = render_to_string(
            'signals/new_post.html',
            {
                'new': instance.title,
                'recipient': instance.author
            }
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Review)
def notify_new_review(sender, instance, created, **kwargs):
    if created:
        author = instance.reviewPost.author.authorUser

        msg = EmailMultiAlternatives(
            subject=instance.text,
            body=instance.text,
            from_email='',
            to=[author.email],
        )
        html_content = render_to_string(
            'signals/new_review.html',
            {
                'new': instance.text,
                'recipient': instance.reviewPost.author
            }
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Review)
def notify_review_status(sender, instance, **kwargs):
    if instance.status:

        author = instance.reviewUser

        msg = EmailMultiAlternatives(
            subject=instance.text,
            body=instance.text,
            from_email='',
            to=[author.email],
        )
        html_content = render_to_string(
            'signals/new_review_status.html',
            {
                'new': instance.text,
                'recipient': instance.reviewUser
            }
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()
