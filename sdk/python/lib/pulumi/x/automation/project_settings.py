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
from typing import Optional, Mapping, Any, Union


@dataclass
class ProjectRuntimeInfo:
    """A description of the Project's program runtime and associated metadata."""
    name: str
    options: Optional[Mapping[str, Any]]


@dataclass
class ProjectTemplateConfigValue:
    """A placeholder config value for a project template."""
    description: Optional[str]
    default: Optional[str]
    secret: Optional[bool]


@dataclass
class ProjectTemplate:
    """A template used to seed new stacks created from this project."""
    description: Optional[str]
    quickstart: Optional[str]
    config: Mapping[str, ProjectTemplateConfigValue]
    important: Optional[bool]


@dataclass
class ProjectBackend:
    """Configuration for the project's Pulumi state storage backend."""
    url: Optional[str]


class ProjectSettings:
    """ A Pulumi project manifest. It describes metadata applying to all sub-stacks created from the project."""
    name: str
    runtime: Union[str, ProjectRuntimeInfo]
    main: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    website: Optional[str] = None
    license: Optional[str] = None
    config: Optional[str] = None
    template: Optional[ProjectTemplate] = None
    backend: Optional[ProjectBackend] = None

    def __init__(self,
                 name: str,
                 runtime: Union[str, ProjectRuntimeInfo],
                 main: Optional[str] = None,
                 description: Optional[str] = None,
                 author: Optional[str] = None,
                 website: Optional[str] = None,
                 license: Optional[str] = None,
                 config: Optional[str] = None,
                 template: Optional[ProjectTemplate] = None,
                 backend: Optional[ProjectBackend] = None):
        if isinstance(runtime, str) and runtime not in ["nodejs", "python", "go", "dotnet"]:
            raise ValueError(f"Invalid value {runtime!r} for runtime. "
                             f"Must be one of 'nodejs', 'python', 'go', 'dotnet'.")
        self.name = name
        self.runtime = runtime
        self.main = main
        self.description = description
        self.author = author
        self.website = website
        self.license = license
        self.config = config
        self.template = template
        self.backend = backend
