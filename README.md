# BitHocker Discord Bot

BitHocker is a versatile, custom Discord bot designed to enhance your
server with advanced activity logging (messages, app usage, and call
recordings), casual browsing interfaces for logs, assistive technology
(AT) integrations for accessibility, and a "spy trap" security feature
that detects unauthorized probes while handling remote third-party
consent opt-ins.

Built with Python and the discord.py library, it's ideal for communities
seeking transparency, inclusivity, and robust protection --- from
editorial banter groups to high-engagement themed communities.

BitHocker transforms your Discord server into a secure **Activity
Vault**, ensuring ethical logging with explicit user consent at its
core.

------------------------------------------------------------------------

## Table of Contents

-   Features
-   Installation
-   Configuration
-   Usage
-   Folder Structure
-   Contributing
-   License
-   Contact
-   Acknowledgements

------------------------------------------------------------------------

## Features

### Comprehensive Logging

-   **Messages** --- Captures texts, edits, deletes, and attachments for
    consented users.
-   **App Usage** --- Tracks online time, voice activity, and status
    changes with daily/weekly reports.
-   **Call Recordings** --- Voice channel recording stubs (extend with
    external libraries like `pyaudio`).

### Casual Browsing

-   Searchable log archives via commands (`!log search keyword`).
-   Usage dashboards accessible through dedicated channels.

### Assistive Technology Enhancements

-   **Text-to-Speech (TTS)** --- `!tts "log text"` (extend with `gtts`).
-   **Speech-to-Text (STT) Stubs** --- Extend with APIs such as Wit.ai.
-   **WCAG-aware Design** --- High-contrast support, keyboard-friendly
    workflows, simplified interfaces.

### Spy Trap Security

-   **Honeypot Detection** --- Logs suspicious probes to admin channels.
-   **Third-Party Consent Opt-Ins** --- Secure webhook/API-key-based
    remote signals.
-   **Ethical Safeguards** --- All logging requires explicit user
    consent with revocation support.

### Modular Architecture

-   Discord Cogs for modular feature control.
-   SQLite-backed persistence.
-   Integration-ready for external systems.

------------------------------------------------------------------------

## Installation

### Prerequisites

-   Python 3.10+
-   Discord Developer Account
-   Dependencies: `discord.py`, `aiohttp`, `sqlite3`

### Setup

Clone repository:

``` bash
git clone https://github.com/yourusername/bithocker.git
cd bithocker
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Create bot via Discord Developer Portal: - Enable intents: Message
Content, Members, Voice States - Copy bot token

Create `.env` file:

``` bash
DISCORD_TOKEN=your_bot_token_here
```

Run the bot:

``` bash
python main.py
```

For production deployment, use a process manager or cloud hosting
provider.

------------------------------------------------------------------------

## Configuration

Edit `config.py`:

-   `LOG_CHANNEL_ID`
-   `APPROVED_THIRD_PARTIES`
-   Database configuration
-   Command prefix (default: `!`)

Optional AT libraries:

``` bash
pip install gtts
```

Ensure required channels exist: - `#message-logs` - `#spy-trap-logs`

------------------------------------------------------------------------

## Usage

### Logging

-   Automatic logging for consented users.
-   `!usage` --- View usage statistics.

### Recording

-   `!start_record` (admin)
-   `!stop_record`

### Accessibility

-   `!tts`
-   `!caption`

### Spy Trap & Consent

-   `!third_party_optin` (admin)
-   Suspicious probes auto-log to spy-trap channel.

Always test in a development server before deploying to production.

------------------------------------------------------------------------

## Folder Structure

    BitHocker/
    ├── main.py
    ├── config.py
    ├── cogs/
    │   ├── logging.py
    │   ├── recording.py
    │   ├── accessibility.py
    │   └── spytrap.py
    ├── utils/
    │   └── database.py
    ├── requirements.txt
    ├── .env.example
    └── README.md

------------------------------------------------------------------------

## Contributing

1.  Fork repository
2.  Create feature branch
3.  Commit changes
4.  Push branch
5.  Open Pull Request

Follow PEP 8 standards and include tests where applicable.

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

## Contact

Maintainer: kings for quads ♠️♦️\
X (Twitter): @contrakant\
Issues: GitHub Issues

------------------------------------------------------------------------

## Acknowledgements

-   Built with discord.py
-   Inspired by community-driven transparency and accessibility needs
-   Thanks to open-source contributors of aiohttp and gtts
