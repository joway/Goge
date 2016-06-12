from rest_framework import routers

from posts.apis import PostViewSet
from users.apis import UserViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"user", UserViewSet, base_name="user")
router.register(r"post", PostViewSet, base_name="post")
# router.register(r"oauth", SocialAuthViewSet, base_name="oauth")
