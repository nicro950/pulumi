// Copyright 2016-2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Package engine contains the core logic for the Pulumi engine, which includes the following:
//
// - Handle resource management and query operations by configuring and spawning goroutines to run the specified
// operations asynchronously.
// - Define events and their associated handlers.
// - Manage journal entries for resource operations.
// - Manage plugins, including installation, version handling, and loading.
//
// The following interfaces are defined:
// - The QueryInfo interface, which handles information common to query operations (list, watch).
// - The RequiredPolicy interface, which represents a set of policies to apply during an update.
// - The SnapshotManager interface, which manages an in-memory resource graph.
// - The UpdateInfo interface, which handles information common to resource operations (update, preview, destroy,
// import, refresh).
package engine
