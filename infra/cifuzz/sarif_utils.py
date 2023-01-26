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
"""Module for outputting SARIF data."""
BUG_ID = 'bug'
RULES = [
  {
      'id': '1',  # Needs to be a stable, opaque identifier.
      'name': BUG_ID,
      'shortDescription': {
        'text': 'A bug'
      },
      'fullDescription': {
        'text': 'A bug'
      },
      'help': {
        'text': 'A bug'
      }
  }
]

def get_sarif_data(stacktrace):
  result = {
      'ruleId': BUG_ID,
      'partialFingerprints': {  # TODO(metzman): Use the stackframes.
        'primaryLocationLineHash': ''
      },
      'message': {
        'text': 'A bug'
      }
  }
  # TODO(metzman): Add location.
  run = {
      'tool': {
          'driver': {
              'name': 'CIFuzz',
              'rules': RULES,
              # TODO(metzman): Finish this.
              'informationUri': 'https://CIFuzz/Docs',
          },
      },
      'results': [result],
  }


  data = {
      '$schema': ('https://raw.githubusercontent.com/oasis-tcs/sarif-spec/'
                  'master/Schemata/sarif-schema-2.1.0.json'),
      'version': '2.1.0', # !!! Delete?
      'runs': [run]
  }
  return data


def write_sarif_data(stacktraces, workspace):
  data = get_sarif_data(stacktraces[0])
  with open(os.path.join(workspace.sarif, 'results.sarif')) as file_handle:
    file_handle.write(data)
