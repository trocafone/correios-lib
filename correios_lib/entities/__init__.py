# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Trocafone
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################


class EntityBase():

    def __init__(self, wsdl, content=None, schema=None):
        """ Base entity used to all responses and requests.

        Args:
            content (dict): Keeps content to further validation
            wsdl (WebserviceBase): Used to get types used
            schema (voluptuous.Schema): Used to validate entity
        """
        self.wsdl = wsdl
        self.content = content
        self.schema = schema

    def validate(self):
        """ Validates content against schema

        In case of failure an error is kept inside the entity object,
        to be displayed by the client user if needed.

        Returns:
            bool: Validation result
        """
        try:
            self.schema(self.content)
            return True
        except Exception as e:
            self.error = e
            return False
