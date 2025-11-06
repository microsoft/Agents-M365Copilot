# Changelog

## [1.0.0](https://github.com/microsoft/Agents-M365Copilot/compare/Microsoft.Agents.M365Copilot-v0.1.0-preview.1...Microsoft.Agents.M365Copilot-v1.0.0) (2025-11-06)


### 🎉 First Stable Release

This marks the first stable release of the Microsoft.Agents.M365Copilot SDK, providing production-ready access to Microsoft 365 Copilot APIs v1.0.

### Features

* **generation:** initial add of request builders and models for dotnet v1 ([#197](https://github.com/microsoft/Agents-M365Copilot/issues/197)) ([46481fb](https://github.com/microsoft/Agents-M365Copilot/commit/46481fb8fc00e209ecc0ab7a945e2a381243d88d))
* **generation:** update request builders and models for dotnet v1 ([#205](https://github.com/microsoft/Agents-M365Copilot/issues/205)) ([10696c7](https://github.com/microsoft/Agents-M365Copilot/commit/10696c7aa00b39f0ec44aa3ab3be12b87d782c81))
* Full support for Copilot APIs v1.0 endpoints
* Stable API surface with semantic versioning guarantees
* Production-ready authentication with Azure Identity
* Support for .NET Standard 2.0, 2.1, .NET 8.0, and .NET 9.0

### 📦 What's Included
- Complete set of models for Copilot Retrieval API responses
- Request builders for Retrieval endpoint
- Integration with Microsoft.Agents.M365Copilot.Core

### 🔄 Migration from Preview
If you're upgrading from 0.1.0-preview.1:
1. Update your package reference to `Microsoft.Agents.M365Copilot` version `1.0.0`
2. No breaking API changes - your existing code should work as-is
3. Review the API documentation for any new features

### 📝 Notes
- The Beta and Core packages remain in preview status
- This stable release focuses on the v1.0 API endpoints only

## [0.1.0-preview.1](https://github.com/microsoft/Agents-M365Copilot/compare/Microsoft.Agents.M365Copilot-v0.1.0-preview.0...Microsoft.Agents.M365Copilot-v0.1.0-preview.1) (2025-10-29)


### Features

* **generation:** initial add of request builders and models for dotnet v1 ([#197](https://github.com/microsoft/Agents-M365Copilot/issues/197)) ([46481fb](https://github.com/microsoft/Agents-M365Copilot/commit/46481fb8fc00e209ecc0ab7a945e2a381243d88d))

## Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
