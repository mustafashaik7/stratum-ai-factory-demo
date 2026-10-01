# Patient Portal — thin consumer

Own patient screens, navigation, branding, accessibility, and approved configuration. Consume runtime capabilities through the shared client SDK.

See [Architecture.md](Architecture.md) and [application.json](application.json). This folder contains no UI implementation yet. The manifest uses the custom Stratum demo format.

Do not add booking services, EHR clients, model providers, orchestration, evaluation infrastructure, or telemetry backends here. Domain policy and vendor logic belong in the healthcare pack; shared enforcement and operations belong in the platform.
