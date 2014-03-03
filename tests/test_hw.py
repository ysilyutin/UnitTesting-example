import sublime
from unittest import TestCase

class TestHelloWorld(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().run_command("close_file")

    if int(sublime.version())<3000:
        def test_hello_world_2(self):
            self.view.run_command("hello_world")
            first_row = self.view.substr(self.view.line(0))
            self.assertEqual(first_row,"hello world")

    if int(sublime.version())>=3000:
        def test_hello_world_3(self):
            self.view.run_command("hello_world")
            first_row = self.view.substr(self.view.line(0))
            self.assertEqual(first_row,"hello world")

    def test_hello_world(self):
        self.view.run_command("hello_world")
        first_row = self.view.substr(self.view.line(0))
        self.assertEqual(first_row,"hello world")