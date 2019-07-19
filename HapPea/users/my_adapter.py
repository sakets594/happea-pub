from .models import CustomUser

# from allauth.account.models import EmailAccount
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # This isn't tested, but should work
        try:
            print("here")
            print(sociallogin.user)
            print("asdf")
            user = CustomUser.objects.get(email=sociallogin.email)
            sociallogin.connect(request, user)
            # Create a response object
            raise ImmediateHttpResponse(response)
        except CustomUser.DoesNotExist:
            print("exception")
            pass