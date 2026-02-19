BitHocker Discord Bot
￼ ￼ ￼
BitHocker is a versatile, custom Discord bot designed to enhance your server with advanced activity logging (messages, app usage, and call recordings), casual browsing interfaces for logs, assistive technology (AT) integrations for accessibility, and a “spy trap” security feature that detects unauthorized probes while handling remote third-party consent opt-ins. Built with Python and the discord.py library, it’s perfect for communities seeking transparency, inclusivity, and robust protection—whether you’re running a banter-filled editorial group (@contrakant) or aiming for “kings for quads” ♠️♦️ level interactions.
This bot turns your Discord server into a secure “Activity Vault,” ensuring ethical logging with user consent at its core.
Table of Contents
	•	Features
	•	Installation
	•	Configuration
	•	Usage
	•	Folder Structure
	•	Contributing
	•	License
	•	Contact
	•	Acknowledgements
Features
BitHocker offers a suite of powerful, modular features:
	•	Comprehensive Logging:
	◦	Messages: Captures texts, edits, deletes, and attachments for consented users.
	◦	App Usage: Tracks online time, voice activity, and status changes with daily/weekly reports.
	◦	Call Recordings: Stubs for voice channel recordings (integrate with external libs like pyaudio for full functionality).
	•	Casual Browsing:
	◦	Searchable log archives via commands (e.g., !log search keyword).
	◦	Visual dashboards for usage stats, accessible through dedicated channels.
	•	Assistive Technology Enhancements:
	◦	Text-to-Speech (TTS): Read logs aloud with commands like !tts "log text".
	◦	Speech-to-Text (STT) Stubs: For real-time captions in calls (extend with APIs like Wit.ai).
	◦	WCAG Compliance: High-contrast support, keyboard navigation, and simplified interfaces for users with disabilities.
	•	Spy Trap Security:
	◦	Honeypot Detection: Traps suspicious commands or probes, logging them to admin channels.
	◦	Third-Party Consent Opt-Ins: Securely handles remote signals via webhooks or commands, verifying API keys and notifying users.
	◦	Ethical Safeguards: All features require explicit consent, with easy revocation.
	•	Modular and Extensible:
	◦	Uses Discord cogs for easy feature addition/removal.
	◦	SQLite database for persistent storage of logs and consents.
	◦	Integration-ready for external tools (e.g., webhooks for third-party apps).
	•	Additional Perks:
	◦	AT-optimized alerts and notifications.
	◦	Customizable for themes like poker-inspired communities (♠️♦️).
BitHocker is designed with privacy in mind, complying with standards like GDPR and emphasizing user control.
Installation
Follow these steps to set up BitHocker on your local machine or a hosting service (e.g., Heroku, Replit, or a VPS).
Prerequisites
	•	Python 3.10 or higher.
	•	A Discord Developer account (for creating a bot application).
	•	Dependencies: discord.py, aiohttp, and sqlite3 (built-in).
Steps
	1	Clone the Repository: git clone https://github.com/yourusername/bithocker.git
	2	cd bithocker
	3	
	4	Install Dependencies: pip install -r requirements.txt
	5	
	6	Create a Discord Bot:
	◦	Go to the Discord Developer Portal.
	◦	Create a new application and add a bot.
	◦	Enable intents: Message Content, Members, and Voice States.
	◦	Copy the bot token.
	7	Set Environment Variables:
	◦	Create a .env file in the root directory: DISCORD_TOKEN=your_bot_token_here
	◦	
	◦	Optionally, add database paths or other configs.
	8	Invite the Bot to Your Server:
	◦	Use the OAuth2 URL generator in the Developer Portal to invite the bot with permissions like read/send messages, join voice, and manage roles.
	9	Run the Bot: python main.py
	10	 The bot should log in and appear online in your server.
For production, consider using a process manager like pm2 or deploying to a cloud service.
Configuration
Customize BitHocker via config.py:
	•	Channel IDs: Set IDs for log channels (e.g., LOG_CHANNEL_ID = 1234567890).
	•	Approved Third Parties: Add API keys for secure opt-ins (e.g., APPROVED_THIRD_PARTIES = ['trusted-app-key']).
	•	Database: Defaults to bithocker.db; modify in utils/database.py for other backends.
	•	Commands Prefix: Change in main.py (default: !).
For AT features, install optional libs like gtts for TTS: pip install gtts.
Update server roles and channels to match the design blueprint (e.g., create #message-logs, #spy-trap-logs).
Usage
Once running, interact with BitHocker using commands:
	•	Logging:
	◦	Messages are auto-logged for consented users.
	◦	!usage: View app usage stats.
	•	Recording:
	◦	!start_record: Begin voice recording (admin only).
	◦	!stop_record: End and upload recording.
	•	Accessibility:
	◦	!tts : Read text aloud (stub; extend with voice playback).
	◦	!caption: Generate call captions (stub).
	•	Spy Trap & Consent:
	◦	!third_party_optin : Apply remote consent (admin only).
	◦	Suspicious actions auto-trigger logs in #spy-trap-logs.
For consent: Users react to rules for manual opt-in; third-party signals via webhooks.
Test in a development server before production. Monitor console for errors.
Folder Structure
BitHocker/
├── main.py             # Bot entry point
├── config.py           # Constants, tokens, and settings
├── cogs/               # Modular cogs for features
│   ├── logging.py      # Message and usage logging
│   ├── recording.py    # Voice recording stubs
│   ├── accessibility.py # AT features like TTS/STT
│   └── spytrap.py      # Security and consent handling
├── utils/              # Helper modules
│   └── database.py     # SQLite database management
├── requirements.txt    # Python dependencies
├── .env.example        # Sample env file (rename to .env)
└── README.md           # This file
Contributing
Contributions are welcome! To contribute:
	1	Fork the repository.
	2	Create a feature branch (git checkout -b feature/AmazingFeature).
	3	Commit changes (git commit -m 'Add some AmazingFeature').
	4	Push to the branch (git push origin feature/AmazingFeature).
	5	Open a Pull Request.
Please follow code style guidelines (PEP 8) and add tests where possible.
Report issues or suggest features via the Issues tab.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
	•	Maintainer: kings for quads ♠️ ♦️
	•	X (Twitter): @contrakant
	•	Issues: GitHub Issues
	•	Email: (Add if desired)
For questions or collaborations, reach out on X or open an issue.
Acknowledgements
	•	Built with discord.py.
	•	Inspired by community needs for secure, accessible Discord servers.
	•	Thanks to open-source contributors for libraries like aiohttp and gtts.
	•	Special nod to banter enthusiasts—keep chasing those quads! ♠️♦️
