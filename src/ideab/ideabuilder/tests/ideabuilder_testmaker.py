#coding: utf-8
from django.test import TestCase
from django.test import Client
from django import template
from django.db.models import get_model

class Testmaker(TestCase):

    #fixtures = ["ideabuilder_testmaker"]


    def test__130347494961(self):
        r = self.client.get('/', {})
        self.assertEqual(r.status_code, 404)
    def test_accounts_130347496238(self):
        r = self.client.get('/accounts/', {})
        self.assertEqual(r.status_code, 404)
    def test_ideabuilder_130347497351(self):
        r = self.client.get('/ideabuilder/', {})
        self.assertEqual(r.status_code, 404)
    def test_ideabuildersignup_130347497817(self):
        r = self.client.get('/ideabuilder/signup/', {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(unicode(r.context["csrf_token"]), u"""c57d2a4a9c75562c009c6448604e57b7""")
        self.assertEqual(unicode(r.context["form"]), u"""<tr><th><label for="id_username">Username:</label></th><td><input id="id_username" type="text" name="username" maxlength="10" /></td></tr>
<tr><th><label for="id_email">Email:</label></th><td><input id="id_email" type="text" name="email" maxlength="20" /></td></tr>
<tr><th><label for="id_password1">Password1:</label></th><td><input id="id_password1" type="password" name="password1" maxlength="20" /></td></tr>
<tr><th><label for="id_password2">Password2:</label></th><td><input id="id_password2" type="password" name="password2" maxlength="20" /></td></tr>""")
        self.assertEqual(unicode(r.context["STATIC_URL"]), u"""/static/""")
        self.assertEqual(unicode(r.context["LANGUAGES"]), u"""(('ar', 'Arabic'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-gb', 'British English'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy-nl', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('id', 'Indonesian'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('nb', 'Norwegian Bokmal'), ('nn', 'Norwegian Nynorsk'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'))""")
        self.assertEqual(unicode(r.context["user"]), u"""AnonymousUser""")
        self.assertEqual(unicode(r.context["LANGUAGE_CODE"]), u"""en-us""")
        self.assertEqual(unicode(r.context["LANGUAGE_BIDI"]), u"""False""")
        self.assertEqual(unicode(r.context["MEDIA_URL"]), u"""""")
    def test_ideabuildersignup_130347499998(self):
        r = self.client.post('/ideabuilder/signup/', {'username': 'user1', 'password1': 'user1', 'csrfmiddlewaretoken': '33f6db57b68d28ea8a93d3afe79cac9e', 'email': 'user1@a.com', 'password2': 'user1', })
    def test_ideabuilderlogin_130347501009(self):
        r = self.client.get('/ideabuilder/login/', {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(unicode(r.context["csrf_token"]), u"""96f6db19da7816927346a7f170e3afc0""")
        self.assertEqual(unicode(r.context["site_name"]), u"""example.com""")
        self.assertEqual(unicode(r.context["form"]), u"""<tr><th><label for="id_username">Username:</label></th><td><input id="id_username" type="text" name="username" maxlength="30" /></td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" id="id_password" /></td></tr>""")
        self.assertEqual(unicode(r.context["site"]), u"""example.com""")
        self.assertEqual(unicode(r.context["STATIC_URL"]), u"""/static/""")
        self.assertEqual(unicode(r.context["next"]), u"""""")
        self.assertEqual(unicode(r.context["LANGUAGES"]), u"""(('ar', 'Arabic'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-gb', 'British English'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy-nl', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('id', 'Indonesian'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('nb', 'Norwegian Bokmal'), ('nn', 'Norwegian Nynorsk'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'))""")
        self.assertEqual(unicode(r.context["user"]), u"""AnonymousUser""")
        self.assertEqual(unicode(r.context["LANGUAGE_CODE"]), u"""en-us""")
        self.assertEqual(unicode(r.context["LANGUAGE_BIDI"]), u"""False""")
        self.assertEqual(unicode(r.context["MEDIA_URL"]), u"""""")
    def test_ideabuilderlogin_130347501651(self):
        r = self.client.post('/ideabuilder/login/', {'username': 'user1', 'csrfmiddlewaretoken': '33f6db57b68d28ea8a93d3afe79cac9e', 'password': 'user1', 'next': '', })
    def test_ideabuilderlogin_130347502213(self):
        r = self.client.post('/ideabuilder/login/', {'username': 'user1', 'csrfmiddlewaretoken': '33f6db57b68d28ea8a93d3afe79cac9e', 'password': 'user1', 'next': '', })
    def test_ideabuilderlogin_130347502744(self):
        r = self.client.post('/ideabuilder/login/', {'username': 'user1', 'csrfmiddlewaretoken': '33f6db57b68d28ea8a93d3afe79cac9e', 'password': 'user1', 'next': '', })
    def test_ideabuilderlogout_130347502855(self):
        r = self.client.get('/ideabuilder/logout/', {})
    def test_ideabuilderlogin_130347503316(self):
        r = self.client.get('/ideabuilder/login/', {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(unicode(r.context["csrf_token"]), u"""32d006003133d2da0024d16e9c492123""")
        self.assertEqual(unicode(r.context["site_name"]), u"""example.com""")
        self.assertEqual(unicode(r.context["form"]), u"""<tr><th><label for="id_username">Username:</label></th><td><input id="id_username" type="text" name="username" maxlength="30" /></td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" id="id_password" /></td></tr>""")
        self.assertEqual(unicode(r.context["site"]), u"""example.com""")
        self.assertEqual(unicode(r.context["STATIC_URL"]), u"""/static/""")
        self.assertEqual(unicode(r.context["next"]), u"""""")
        self.assertEqual(unicode(r.context["LANGUAGES"]), u"""(('ar', 'Arabic'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-gb', 'British English'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy-nl', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('id', 'Indonesian'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('nb', 'Norwegian Bokmal'), ('nn', 'Norwegian Nynorsk'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'))""")
        self.assertEqual(unicode(r.context["user"]), u"""AnonymousUser""")
        self.assertEqual(unicode(r.context["LANGUAGE_CODE"]), u"""en-us""")
        self.assertEqual(unicode(r.context["LANGUAGE_BIDI"]), u"""False""")
        self.assertEqual(unicode(r.context["MEDIA_URL"]), u"""""")
    def test_ideabuilderlogin_130347503959(self):
        r = self.client.post('/ideabuilder/login/', {'username': 'user1', 'csrfmiddlewaretoken': '33f6db57b68d28ea8a93d3afe79cac9e', 'password': 'user1', 'next': '', })
