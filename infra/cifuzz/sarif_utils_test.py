# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for sarif_utils."""
import unittest

import sarif_utils

class GetSarifData(unittest.TestCase):
  def test_get_sarif_data(self):
    data = sarif_utils.get_sarif_data('', '')
    with open('/tmp/k.sarif', 'w') as fp:
      import json
      fp.write(json.dumps(data))
      # import pdb; pdb.set_trace()
