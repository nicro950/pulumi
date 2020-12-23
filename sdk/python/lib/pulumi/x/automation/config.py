# Copyright 2016-2020, Pulumi Corporation.
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

from dataclasses import dataclass
from typing import Optional, MutableMapping


@dataclass
class ConfigValue:
    """
    ConfigValue is the input/output of a `pulumi config` command.
    It has a plaintext value, and an option boolean indicating secretness.
    """
    value: str
    secret: Optional[bool]


ConfigMap = MutableMapping[str, ConfigValue]
"""ConfigMap is a map of string to ConfigValue."""
