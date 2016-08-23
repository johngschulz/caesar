#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from helpers import alphabet_position, rotate_character

#forms for rotation encryption and text
rot_form = """
    <form method="post">
        <label>
            Rotate amount:
        <br>
            <input type="text" name="rotation" value="%(rotation)s">
        <br>
        </label>
        <label>
            Input text to rotate:
        <br>
            <input name="text" value="%(text)s">
        </label>
            <input type="submit" value="Rot It"/>
        <div style="color:red">%(error)s</div>
    </form>
        """

def encrypt(text, rot):
    crypt_text = ""
    for i in text:
        crypt_text = crypt_text + rotate_character(i, rot)
    return(crypt_text)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", rotation="", text=""):
        self.response.write(rot_form % {"error":error,
                                        "rotation":rotation,
                                        "text": text})
    def get(self):
        self.write_form()

    def post(self):
        user_rot = self.request.get(cgi.escape("rotation"))
        user_text = self.request.get(cgi.escape("text"))
        text = encrypt(user_text, user_rot)
        self.write_form("",user_rot,text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
