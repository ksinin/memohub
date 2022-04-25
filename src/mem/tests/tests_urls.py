from django.test import SimpleTestCase
from django.urls import reverse, resolve

from mem.views import AddMemView, YourMemView, DeleteMemView, EditMemView, MemLikeView, UserFollowingView, \
    UserFollowersView, FollowToggleUserView


class TestUrls(SimpleTestCase):

    def test_addmem_url_resolves(self):
        url = reverse('addmem')
        self.assertEqual(resolve(url).func.view_class, AddMemView)

    def test_yourmemes_url_resolves(self):
        url = reverse('yourmemes', args=[1])
        self.assertEqual(resolve(url).func.view_class, YourMemView)

    def test_deletemem_url_resolves(self):
        url = reverse('deletemem', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteMemView)

    def test_editmem_url_resolves(self):
        url = reverse('editmem', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditMemView)

    def test_mem_like_url_resolves(self):
        url = reverse('mem_like', args=[1])
        self.assertEqual(resolve(url).func.view_class, MemLikeView)

    def test_user_following_list_url_resolves(self):
        url = reverse('user_following_list', args=[self.id])
        self.assertEqual(resolve(url).func.view_class, UserFollowingView)

    def test_user_followers_list_url_resolves(self):
        url = reverse('user_followers_list', args=[self.id])
        self.assertEqual(resolve(url).func.view_class, UserFollowersView)

    def test_user_follow_unfollow_url_resolves(self):
        url = reverse('user_follow_unfollow', args=[self.id])
        self.assertEqual(resolve(url).func.view_class, FollowToggleUserView)


# class ViewsTestCase(TestCase):
#
#     """The index page loads properly"""
#
#     client = Client()
#
#     def test_addmem_url_loads_properly(self):
#         response = self.client.get(reverse('addmem'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_yourmemes_url_loads_properly(self):
#         response = self.client.get(reverse('yourmemes', args=[self.userName]))
#         self.assertEqual(response.status_code, 200)


