# from django.contrib.auth.models import AnonymousUser, User
# from django.test import RequestFactory, TestCase

# from .models import Playlist
# from .views import PlaylistViewSet

# class SimpleTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='ayasse', email='ayasser@gmail.com', password='top_secret')
#         self.playlist = Playlist.objects.create()

#     def test_details(self):
#         request = self.factory.post('playlist/', data={'title':'coding_playlist'}, content_type='application/json')

#         request.user = self.user
#         response = PlaylistViewSet(request)
#         print(response)
#         # response = send_sms(request)
#         self.assertEqual(response.status_code, 200)